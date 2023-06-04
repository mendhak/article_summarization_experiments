import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Function to extract text content from the article URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text

# Function to preprocess the text
def preprocess_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    preprocessed_sentences = []
    for sentence in sentences:
        # Tokenize sentence into words
        words = sentence.split()

        # Remove stopwords and perform stemming
        filtered_words = [stemmer.stem(word) for word in words if word.lower() not in stop_words]

        # Join filtered words back into a sentence
        preprocessed_sentence = ' '.join(filtered_words)
        preprocessed_sentences.append(preprocessed_sentence)

    return preprocessed_sentences

# Function to generate summary from preprocessed sentences
def generate_summary(sentences, num_sentences=3):
    ranked_sentences = {}
    for i, sentence in enumerate(sentences):
        ranked_sentences[i] = len(sentence)

    sorted_sentences = sorted(ranked_sentences, key=ranked_sentences.get, reverse=True)
    top_sentences = sorted_sentences[:num_sentences]
    summary = ' '.join([sentences[i] for i in top_sentences])
    return summary

# Example usage
article_url = 'https://code.mendhak.com/use-wildcard-certificates-for-internal-infrastructure/'  # Replace with your desired URL
article_text = extract_text_from_url(article_url)
preprocessed_sentences = preprocess_text(article_text)
summary = generate_summary(preprocessed_sentences)
print(summary)