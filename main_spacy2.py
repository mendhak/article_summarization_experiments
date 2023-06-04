import spacy
import requests
from bs4 import BeautifulSoup
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

nlp = spacy.load("en_core_web_sm")

stopwords = list(STOP_WORDS)

def extract_text_from_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'
    }
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text

# Example usage
article_url = 'https://www.flightglobal.com/strategy/latin-america-at-risk-of-being-left-behind-on-sustainable-aviation-fuel/153537.article'  # Replace with your desired URL
article_text = extract_text_from_url(article_url)


docx = nlp(article_text)
mytokens = [token.text for token in docx]

# for entity in docx.ents:
#     print(entity.text, entity.label_)

word_frequencies = {}

for word in docx:
    if word.text not in stopwords:
        if word.text not in word_frequencies.keys():
            word_frequencies[word.text] = 1
        else:
            word_frequencies[word.text] += 1
        

maximum_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)



sentence_list = [ sentence for sentence in docx.sents ]

sentence_scores = {}

for sent in sentence_list:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if len(sent.text.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]




threshold = 0.8


for i in sentence_scores:
    if sentence_scores[i] > threshold:
        print(i)