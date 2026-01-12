import streamlit as st
from deep_translator import GoogleTranslator

# Language dictionary (MUST be before usage)
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

# App title
st.title("🌍 AI Language Translation Tool")
st.write("Translate text between different languages using AI")

# Text input
text = st.text_area("Enter text to translate")

# Language selection
language_names = list(LANGUAGES.keys())

source_lang_name = st.selectbox("Source Language", language_names)
target_lang_name = st.selectbox("Target Language", language_names, index=1)

source_lang = LANGUAGES[source_lang_name]
target_lang = LANGUAGES[target_lang_name]

# Translate button
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter text to translate")
    else:
        translated_text = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        st.success("Translation Successful")
        st.text_area("Translated Text", translated_text, height=150)
