import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
    const blog = await getCollection('articles');
    return rss({
        title: 'Software development agency',
        description: 'A humble Astronaut’s guide to the stars',
        site: "https://izdrail.com",
        items: blog.map((post) => ({
            title: post.data.title,
            pubDate: post.data.pubDate,
            description: post.data.description,
            // Compute RSS link from post `slug`
            // This example assumes all posts are rendered as `/blog/[slug]` routes
            link: `/articles/${post.slug}/`,
        })),
    });
}
