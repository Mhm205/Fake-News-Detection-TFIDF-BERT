import streamlit as st

st.set_page_config(page_title="Fake News Detection")

st.title("Hybrid Fake News Detection")

st.write(
    "Fake News Detection using TF-IDF, BERT and Random Forest"
)

news_text = st.text_area(
    "Enter News Text"
)

if st.button("Analyze"):

    if len(news_text.strip()) == 0:
        st.warning("Please enter a news article.")
    else:
        st.success("Text received successfully.")

        st.write("Input Text:")
        st.write(news_text)

        st.info(
            "Model deployment version."
        )
