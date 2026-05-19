#!/usr/bin/env python3
"""portfolio_status.py -- Show OutrageousStorm GitHub portfolio stats
Fetches all repos, calculates stats, shows trending
"""
import subprocess, json, urllib.request

def github_api(path):
    url = f"https://api.github.com/users/OutrageousStorm/{path}"
    req = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json'})
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except:
        return {}

def main():
    repos = github_api("repos?per_page=100&sort=stars")
    if not repos:
        print("Could not fetch repos")
        return
    
    total_stars = sum(r['stargazers_count'] for r in repos)
    total_forks = sum(r['forks_count'] for r in repos)
    languages = {}
    
    for r in repos:
        if r.get('language'):
            languages[r['language']] = languages.get(r['language'], 0) + 1
    
    print(f"\n📊 OutrageousStorm Portfolio Stats")
    print(f"{'─'*40}")
    print(f"Repos:        {len(repos)}")
    print(f"Total stars:  {total_stars}⭐")
    print(f"Total forks:  {total_forks}")
    print(f"\n Languages:")
    for lang, count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        print(f"  {lang:<15} {count} repos")
    
    print(f"\n🔝 Top 5:")
    for i, r in enumerate(repos[:5], 1):
        print(f"  {i}. {r['name']:<35} {r['stargazers_count']:>3}⭐")

if __name__ == "__main__":
    main()
