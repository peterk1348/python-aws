#!/usr/bin/env python
from runtime_context import LOGGER
import requests


def get_top_story(event, context):
    """retrieve the top story from HackerNews
    https://github.com/HackerNews/API
    """
    LOGGER.debug('get_top_story - ENTRY')
    top_stories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    assert top_stories.status_code == 200, 'Failed to get top stories [{}]'.format(top_stories.status_code)
    top_story_id = top_stories.json()[0]
    LOGGER.info('get_top_story - top_story_id={}'.format(top_story_id))
    top_story = requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json'.format(top_story_id))
    assert top_story.status_code == 200, 'Failed to get the top story [{}]'.format(top_stories.status_code)
    story = top_story.json()
    LOGGER.debug('get_top_story - EXIT')
    return {
        'statusCode': 200,
        'body': '"{}" by {} on {}'.format(story.get('title'), story.get('by'), story.get('url')),
        'headers': {
            'content-type': 'text/plain'
        }
    }
