# Dataset Introduction

This dataset is used for fine-tuning a large model, sourced from 2185 pages across 13 categories on the [reads.alibaba.com](https://reads.alibaba.com) website. Below are the fields included in the dataset and their descriptions:

## Data Fields

| Field Name        | Description                           |
|-------------------|---------------------------------------|
| title             | Page title                            |
| keywords          | Page keywords                         |
| word_count        | Word count of the page content        |
| description       | Page description                      |
| date_published    | Publication date                      |
| content           | Page content                          |
| category          | Page category                         |
| estimated_token   | Estimated token count of the content (content length divided by 4) |
| h2_count          | Number of H2 headings on the page     |
| h3_count          | Number of H3 headings on the page     |
| p_count           | Number of paragraphs on the page      |
| url               | Page URL                              |

## Data Statistics

- **Total Pages**: 2185
- **Categories**: 13

## Data Usage
This dataset is primarily used for fine-tuning large models. With its rich data fields, the model can learn the writing styles and structures of different types of content, thereby enhancing the quality and diversity of generated content.

## Category Details

The 13 categories are as follows:

- Apparel & Accessories
- Beauty & Personal Care
- Consumer Electronics
- Home & Garden
- Home Improvement
- Chemicals & Plastics
- Machinery
- Mother, Kids & Toys
- Packaging & Printing
- Raw Materials
- Renewable Energy
- Sports
- Vehicle Parts & Accessories

## Example

```json
{
    "title": "Example Title",
    "keywords": ["example", "keywords"],
    "word_count": 1200,
    "description": "This is an example description.",
    "date_published": "2024-01-01",
    "content": "This is the full content of the page.",
    "category": "Example Category",
    "estimated_token": 300,
    "h2_count": 5,
    "h3_count": 10,
    "p_count": 20,
    "url": "https://reads.alibaba.com/example-page"
}
```