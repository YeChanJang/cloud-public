# Operation checklist

## API key

- [ ] Keep API keys out of source code.
- [ ] Store keys in `.env`, CI secrets, or a secret manager.
- [ ] Prevent keys from appearing in logs.

## Response quality

- [ ] Inspect citations or search results.
- [ ] Separate official docs from blogs and news articles.
- [ ] Add a time window for freshness-sensitive questions.
- [ ] Review high-impact answers before acting on them.

## Cost and performance

- [ ] Log request count and model name.
- [ ] Track usage fields when available.
- [ ] Set timeouts.
- [ ] Use retries carefully.
- [ ] Use streaming only when the UX needs it.
- [ ] Cache repeated research queries where appropriate.

## Reliability

- [ ] Handle API errors without exposing raw stack traces to users.
- [ ] Add backoff for rate limits.
- [ ] Prepare fallback messages for external API failures.
- [ ] Validate optional response fields before rendering them.
