import streamlit as st
import PyPDF2
import preprocessor
from nltk.corpus import stopwords


st.sidebar.title("PDF Summarization")

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf"])


if uploaded_file is not None:

    reader = PyPDF2.PdfReader(uploaded_file)
    st.write("File successfully uploaded!")
    page = len(reader.pages)
    pdf_text = []
    for i in range(page) :
        pdf_text.append(reader.pages[i].extract_text())
        
# st.write(pdf_text)
text = " ".join(pdf_text)

cleaned_text = preprocessor.remove_html_tags(text)
cleaned_text = preprocessor.remove_url(cleaned_text)
text = cleaned_text.lower()


stopwords = stopwords.words()

summary = preprocessor.adjust_based_on_length(text, stopwords, page)
key_words = preprocessor.top_keywords(pdf_text)


st.write(summary)
st.write(key_words)

# wordcloud = preprocessor.plot_cloud(text, stopwords)
# plot = plt.figure(figsize = (40,30))
# plt.imshow(wordcloud)          # Display image
# plt.axis('off') 
# # st.pyplot(plot)














