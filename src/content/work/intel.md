---
title: Intel Application - Discover for free what is trending on the web, media, and more.
publishDate: 2024-03-02 00:00:00
img: https://i.imgur.com/98wN3R6.png
img_alt: today intel
description: |
  The API is designed to provide various functionalities related to NLP, Article Extraction, News, Trends, Article Summarization
tags:
  - Python
  - Fast Api
  - Spacy NLP
  - Text Summarization
  - Entity Extraction
  - Sentiment Analysis
---

# Intel API Documentation

This repository contains the API documentation for the tools running on my [Website](https://izdrail.com).

The API was designed to provide various functionalities to developers related to news, SEO analysis, NLP, videos, and more.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Request Examples](#request-examples)
- [Response Examples](#response-examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This API is the backend for the all the tools running on my [Website](https://izdrail.com) app. 
It is a RESTful API, providing endpoints for fetching news, running SEO analysis, performing NLP tasks, and more. It adheres to the OpenAPI 3.1.0 specification.

## Getting Started

To get started with the this Intel API, follow these steps:

1. Clone the repository.
2. Review the API documentation to understand available endpoints and their functionalities.
3. Set up the required dependencies.
4. Make requests to the API endpoints as needed.

For more details, refer to the [Terms of Service](https://izdrail.com/terms). provided by [Laravel Developer](https://izdrail.com).

## API Endpoints

- **POST /feed/reader:** Reads the rss feed and return latest items from the feed in a json format
- **POST /feed/finder:** Find relevant feeds.
- **POST /run/scrapper:** Run a web scraper.
- **POST /jobs:** Searches fo jobs.
- **GET /google/trending:** Get trending Google searches.
- **POST /google/news/search:** Search Google News.
- **POST /google/news/topic:** Get news on a specific topic.
- **POST /seo/analyze:** Analyze SEO for a given link.
- **POST /seo/lighthouse:** Run Lighthouse SEO analysis.
- **POST /nlp/article:** Perform NLP analysis on an article.
- **POST /videos/youtube:** Search for videos on YouTube.
- **GET /:** Root endpoint.

For detailed information on request and response formats, refer to the OpenAPI specification in the `openapi.yaml` file.

## Request Examples

### Fetch News Feed

This endpoint will efficiently retrieve and process new items from a specified RSS or Atom feed. 
It will extract relevant data from each item, such as title, description, publication date, author, and any custom fields defined in the feed. 
The response will be a well-structured JSON object, providing a clear and concise representation of the feed content.

- `link`: The link to the feed.
- `format`: The format of the feed.
- `items`: The list of items in the feed.


Example Request:
```json
{
  "link": "https://example.com/feed"
}
```

Example Response:
```json
{
  "link": "https://example.com/feed",
  "format": "json",
  "items": [
    {
      "title": "My Title",
      "link": "https://example.com/article",
      "description": "My Description"
    }
    ]}

```

### Run SEO Analysis

This endpoint will leverage Lighthouse, a powerful web performance auditing tool, to conduct a comprehensive analysis of a specified web page. 
It will evaluate various aspects of the page's performance, accessibility, best practices, and SEO, providing valuable insights for optimization. 
The results will be returned in a well-structured JSON format, making it easy to interpret and integrate into client applications.

```json
{
  "link": "https://example.com",
  "format": "json|html"
}
```
### Perform NLP Analysis
This endpoint will extract content from a provided url and return the results as a JSON Format.


```json
{
  "link": "https://example.com/article"
}
```
## Response Examples

### Successful Response

```json
{
  "data": "..."
}
```

### Validation Error

  ```json
  {
  "detail": [
    {
      "loc": [],
      "msg": "Validation error message",
      "type": "error_type"
    }
  ]
}
  ```
