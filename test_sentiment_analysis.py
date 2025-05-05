import SentimentAnalysis

import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyser(self):
        result_1 = SentimentAnalysis.sentiment_analyser('I love working with Python')
        print(result_1)
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        
        # Test case for negative sentiment
        result_2 = SentimentAnalysis.sentiment_analyser('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        
        # Test case for neutral sentiment
        result_3 = SentimentAnalysis.sentiment_analyser('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL') 



unittest.main()  