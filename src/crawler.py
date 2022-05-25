import requests
import os
from dotenv import load_dotenv
import time
import csv

subjects = [
    'nasa',
    'music',
    'sports',
    'science',
    'art',
    'history',
    'psychology',
    'technology',
    'university',
    'vacation',
    'biology',
    'mechanics',
    'computer',
    'programming',
    'nature',
    'networks',
    'security',
    'artificial intelligence',
    'artist',
    'movies',
]

search_url = "https://api.twitter.com/2/tweets/search/recent"
query_params = lambda query : { 'query': f'{query} -is:retweet lang:en', 'max_results': 100 }

def bearer_oauth(request):
    load_dotenv('config.env')
    bearer_token = f"Bearer {os.environ.get('BEARER_TOKEN')}"
    request.headers['Authorization'] = bearer_token

    return request
    
def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():

    output_file_path = 'data/raw/output.csv'

    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    
    iterations_count = 25
    length = len(subjects)
    counter = 0 
    for i in range(iterations_count):
        for j in range(length):
            print('----------')
            print(f"Request #{counter + 1}")
            params = query_params(subjects[j])
            json_response = connect_to_endpoint(search_url, params)
            data = []
            
            for tweet in json_response['data']:
                data.append([tweet['text']])

            with open(output_file_path, 'a', encoding='UTF8', newline='') as file:
                writer = csv.writer(file, skipinitialspace=True)
                writer.writerows(data)
            
            print('waiting for 10s ...')
            time.sleep(10)
            counter += 1

    print('----------')
    print(f"Total number of requests: {counter}")
    print(f'{(counter) * 100} tweets crawled')

if __name__ == '__main__':
    main()



