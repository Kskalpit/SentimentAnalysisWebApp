import json

from sentiment_analysis import sentiment_analyser
response = sentiment_analyser("I love this new technology")

formatted_response = json.loads(response)

label = formatted_response['documentSentiment']['label']
score = formatted_response['documentSentiment']['score']