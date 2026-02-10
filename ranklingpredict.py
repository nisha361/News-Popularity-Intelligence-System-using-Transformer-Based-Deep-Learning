import torch
from transformers import DistilBertTokenizer
from models.encoder import NewsEncoder
from models.popularity_head import PopularityHead

tokenizer = DistilBertTokenizer.from_pretrained(
    "distilbert-base-uncased"
)

encoder = NewsEncoder()
head = PopularityHead()

encoder.load_state_dict(torch.load("models/saved/encoder.pt"))
head.load_state_dict(torch.load("models/saved/head.pt"))

encoder.eval()
head.eval()

def predict_popularity(title, description):
    text = title + " " + description
    tokens = tokenizer(
        text,
        truncation=True,
        padding=True,
        return_tensors="pt"
    )

    with torch.no_grad():
        embedding = encoder(**tokens)
        score = head(embedding)
proxy_score = proxy_popularity(text)


final_score = (score + proxy_score) * 5
return round(min(max(final_score, 0), 10), 2)
