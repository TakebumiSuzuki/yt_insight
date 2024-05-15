import streamlit as st
import logic as f


st.title("YouTube Insight")

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
    text = "\n".join(top_video_list)
    print(text)
    st.session_state.messages.append({"role": "AI", "content": text})
    with st.chat_message("AI"):
        st.markdown(text)


    answer = f.ask_llm(text)
    st.session_state.messages.append({"role": "AI", "content": answer})
    with st.chat_message("AI"):
        st.markdown(answer)












