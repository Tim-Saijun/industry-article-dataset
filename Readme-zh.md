# 数据集介绍

该数据集用于对大模型进行微调，来源于对 [reads.alibaba.com](https://reads.alibaba.com) 网站中13个分类的2185个页面的抓取。以下是该数据集包含的字段及其描述：

## 数据字段

| 字段名              | 描述                           |
|-------------------|------------------------------|
| title             | 页面标题                       |
| keywords          | 页面关键词                      |
| word_count        | 页面内容的字数                   |
| description       | 页面描述                       |
| date_published    | 发布日期                       |
| content           | 页面内容                       |
| category          | 页面分类                       |
| estimated_token   | 页面内容的估算token数 (内容长度除以4) |
| h2_count          | 页面中H2标题的数量               |
| h3_count          | 页面中H3标题的数量               |
| p_count           | 页面中段落的数量                 |
| url               | 页面链接                       |

## 数据统计

- **总页面数**: 2185
- **分类数**: 13

## 数据用途
该数据集主要用于对大模型进行微调，通过丰富的数据字段，模型能够学习到不同类型内容的写作风格和结构，从而提升生成内容的质量和多样性。

## 分类详情

13个分类领域如下：

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

## 示例

```json
{
    'title': '示例标题',
    'keywords': ['示例', '关键词'],
    'word_count': 1200,
    'description': '这是一个示例描述。',
    'date_published': '2024-01-01',
    'content': '这是页面的完整内容。',
    'category': '示例分类',
    'estimated_token': 300,
    'h2_count': 5,
    'h3_count': 10,
    'p_count': 20,
    'url': 'https://reads.alibaba.com/example-page'
}
```