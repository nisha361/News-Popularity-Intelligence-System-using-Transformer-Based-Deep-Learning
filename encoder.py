import torch
from transformers import DistilBertModel

class NewsEncoder:
def __init__(self):
self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
self.model = DistilBertModel.from_pretrained('distilbert-base-uncased')
self.model.eval()


def encode(self, texts):
inputs = self.tokenizer(texts, return_tensors='pt', truncation=True, padding=True)
with torch.no_grad():
outputs = self.model(**inputs)
return outputs.last_hidden_state[:, 0, :]
