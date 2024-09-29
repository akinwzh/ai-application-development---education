import streamlit as st
import os
from video import generate_script
openai_api_key = os.getenv("OPENAI_API_KEY")
st.title("视频脚本生成器")
with st.sidebar:
    openai_api_key = st.text_input("请输入openai的api秘钥", type="password")
    st.markdown("[B站地址](http://localhost:8501/#5a87d6a2)")
subject=st.text_input("请输入视频主题")
vedio_length= st.number_input("请输入视频时长",min_value=0.1,step=0.1)
creativity=st.slider("请输入视频脚本的创造力，数字越大创造力水平越高",min_value=0.0,max_value=1.0,value=0.2,step=0.1)
submit = st.button("生成脚本")
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit and not vedio_length>= 0.1:
    st.info("视频时间过短")
    st.stop()
if submit:
    with st.spinner(("AI正在思考中，请稍等")):
       search_result,title,script = generate_script(subject,vedio_length,creativity,openai_api_key)
    st.success("视频脚步已生成")
    st.subheader("标题：")
    st.write(title)
    st.subheader("视频脚本")
    st.write(script)
    with st.expander("维基百科搜索结果："):
        st.info(search_result)


