import streamlit as st
from inference.predict import predict_popularity, explain_prediction

def show():
    st.title("📰 News Intelligence")

    title = st.text_input("Enter News Title")
    desc = st.text_area("Enter News Description")

    if st.button("Analyze Popularity"):
        if title.strip() == "" and desc.strip() == "":
            st.warning("Please enter title or description.")
            return

        score = predict_popularity(title, desc)
        explanation = explain_prediction(title, desc)

        st.metric("📊 Predicted Popularity Score", f"{score:.2f} / 10")

        st.markdown("### 🔎 Why this score?")
        st.write(explanation)
