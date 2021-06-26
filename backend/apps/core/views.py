import requests
import json
from pprint import PrettyPrinter
from django.shortcuts import render


def get_trending():
    url = "https://bing-news-search1.p.rapidapi.com/news"

    querystring = {"textFormat": "Raw", "safeSearch": "Off",
                   "headlineCount": "8", "cc": "IN"}

    headers = {
        'x-bingapis-sdk': "true",
        'x-rapidapi-key': "edd273c1a4msheb86eae47ecdb2ep12c1fcjsn245c5ded093a",
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    fetched_content = json.loads(response.text)['value']

    return fetched_content


def get_news(query):
    url = "https://bing-news-search1.p.rapidapi.com/news/search"

    querystring = {"q": query, "safeSearch": "Off",
                   "textFormat": "Raw", "freshness": "Day", "cc": "IN", "count": "8"}

    headers = {
        'x-bingapis-sdk': "true",
        'x-rapidapi-key': "edd273c1a4msheb86eae47ecdb2ep12c1fcjsn245c5ded093a",
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    fetched_content = json.loads(response.text)['value']

    return fetched_content


def home_page(request):
    status = request.user.is_authenticated
    if status:
        query = request.GET.get('query')
        data = {}
        if query is not None:
            print(f'Query = {query}')

            related_list = get_news(query)

            results_list = []
            for item in related_list:
                if len(results_list) > 5:
                    break
                try:
                    article = {}
                    article['title'] = item['name']
                    article['summary'] = item['description']
                    article['source'] = item['url']
                    article['siteimg'] = item['image']['thumbnail']['contentUrl']
                except:
                    continue
                results_list.append(article)

            data["search"] = True
            data["results"] = results_list

        fetched_content = get_trending()
        articles_list = []
        for item in fetched_content:
            if len(articles_list) >= 8:
                break
            try:
                article = {}
                article['title'] = item['name']
                article['summary'] = item['description']
                article['source'] = item['url']
                article['siteimg'] = item['image']['thumbnail']['contentUrl']
                article['published'] = item['datePublished'][:10]
            except:
                continue
            articles_list.append(article)

        printer = PrettyPrinter(indent=4, depth=4)
        printer.pprint(articles_list)

        data["articles"] = articles_list

        return render(request=request, template_name='index.html', context=data)
    return render(request=request, template_name='home.html')
