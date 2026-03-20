---
name: scrapling-fetcher
description: Web scraping using Scrapling framework with adaptive parsing and anti-crawler bypass capabilities.
---

# Scrapling Web Fetcher

Fetch web pages using Scrapling with support for static, dynamic, and stealth modes.

## Usage

### Basic Fetch (Static Pages)

```bash
./skills/scrapling-fetcher/fetch.sh "https://example.com"
```

### Stealth Fetch (Anti-Crawler Sites)

```bash
./skills/scrapling-fetcher/fetch.sh --stealth "https://protected-site.com"
```

### Extract Data with CSS Selector

```bash
./skills/scrapling-fetcher/fetch.sh --selector "h1::text" "https://example.com"
```

## Features

- ✅ **Adaptive Parsing** - Automatically adapts to website structure changes
- ✅ **Anti-Crawler Bypass** - Bypasses Cloudflare Turnstile and other protections
- ✅ **High Performance** - Up to 698x faster than BeautifulSoup
- ✅ **Multiple Modes** - Static, Dynamic (Playwright), and Stealth modes
- ✅ **CSS/XPath Selectors** - Full selector support

## Output Format

```json
{
  "url": "https://example.com",
  "status": 200,
  "title": "Example Domain",
  "content": "<html>...",
  "extracted": "Extracted text"
}
```

## Requirements

- Python 3.9+
- scrapling package (`pip install scrapling`)
