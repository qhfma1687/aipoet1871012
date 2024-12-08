# 필요한 라이브러리 설치
# pip install python-dotenv
# pip install langchain-openai
# pip install streamlit

from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import streamlit as st

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 로드 및 확인
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API 키가 설정되지 않았습니다.")
else:
    # OpenAI Chat 모델 초기화
    chat_model = ChatOpenAI(api_key=api_key)

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
