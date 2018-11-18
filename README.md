# Reddit Scraper 

A simple scraper that scrapes the top *X* posts from a given *subreddit* thread, and
the top level comments belonging to those posts. 

This simple scraper was created for an academic project. 

## Setup
- Set up an **app** [here](https://www.reddit.com/prefs/apps).
- Fill out the `KEY_sample.py` and rename it to `KEY.py`.

## Usage
```python
// Create your virtual environment, f.x.:
python3 -m venv reddit-scrape
// Activate it, f.x.:
. reddit-scrape/bin/activate
// Install dependencies 
pip install -r requirements.txt 
// Run the scraper 
python scraper <subreddit-name> <number-of-posts>
```

 

