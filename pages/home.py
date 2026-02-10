import streamlit as st

def show():
    st.title("📰 News Popularity Intelligence System")

    st.markdown("""
    ## 📌 Problem
    News platforms must decide which articles to promote **before**
    real popularity metrics (clicks, shares) are available.

    ## 💡 Our AI Solution
    We use a **Transformer-based deep learning system** that:
    - Understands article meaning
    - Detects urgency and emotion
    - Measures linguistic richness
    - Estimates **attention potential**

    Popularity is treated as a **latent variable**, inferred directly from text.
    """)

    st.markdown("## ⚙️ System Architecture")

    st.markdown("""
    **Title + Description → Transformer Encoder → Semantic Embedding →  
    Weak Supervision Signals → Popularity Scoring Model → Final Rank**
    """)
