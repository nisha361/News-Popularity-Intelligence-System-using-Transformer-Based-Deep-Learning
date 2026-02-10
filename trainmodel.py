import torch
import pandas as pd
from transformers import DistilBertTokenizer
from models.encoder import NewsEncoder
from models.popularity_head import PopularityHead
from proxy_signals.popularity_proxies import proxy_popularity

df = pd.read_csv("data/processed_news.csv")
df["proxy_score"] = df["text"].apply(proxy_popularity)

tokenizer = DistilBertTokenizer.from_pretrained(
    "distilbert-base-uncased"
)

encoder = NewsEncoder()
head = PopularityHead()

optimizer = torch.optim.Adam(
    list(encoder.parameters()) + list(head.parameters()),
    lr=2e-5
)

loss_fn = torch.nn.MSELoss()

for epoch in range(3):
    for _, row in df.iterrows():
        tokens = tokenizer(
            row["text"],
            truncation=True,
            padding=True,
            return_tensors="pt"
        )

        embedding = encoder(**tokens)
        prediction = head(embedding)

        target = torch.tensor(row["proxy_score"])
        loss = loss_fn(prediction.squeeze(), target)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    print(f"Epoch {epoch+1} finished")

torch.save(encoder.state_dict(), "models/saved/encoder.pt")
torch.save(head.state_dict(), "models/saved/head.pt")
