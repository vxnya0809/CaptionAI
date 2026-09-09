import streamlit as st 
from predict import predict_gesture
from deep_translator import GoogleTranslator
st.set_page_config(
    page_title="CaptionAI",
    page_icon="🗫",
    layout="centered"
)
st.title("🗫 CaptionAI")
st.subheader("Real-Time Sign Language Captioning")
language = st.selectbox(
    "Select Output Language",
    [
        "English",
        "Tamil",
        "Hindi",
        "Telugu",
        "Kannada",
        "Malayalam"
    ]
)
language_map={
    "English":"en",
    "Tamil":"ta",
    "Hindi":"hi",
    "Telugu":"te",
    "Kannada":"kn",
    "Malayalam":"ml"
}
if st.button("Start Camera"):
    caption = predict_gesture()
    if language != "English":
        caption = GoogleTranslator(
            source="auto",
            target=language_map[language]
        ).translate(caption)
    st.markdown("## Caption")
    st.success(caption)