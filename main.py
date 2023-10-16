
import streamlit as st
from functions import responder, find_txt_examples

def main():

    # Create a title for the chat interface
    st.title("Trainual Tracy RAG Tester")
    userresponse = st.text_area("Enter your query")

    if st.button('Submit'):
        examples = find_txt_examples(userresponse)
        response = responder(examples, userresponse)

        st.title('Response:')
        st.write(response)

        st.title('Doc Samples:')
        st.write(examples)

if __name__ == '__main__':
    main()