import constants as K
import streamlit as st
import logic as f
import time
import random

st.set_page_config(
    page_title = "SmartTube Planner",
)

st.markdown(K.CSS, unsafe_allow_html=True)

st.title("SmartTube Planner")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if url := st.chat_input("Enter url"):

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": url})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(url)


    top_video_list = f.ask_youtube(url)
    list = []
    for elem in top_video_list:
        elem = "1. " + elem
        list.append(elem)
    text = "  \n".join(list)
    text2 = "### **The most viewed video in the past year**  \n" + text

    st.session_state.messages.append({"role": "AI", "content": text})
    with st.chat_message("AI"):
        st.markdown(text2)

    full_response = ""
    answer = f.ask_llm(text)

    with st.chat_message("AI"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")
            try:
                for chunk in answer:
                    word_count = 0
                    random_int = random.randint(5,10)
                    for word in chunk.text:
                        full_response+=word
                        word_count+=1
                        if word_count == random_int:
                            time.sleep(0.05)
                            message_placeholder.markdown(full_response + "_")
                            word_count = 0
                            random_int = random.randint(5,10)
                message_placeholder.markdown(full_response)

            except Exception as e:
                st.exception(e)
            st.session_state.messages.append({"role": "AI", "content": answer})













