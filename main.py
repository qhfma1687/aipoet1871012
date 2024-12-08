import streamlit as st
from langchain_openai import ChatOpenAI

# OpenAI Chat 모델 초기화
chat_model = ChatOpenAI(api_key=st.secrets["openai"]["api_key"])

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    if not subject:
        st.error("주제를 입력해 주세요.")
    else:
        with st.spinner("시 작성중 ..."):
            try:
                result = chat_model.invoke(subject + "에 대한 시를 써줘")
                st.write(result.content)
            except Exception as e:
                st.error(f"오류 발생: {e}")
