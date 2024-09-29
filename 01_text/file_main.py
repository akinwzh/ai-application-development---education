import streamlit as st
from file import qa_agent
from langchain.memory import ConversationBufferMemory
import os
st.title("AI智能PDF问答工具")
with st.sidebar:
        # 添加返回首页的链接
    st.markdown("""
    <div style="position: fixed; top: 10px; right: 10px; z-index: 1000;margin-right: 1450px;">
        <a href="http://localhost:5000" target="_self" style="text-decoration: none; color: #4285f4; font-weight: bold;">
           返回首页
        </a>
    </div>
    """, unsafe_allow_html=True)
    openai_api_key = st.text_input("请输入OPENAI秘钥:",type="password")
    st.markdown("[video页面](https://www.bilibili.com/)")


if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
uploaded_file = st.file_uploader("上传你的PDF文件",type="pdf")
question= st.text_input("对PDF的内容进行提问",disabled=not uploaded_file)
if uploaded_file and question:
    with st.spinner("AI正在思考中，请稍等......"):
        response = qa_agent(os.getenv("OPENAI_API_KEY"),st.session_state["memory"],uploaded_file,question)
    st.write("### 答案")
    st.write(response["answer"])
    st.session_state["chat_history"]=response['chat_history']
if "chat_history" in st.session_state:
    with st.expander("历史消息"):
        for i in range(0,len(st.session_state["chat_history"]),2):
            human_message = st.session_state["chat_history"][i]
            ai_message = st.session_state["chat_history"][i+1]
            st.write(human_message.content)
            st.write(ai_message.content)
            if i < len(st.session_state["chat_history"]) - 2:
                st.divider()