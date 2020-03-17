import os
import json
import utils


def print_json(info):
    print(json.dumps(info, indent=4))
    pass


article = 'balanced_scorecard'
art_dict = utils.get_article_by_id(article)
print(art_dict)
