""" This module snchronises the database with the post reposotory on GitHub. """


from model import db
from .aggregator import PostAggregator


def synchronize():

    pa = PostAggregator()
    repo = pa.get_repo_hash()
    files = pa.get_file_hashes(repo)

    for file_id in files:
        text = pa.get_file_content(file_id)

