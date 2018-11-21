import praw 
import pandas as pd 
import datetime as dt 
from KEYS import *
import sys 

REDDIT_API_CLIENT = praw.Reddit(client_id=PERSONAL_USE_SCRIPT, 
                                client_secret=SECRET,
                                user_agent=NAME, 
                                username=DEVELOPER,
                                password=PASSWORD,
                               )


def get_date(created):
    return dt.datetime.fromtimestamp(created)

def scrape_data(subreddit, number_of_posts):
    subreddit = REDDIT_API_CLIENT.subreddit(subreddit)
    top_subreddit = subreddit.top(limit=number_of_posts)

    topics_dict = {
        "title": [],
        "score": [], 
        "id": [],
        "comms_num": [],
        "created": [],
        "body": [],
    }

    comments_dict = {
        "body": [],
        "created": [],
        "id": [],
    }

    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
        for top_level_comment in submission.comments:
            if hasattr(top_level_comment, "body"):
                comments_dict["body"].append(top_level_comment.body)
                comments_dict["created"].append(top_level_comment.created)
                comments_dict["id"].append(top_level_comment.id)

    topics_data = pd.DataFrame(topics_dict)
    comments_data = pd.DataFrame(comments_dict)
    topics_data.index.name = 'index'
    comments_data.index.name = 'index'

    _timestamp = topics_data["created"].apply(get_date)
    _timestamp_2 = comments_data["created"].apply(get_date)

    topics_data = topics_data.assign(timestamp = _timestamp)
    comments_data = comments_data.assign(timestamp = _timestamp_2)

    return topics_data, comments_data


def to_csv(subreddit, posts, comments):
    posts.to_csv(subreddit + '_posts.csv', index=True) 
    comments.to_csv(subreddit + '_comments.csv', index=True)


if __name__ == "__main__":
    subreddit = sys.argv[1] 
    number_of_posts = int(sys.argv[2])
    posts, comments = scrape_data(subreddit=subreddit, number_of_posts=number_of_posts)
    to_csv(subreddit, posts, comments)





