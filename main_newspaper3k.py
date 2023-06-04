import newspaper
from newspaper import fulltext


# Example usage
article_url = 'https://www.flightglobal.com/strategy/latin-america-at-risk-of-being-left-behind-on-sustainable-aviation-fuel/153537.article'  # Replace with your desired URL
article = newspaper.Article(article_url)
article.download()
article.parse()
article.nlp()
print(article.keywords)
print(article.summary)

