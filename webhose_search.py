import json
import urllib.parse
import urllib.request

from pip._vendor.distlib.compat import raw_input


def read_webhose_key():
    webhose_api_key = None

    try:
        with open('search.key', 'r') as f:
            webhose_api_key = f.readline().strip()
    except:
        raise IOError('search.key file not found')

    return webhose_api_key


def run_query(search_terms, size=10):
    webhose_apy_key = read_webhose_key()

    if not webhose_apy_key:
        raise KeyError('Webhose key not found')

    root_url = 'http://webhose.io/search'

    query_string = urllib.parse.quote(search_terms)

    search_url = ('{root_url}?token={key}&format=json&q={query}'
                  '&sort=relevancy&size={size}').format(
        root_url=root_url,
        key=webhose_apy_key,
        query=query_string,
        size=size)

    results = []

    try:

        response = urllib.request.urlopen(search_url).read().decode('utf-8')
        json_response = json.loads(response)

        for post in json_response['posts']:
            results.append({'title': post['title'],
                            'link': post['url'],
                            'summary': post['text'][:200]})

    except:
        print("Error when querying the Webhose API")

    return results


def main():
    query = raw_input("Enter the query to search: ")

    results = run_query(query)

    for result in results:
        print(("{title}\n"
               "{link}\n"
               "{summary}\n").format(
            title=result['title'],
            link=result['link'],
            summary=result['summary']
        ))
        print("\n")


if __name__ == '__main__':
    main()
