# Prompt patterns

Sonar API can answer with web grounding, but the prompt still matters.

## Source-first research

```text
Summarize the latest official updates about Amazon Bedrock.
Prioritize official AWS documentation and include source URLs.
```

## Comparison research

```text
Compare Perplexity Sonar API and a general LLM API for developer use.
Use freshness, citations, latency, cost, and operational complexity as criteria.
```

## Source quality request

```text
Separate official documentation, vendor blogs, news articles, and community posts.
Mark non-official sources as requiring additional review.
```

## Structured answer request

```text
Return the answer in this shape:
- summary
- key points
- source review notes
- links
```

## Practical rules

- Specify a time window for freshness-sensitive questions.
- Ask for official sources first when accuracy matters.
- Tell the model what language to answer in.
- Review sources before using the answer in production workflows.
