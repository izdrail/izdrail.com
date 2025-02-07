from fastapi import APIRouter
from pydantic import BaseModel
import spacy
from newspaper import Article, Config
from markdownify import markdownify as md
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import yake
import socials
import socid_extractor
import socialshares
from spacy import displacy

# Initialize FastAPI Router
router = APIRouter()

# Load SpaCy Model
nlp = spacy.load("en_core_web_trf")

# Initialize Sentiment Analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Constants
EXCLUDED_ENTITY_TYPES = {"TIME", "DATE", "LANGUAGE", "PERCENT", "MONEY", "QUANTITY", "ORDINAL", "CARDINAL"}

# Request Models
class ArticleAction(BaseModel):
    link: str


class SummarizeAction(BaseModel):
    text: str


# Helper Functions
def fetch_article(link: str):
    """Fetch and parse an article using the Newspaper library."""
    user_agent = "NLP/0.0.1 (Unix; Intel) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/50.0.2661.102 Safari/537.36"
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 10
    config.fetch_images = True
    config.memoize_articles = True
    config.follow_meta_refresh = True

    article = Article(link, config=config, keep_article_html=True)
    article.download()
    article.parse()
    return article


def extract_keywords(text: str, language="en", n=1, dedup_lim=0.9, top=5):
    """Extract keywords using YAKE."""
    extractor = yake.KeywordExtractor(lan=language, n=n, dedupLim=dedup_lim, top=top)
    return sorted(extractor.extract_keywords(text), key=lambda x: x[1])


def filter_entities(doc):
    """Filter and deduplicate entities."""
    entities = [(ent.label_, ent.text) for ent in doc.ents if ent.label_ not in EXCLUDED_ENTITY_TYPES]
    return list(dict.fromkeys(entities))  # Deduplicate by text


# Routes
@router.post("/nlp/article")
async def process_article(article: ArticleAction):
    try:
        # Fetch article
        crawler = fetch_article(article.link)

        # NLP Processing
        doc = nlp(crawler.text)
        filtered_entities = filter_entities(doc)

        # Social and Sentiment Analysis
        social_accounts = socials.extract(article.link).get_matches_per_platform()
        social_shares = socialshares.fetch(article.link, ["facebook", "pinterest", "linkedin", "google", "reddit"])
        sentiment_scores = sentiment_analyzer.polarity_scores(crawler.text)

        # Generate SpaCy HTML
        spacy_html = displacy.render(doc, style="ent", options={"ents": [e[0] for e in filtered_entities]})

        # Extract Keywords
        keywords = extract_keywords(crawler.text, top=5)

        # Response
        return {
            "data": {
                "title": crawler.title,
                "date": crawler.publish_date,
                "text": crawler.text,
                "markdown": md(crawler.article_html, newline_style="BACKSLASH", strip=["a"], heading_style="ATX"),
                "html": crawler.article_html,
                "summary": crawler.summary,
                "keywords": keywords,
                "authors": crawler.authors,
                "banner": crawler.top_image,
                "images": crawler.images,
                "entities": filtered_entities,
                "videos": crawler.movies,
                "social": social_accounts,
                "spacy": spacy_html,
                "spacy_markdown": md(spacy_html, newline_style="BACKSLASH", strip=["a"], heading_style="ATX"),
                "sentiment": sentiment_scores,
                "accounts": socid_extractor.extract(crawler.text),
                "social-shares": social_shares,
            },
        }
    except Exception as e:
        return {"error": str(e)}


@router.post("/nlp/tags")
async def extract_tags(article: SummarizeAction):
    try:
        keywords = extract_keywords(article.text, n=3, top=5)
        return {"data": keywords}
    except Exception as e:
        return {"error": str(e)}
