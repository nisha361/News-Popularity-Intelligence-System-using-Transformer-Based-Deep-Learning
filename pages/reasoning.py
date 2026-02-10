import streamlit as st

def show():
    st.title("🔍 Model Reasoning")

    st.markdown("""
    ## 🧠 How the Model Infers Popularity

    The system does **not use historical popularity labels**.
    Instead, it relies on **weak supervision signals**:

    - 🔥 Emotional intensity  
    - ⚡ Urgency or breaking-news language  
    - 🧩 Lexical diversity  
    - 📖 Narrative clarity  
    - ✍️ Linguistic structure  

    These signals are combined with **Transformer embeddings**
    to estimate how attention-worthy an article is.
    """)

    st.markdown("## 📊 Example Comparison")

    st.info("""
    **Article A:** "Breaking: Massive Storm Approaches Coast"  
    → High urgency + strong emotion → **Higher popularity score**

    **Article B:** "City Council Reviews Annual Budget Proposal"  
    → Neutral tone + low urgency → **Lower popularity score**
    """)
