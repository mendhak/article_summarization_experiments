import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

# Function to extract text content from the article URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text

# Example usage
article_url = 'https://code.mendhak.com/use-wildcard-certificates-for-internal-infrastructure/'  # Replace with your desired URL
article_text = extract_text_from_url(article_url)
summary = summarize(article_text)
print(summary)