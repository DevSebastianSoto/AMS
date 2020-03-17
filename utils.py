import os
import json


def readJson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_article_by_id(id: str):
    articles_json = readJson(os.path.join('content', 'articles.json'))
    for a in articles_json:
        if a['href'] == id:
            return a


def get_full_project_info():
    projects = readJson(os.path.join('content', 'projects.json'))
    technologies = readJson(os.path.join('content', 'technologies.json'))
    full = []
    for k, v in projects.items():
        for proj in v:
            proj["techs"].append(k)
            full_techs = []
            proj["techs"].sort()
            for tech in proj["techs"]:
                full_techs.append({
                    "name": technologies[tech]['name'],
                    "color": technologies[tech]['color'],
                })
            proj['techs'] = full_techs
            full.append(proj)
    return full
