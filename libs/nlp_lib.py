# Enumeration class to avoid hardcoded strings in later code
class Sentiments:
    positive = 'POSITIVE'
    negative = 'NEGATIVE'
    neutral = 'NEUTRAL'

# Review class to objectify a review to make code more readable.
# Will take the overall rating and review text of a specific review
# and create an object for that particular review.

class Reviews:
    def __init__(self, review_text, review_rating):
        self.review_text = review_text
        self.review_rating = review_rating
        self.sentiment = self.get_sentiment()

    # Takes the objects review_rating and returns
    # a sentiment, based on the numerical value

    def get_sentiment(self):
        if self.review_rating <= 2:
            return Sentiments.negative
        elif self.review_rating >= 4:
            return Sentiments.positive
        else:
            return Sentiments.neutral
