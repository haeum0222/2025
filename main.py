import streamlit as st # Streamlit 라이브러리를 'st'라는 이름으로 불러옵니다. 이게 Streamlit의 시작이에요!

# 1. MBTI별 적합 직업 데이터를 정의합니다.
# 이 데이터는 파이썬 딕셔너리 형태로 저장되어 있어요.
mbti_job_recommendations = {
    "ISTJ": ["회계사", "공무원", "데이터 분석가", "경찰관", "군인"],
    "ISFJ": ["간호사", "사회복지사", "영양사", "보육교사", "상담사"],
    "INFJ": ["작가", "심리학자", "상담사", "교사", "성직자"],
    "INTJ": ["과학자", "프로그래머", "건축가", "전략 기획가", "대학교수"],
    "ISTP": ["기술자", "정비사", "소방관", "조종사", "요리사"],
    "ISFP": ["디자이너", "사진작가", "음악가", "예술가", "자유기고가"],
    "INFP": ["작가", "예술가", "심리학자", "상담사", "교사"],
    "INTP": ["과학자", "철학자", "프로그래머", "수학자", "연구원"],
    "ESTP": ["사업가", "영업직", "경찰관", "소방관", "스포츠 에이전트"],
    "ESFP": ["연예인", "이벤트 플래너", "유치원 교사", "서비스업", "관광 가이드"],
    "ENFP": ["마케터", "강사", "상담사", "광고 기획자", "크리에이터"],
    "ENTP": ["기업가", "변호사", "발명가", "컨설턴트", "마케터"],
    "ESTJ": ["관리자", "경영자", "변호사", "판사", "군 장교"],
    "ESFJ": ["교사", "간호사", "사회복지사", "상담사", "인사 담당자"],
    "ENFJ": ["교사", "상담사", "성직자", "리더십 트레이너", "인사 책임자"],
    "ENTJ": ["최고경영자(CEO)", "컨설턴트", "변호사", "정치인", "기업 전략가"]
}

# 2. Streamlit 앱의 타이틀과 설명 설정 (st.title, st.write는 Streamlit UI 요소입니다)
st.title("💡 MBTI 기반 직업 추천 사이트")
st.write("당신의 MBTI를 선택하고, 어떤 직업이 잘 맞을지 알아보세요!")

# 3. 사용자로부터 MBTI 유형 선택 받기 (st.selectbox는 Streamlit의 드롭다운 메뉴입니다)
mbti_types = sorted(list(mbti_job_recommendations.keys()))
selected_mbti = st.selectbox(
    "당신의 MBTI 유형은 무엇인가요?", # 사용자에게 보여줄 질문
    mbti_types, # 드롭다운에 표시할 선택지 목록
    index=0 # 앱 실행 시 기본으로 선택되어 있을 항목 (첫 번째 항목)
)

# 4. 선택된 MBTI에 따른 직업 추천 결과 표시 (st.subheader, st.markdown, st.info는 Streamlit UI 요소입니다)
if selected_mbti: # 사용자가 MBTI를 선택했다면
    st.subheader(f"✨ '{selected_mbti}' 유형에게 추천하는 직업") # 소제목 표시
    recommended_jobs = mbti_job_recommendations[selected_mbti]

    # 파이썬 리스트를 Streamlit의 마크다운 기능으로 예쁘게 목록화합니다.
    job_list_markdown = "\n".join([f"- {job}" for job in recommended_jobs])
    st.markdown(job_list_markdown) # 마크다운 형식으로 내용 표시

    st.markdown("---") # 구분선 표시
    st.info(f"**{selected_mbti}** 유형은 다음과 같은 특징을 가집니다:") # 정보 박스 표시

    # 여기에는 각 MBTI 유형별 특징 설명을 추가하는 파이썬 로직입니다.
    if selected_mbti == "ISTJ":
        st.write("책임감이 강하고 현실적이며 신뢰할 수 있습니다. 조직적이고 체계적인 것을 선호하며, 세부사항에 주의를 기울입니다.")
    elif selected_mbti == "ENFP":
        st.write("자유로운 영혼의 소유자로, 열정적이고 창의적이며 사회성이 좋습니다. 새로운 가능성을 탐색하고 사람들과 교류하는 것을 즐깁니다.")
    else:
        st.write("*(여기에 다른 MBTI 유형에 대한 상세 설명을 추가할 수 있어요!)*")

st.markdown("---") # 하단 구분선
st.write("본 직업 추천은 일반적인 경향을 바탕으로 하며, 개인의 흥미와 능력에 따라 더 다양한 직업이 적합할 수 있습니다.")
