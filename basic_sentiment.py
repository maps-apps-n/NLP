from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analysis = TextBlob("TextBlob text text text text")

print(dir(analysis))

print(analysis.sentiment)





