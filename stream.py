import streamlit as st

st.set_page_config(
    page_title="News Popularity Intelligence",
    layout="wide"
)

st.sidebar.title("🧠 News Popularity Intelligence")
st.sidebar.markdown("Transformer-Based Media AI System")

page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "News Intelligence", "Model Reasoning"]
)

if page == "Home":
    from pages import home
    home.show()

elif page == "News Intelligence":
    from pages import intelligence
    intelligence.show()

else:
    from pages import reasoning
    reasoning.show()
