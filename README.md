# 🧠 COOLSCRAPER — AI news → ready-to-post social content

Automated pipeline that collects Artificial Intelligence news from international media, uses an LLM to
write short social-media posts, and pushes them to Google Sheets. From there, schedulers like
Make, Zapier, n8n or Buffer can publish them.

```
RSS feeds ──► keyword filter ──► OpenAI (title + ≤280-char summary) ──► Google Sheets ──► Make / Zapier / Buffer
                     │                          │
                     └── log_history/*.json ◄───┘   (+ token usage & cost per run)
```

## Features

- **Multi-source ingestion**: BBC, NYTimes, MIT Technology Review, El País, Xataka and more. Sources are configured in `feeds_rss.json`.
- **Keyword filtering** with word boundaries, so "IA" does not match "noticia". Keywords live in `keywords_ia.json`.
- **LLM copywriting**: each story becomes a catchy title plus a summary of 280 characters or less, with the source link.
- **Cost tracking**: every run reports tokens used and an approximate cost in USD and EUR.
- **Google Sheets export**: rows are appended with a `pendiente` (pending) status, ready for any no-code publisher.
- **Run history**: raw news and generated posts are saved as timestamped JSON files.

## Tech

Python 3.11+ · feedparser · OpenAI API · gspread (Google service account) · python-dotenv · schedule

## Project structure

```
├── main.py                 # Orchestrates the pipeline
├── modules/
│   ├── scraper.py          # RSS ingestion + keyword filter
│   ├── generador.py        # LLM post generation + token/cost tracking
│   └── exportador.py       # Google Sheets export
├── feeds_rss.json          # Sources
├── keywords_ia.json        # Filter keywords
├── .env.example            # Configuration template
└── log_history/            # Run output (git-ignored)
```

## Getting started

```bash
pip install -r requirements.txt
cp .env.example .env        # then fill in your keys
python main.py
```

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key |
| `OPENAI_MODEL` | Model to use (default `gpt-4o-mini`) |
| `SPREADSHEET_ID` | ID of the target Google Sheet |
| `GOOGLE_SERVICE_ACCOUNT_PATH` | Path to the service-account JSON. Share the sheet with that account's email |

If Google Sheets is not configured, the pipeline still runs and saves its output to `log_history/`.

## Security

Credentials are loaded only from environment variables. `.env` and service-account files are
git-ignored and never committed.

---

Built by [Juan Dalebrook](https://github.com/jdalebrook) · [dalebrook.org](https://dalebrook.org)
