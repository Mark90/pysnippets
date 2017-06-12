import requests
from collections import Counter
from celery import task, chord, chain

@task(ignore_result=False)
def find_frequency(link_text, user_words):
    # we live the implementation as an exercise to the reader :)
    return {'foo': 1, 'bar': 1, 'baz': 1}

@task(ignore_result=False)
def scrape_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

@task(ignore_result=False)
def aggregate_results(results):
    counter = Counter()
    for result in results:
        counter.update(result)
    # do something with data
    return counter


user_submitted_words = ['foo', 'bar', 'john']
urls_to_scrape = []

async_result = chord(
    [chain(
        scrape_url.subtask(args=(url,)),
        find_frequency.subtask(args=(user_submitted_words,)))
     for url in urls_to_scrape]
)(aggregate_results.s())