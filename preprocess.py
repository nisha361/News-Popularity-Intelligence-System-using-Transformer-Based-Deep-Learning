import pandas as pd

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.dropna()

    df["text"] = df["Title"] + " [SEP] " + df["Description"]
    df = df[["text"]]

    df.to_csv(output_path, index=False)
    print("Preprocessing completed")

if __name__ == "__main__":
    preprocess_data(
        "data/raw_news.csv",
        "data/processed_news.csv"
    )
