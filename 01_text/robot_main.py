import streamlit as st
from robot import get_chat_response
from langchain.memory import ConversationBufferMemory
import os

st.title("AI教育聊天机器人")



with st.sidebar:
    openai_api_key = st.text_input("请输入OPENAI秘钥:", type="password")
    st.markdown("[获取 OpenAI API 密钥](https://platform.openai.com/account/api-keys)")
    # 添加返回首页的链接
    st.markdown("""
    <div style="position: fixed; top: 10px; right: 10px; z-index: 1000;margin-right: 1450px;">
        <a href="http://localhost:5000" target="_self" style="text-decoration: none; color: #4285f4; font-weight: bold;">
           返回首页
        </a>
    </div>
    """, unsafe_allow_html=True)

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai", "content": "你好，我是你的AI助手，有什么可以帮到你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()

if prompt:
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等......."):
        api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("请提供有效的 OpenAI API 密钥。")
        else:
            response = get_chat_response(prompt, st.session_state["memory"], api_key)
            msg = {"role": "ai", "content": response}
            st.session_state["messages"].append(msg)
            st.chat_message("ai").write(response)

# 添加一些使用说明
st.sidebar.title("使用说明")
st.sidebar.write("1. 在输入框中输入你的问题")
st.sidebar.write("2. 按回车键或点击发送按钮")
st.sidebar.write("3. 等待AI助手的回复")
st.sidebar.write("4. 你可以继续提问，进行多轮对话")
