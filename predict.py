import numpy as np
from textblob import TextBlob

urgency_words = ["breaking", "urgent", "alert", "shocking", "crisis"]

def urgency_score(text):
    text = text.lower()
    return sum(word in text for word in urgency_words) / len(urgency_words)

def lexical_diversity(text):
    words = text.split()
    return len(set(words)) / (len(words) + 1)

def length_score(text):
    return min(len(text) / 300, 1)

def sentiment_intensity(text):
    polarity = TextBlob(text).sentiment.polarity
    return abs(polarity)  # emotional strength, not direction

def predict_popularity(title, desc):
    text = title + " " + desc

    u = urgency_score(text)
    l = lexical_diversity(text)
    ln = length_score(text)
    s = sentiment_intensity(text) 

    # Weakly supervised popularity score
    score = (0.35 * u) + (0.25 * l) + (0.2 * ln) + (0.2 * s)

    return float(score * 10)  # Scale to 0–10


def explain_prediction(title, desc):
    text = title + " " + desc
    explanations = []

    if urgency_score(text) > 0:
        explanations.append(
            "Contains urgency-related or breaking-news language, increasing immediate attention."
        )

    if sentiment_intensity(text) > 0.4:
        explanations.append(
            "Contains strong emotional cues, which often increase reader engagement and sharing."
        )

    if lexical_diversity(text) > 0.5:
        explanations.append(
            "Uses diverse vocabulary, improving clarity and reader engagement."
        )

    if length_score(text) > 0.7:
        explanations.append(
            "Provides detailed context, making the article more informative."
        )

    if not explanations:
        explanations.append(
            "The article has a neutral tone with moderate informational structure."
        )

    return explanations
