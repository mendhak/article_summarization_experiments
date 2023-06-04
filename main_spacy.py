import requests
from bs4 import BeautifulSoup
import spacy


# Function to extract text content from the article URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text

# Example usage
article_url = 'https://code.mendhak.com/use-wildcard-certificates-for-internal-infrastructure/'  # Replace with your desired URL
article_text = extract_text_from_url(article_url)

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Process the article text
doc = nlp(article_text)

# Extract sentences and calculate their similarity scores
sentences = [sent.text for sent in doc.sents]
sentence_scores = {sent: sent._.trf_word_pieces_similarity for sent in doc.sents}

# Sort sentences based on their similarity scores
sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

# Generate the summary by selecting the top sentences
num_sentences = 3  # Number of sentences in the summary
summary = ' '.join(sorted_sentences[:num_sentences])
print(summary)