
import streamlit as st
from functions import responder, find_txt_examples
from supabase_client import get_prompt
def main():

    # Create a title for the chat interface
    st.title("Trainual Tracy RAG Tester")
    st.write('Modify system prompt here. Remember, (Chunk Size * k) = Prompt Length')

    #input model parameters
    chunk_size = st.selectbox("Choose Chunk Size (default 400)",[200,400,600,800], index =1)
    chunk_overlap = st.selectbox("Choose Chunk Overlap (default 100)", [50,100,150,200], index = 1)
    k = st.selectbox("Select k (default = 6)", [2,4,6,8,10,12], index = 2)

    #user query
    userresponse = st.text_area("Enter your query")

    #retrieve system prompt
    bot_prompt = get_prompt('tracyRAG')

    if st.button('Submit'):
        #fetch examples from vector database
        examples = find_txt_examples(userresponse, chunk_size, chunk_overlap, k)

        #generate response
        response = responder(bot_prompt, examples, userresponse)

        #print for user
        st.title('Response:')
        st.write(response)

        st.title('Doc Samples:')
        st.write(examples)

if __name__ == '__main__':
    main()