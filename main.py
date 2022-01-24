import argparse
import requests
import os
from urllib.parse import urlparse 
from dotenv import load_dotenv


ADDRESS = 'https://api-ssl.bitly.com'


def shorten_link(token, link):
  endpoint = '/v4/shorten'
  headers = {'Authorization': f'Bearer {token}'}
  content = {"long_url": link, "domain": "bit.ly"}
  response = requests.post(f'{ADDRESS}{endpoint}', headers=headers, json=content)
  response.raise_for_status()
  return response.json()['link']


def count_clicks(token, link):
  parsed = urlparse(link) 
  bitlink = f'{parsed.hostname}{parsed.path}'
  endpoint = f'/v4/bitlinks/{bitlink}/clicks/summary'
  headers = {'Authorization': f'Bearer {token}'}
  response = requests.get(f'{ADDRESS}{endpoint}', headers=headers)
  response.raise_for_status()
  return response.json()['total_clicks']


def is_bitlink(token, link):
  parsed = urlparse(link)
  bitlink = f'{parsed.hostname}{parsed.path}'
  endpoint = f'/v4/bitlinks/{bitlink}'
  headers = {'Authorization': f'Bearer {token}'}
  response = requests.get(f'{ADDRESS}{endpoint}', headers=headers)
  return response.ok


if __name__ == "__main__":
  load_dotenv()
  token = os.environ['BITLY_API_TOKEN']
  
  parser = argparse.ArgumentParser(
    description='''Returns the short link or the number 
    of clicks on the short link using the bit.ly service'''
  )
  parser.add_argument('link', help='Link or bitlink')
  args = parser.parse_args()

  link = args.link
  
  try:
    if is_bitlink(token, link):
      clicks_count = count_clicks(token, link)
      print('Clicks:', clicks_count)  
    else:
      bitlink = shorten_link(token, link)
      print('Shortlink:', bitlink)
  except requests.exceptions.HTTPError as error:
    print(f'An http-error has occurred: {error.response.status_code} {error.response.reason}')
  except requests.exceptions.Timeout:
    print('Error: Timeout expired')
   