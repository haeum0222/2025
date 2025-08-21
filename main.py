import streamlit as st
import time # 잠시 대기하는 효과를 주기 위해 import

# ✨ 앱의 전체적인 설정 (이모지, 파비콘, 레이아웃)
st.set_page_config(
    page_title="💖 꿈의 직업 탐색기 💖",
    page_icon="💡", # 브라우저 탭에 표시될 아이콘
    layout="centered" # 앱 레이아웃 설정
)

# 🎨 파란색과 초록색 계열의 화려한 테마를 생각하며 이모지 조합!
# 🌈 1. MBTI별 적합 직업 데이터를 정의합니다. (데이터는 이전과 동일)
mbti_job_recommendations = {
    "ISTJ": ["회계사 📊", "공무원 🏛️", "데이터 분석가 📈", "경찰관 👮‍♀️", "군인 🎖️", "은행원 🏦", "교사 (행정 중시) 🧑‍🏫"],
    "ISFJ": ["간호사 👩‍⚕️", "사회복지사 🤝", "영양사 🍎", "보육교사 🧑‍🍼", "상담사 🗣️", "행정직원 📋", "도서관 사서 📚"],
    "INFJ": ["작가 ✍️", "심리학자 🧠", "상담사 🗣️", "교사 🧑‍🏫", "성직자 🙏", "예술가 🎨", "NGO 활동가 🌍"],
    "INTJ": ["과학자 🔬", "프로그래머 💻", "건축가 🏗️", "전략 기획가 📈", "대학교수 🧑‍🎓", "컨설턴트 💼", "연구원 💡"],
    "ISTP": ["기술자 🛠️", "정비사 🔧", "소방관 🧑‍🚒", "조종사 ✈️", "요리사 👨‍🍳", "운동선수 🏃‍♂️", "IT 관리자 🖥️"],
    "ISFP": ["디자이너 🎨", "사진작가 📸", "음악가 🎶", "예술가 🎭", "자유기고가 📝", "패션 디자이너 👗", "수공예가 🤲"],
    "INFP": ["작가 ✍️", "예술가 🎭", "심리학자 🧠", "상담사 🗣️", "교사 🧑‍🏫", "사회복지사 🤝", "그래픽 디자이너 🎨"],
    "INTP": ["과학자 🧪", "철학자 🤔", "프로그래머 💻", "수학자 📐", "연구원 💡", "대학교수 🧑‍🎓", "시스템 분석가 📊"],
    "ESTP": ["사업가 💼", "영업직 🤝", "경찰관 👮‍♂️", "소방관 🧑‍🚒", "스포츠 에이전트 🏆", "응급구조사 🚑", "마케터 📢"],
    "ESFP": ["연예인 🌟", "이벤트 플래너 🎉", "유치원 교사 👩‍🏫", "서비스업 🏨", "관광 가이드 🗺️", "레크리에이션 강사 🤸‍♀️", "판매원 🛍️"],
    "ENFP": ["마케터 📢", "강사 🗣️", "상담사 💖", "광고 기획자 💡", "크리에이터 🎥", "언론인 🎤", "여행 작가 ✈️"],
    "ENTP": ["기업가 🚀", "변호사 ⚖️", "발명가 💡", "컨설턴트 📊", "마케터 📈", "벤처 투자가 💰", "엔지니어 (새로운 아이디어) ⚙️"],
    "ESTJ": ["관리자 🧑‍💼", "경영자 💼", "변호사 ⚖️", "판사 👩‍⚖️", "군 장교 🎖️", "회계사 📊", "프로젝트 매니저 📋"],
    "ESFJ": ["교사 🧑‍🏫", "간호사 👩‍⚕️", "사회복지사 💖", "상담사 🗣️", "인사 담당자 🤝", "병원 코디네이터 🏥", "이벤트 플래너 🎉"],
    "ENFJ": ["교사 🧑‍🏫", "상담사 🗣️", "성직자 🙏", "리더십 트레이너 🏆", "인사 책임자 🤝", "정치인 🏛️", "코치 📣"],
    "ENTJ": ["최고경영자(CEO) 👑", "컨설턴트 📊", "변호사 ⚖️", "정치인 🗣️", "기업 전략가 💡", "프로젝트 매니저 📋", "사업 개발자 📈"]
}

# 🚀 2. Streamlit 앱의 타이틀과 설명 (초화려 버전!)
st.title("💖 나의 잠재력을 깨울 운명의 직업은? 🌟")
st.write("---") # 깔끔한 구분선

st.markdown(
    """
    <p style='font-size: 20px; text-align: center; color: #1E90FF;'>
    ✨ 심리 검사 MBTI를 통해 당신의 성향에 꼭 맞는 환상의 직업을 찾아보세요! 🚀
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---") # 또 다른 구분선

# 💙💚 3. 사용자로부터 MBTI 유형 선택 받기 (파란색 계열 강조)
mbti_types = sorted(list(mbti_job_recommendations.keys()))

# 컬럼을 사용하여 레이아웃을 좀 더 재미있게 구성
col1, col2, col3 = st.columns([1, 2, 1])

with col2: # 가운데 컬럼에 셀렉트 박스 배치
    st.markdown(
        "<h3 style='color: #4682B4;'>🔍 당신의 MBTI 유형은 무엇인가요? 🌈</h3>",
        unsafe_allow_html=True
    )
    selected_mbti = st.selectbox(
        "⬇️ 여기에서 선택해주세요!", # 레이블은 작게
        mbti_types,
        index=0 # 초기 선택값 설정
    )

st.write("") # 간격 띄우기

# 🎉 4. 선택된 MBTI에 따른 직업 추천 결과 표시
if selected_mbti:
    # 🎈 선택 후 화려한 효과!
    st.balloons()
    st.success(f"🎉 와우! 당신은 바로 '{selected_mbti}' 유형이군요! 축하합니다! 🎉")
    st.info("💡 지금부터 당신의 잠재력을 폭발시킬 직업을 추천해 드릴게요! 💡")

    st.markdown("---") # 구분선
    st.markdown(
        f"<h2 style='color: #2E8B57; text-align: center;'>🎯 '{selected_mbti}' 유형을 위한 ✨BEST CAREER PICKS!✨</h2>",
        unsafe_allow_html=True
    )

    recommended_jobs = mbti_job_recommendations[selected_mbti]

    # 직업 목록을 훨씬 더 눈에 띄게 표시
    st.write("") # 간격
    for job in recommended_jobs:
        st.markdown(
            f"<h3 style='color: #36B078;'>✅ {job}</h3>",
            unsafe_allow_html=True
        )
        time.sleep(0.05) # 한 줄씩 천천히 나타나는 효과 (선택 사항)

    st.markdown("---") # 구분선

    # 🧠 MBTI 특징 설명을 Info 박스로 강조 (파란색 계열)
    st.markdown(
        f"<h3 style='color: #1F618D;'>🧠 당신의 MBTI 파헤치기! 🧬 깊이 있는 분석!</h3>",
        unsafe_allow_html=True
    )
    st.info(f"**🌟 '{selected_mbti}' 유형은 다음과 같은 놀라운 특징을 가집니다: 🌟**")

    # 각 MBTI 유형별 특징 설명을 여기에 추가 (이모지 듬뿍!)
    if selected_mbti == "ISTJ":
        st.markdown("📝 **정확성!** 책임감이 강하고 현실적이며 신뢰할 수 있어요! 🎯 조직적이고 체계적인 것을 선호하며, 세부사항에 주의를 기울이는 완벽주의자 타입! 🕵️‍♀️")
    elif selected_mbti == "ENFP":
        st.markdown("💖 **자유분방!** 자유로운 영혼의 소유자로, 열정적이고 창의적이며 사회성이 최고예요! 🎉 새로운 가능성을 탐색하고 사람들과 교류하는 것을 즐기는 핵인싸! ✨")
    elif selected_mbti == "INTJ":
        st.markdown("💡 **전략가!** 독립적이고 논리적이며, 복잡한 문제 해결에 탁월한 능력을 발휘해요! 🧐 비전을 제시하고 목표를 달성하는 데 몰두하는 강력한 리더 타입! 👑")
    elif selected_mbti == "ISFP":
        st.markdown("🎨 **예술혼!** 온화하고 예술적인 감각이 뛰어나며, 현재를 즐기는 유연한 타입! 🖼️ 아름다움과 조화를 추구하며 자신만의 스타일을 표현하는 섬세한 영혼! 🌸")
    else:
        st.markdown("🚀 더 많은 MBTI 유형별 특징 설명을 여기에 추가하면 앱이 더욱 풍성해질 거예요! ✨ 당신의 지식으로 이 공간을 가득 채워주세요! 💡")

st.markdown("---") # 마무리 구분선

st.markdown(
    """
    <p style='font-size: 18px; text-align: center; color: #6A5ACD;'>
    💡 본 직업 추천은 일반적인 MBTI 경향을 바탕으로 하며, 
    개인의 흥미와 능력에 따라 더 다양한 꿈의 직업이 적합할 수 있다는 점, 잊지 마세요! 💖
    </p>
    """,
    unsafe_allow_html=True
)

st.write(" ") # 마지막 간격
st.markdown("<p style='text-align: center;'>✨ 당신의 빛나는 미래를 응원합니다! ✨</p>", unsafe_allow_html=True)
        st.write("*(여기에 다른 MBTI 유형에 대한 상세 설명을 추가할 수 있어요!)*")

st.markdown("---") # 하단 구분선
st.write("본 직업 추천은 일반적인 경향을 바탕으로 하며, 개인의 흥미와 능력에 따라 더 다양한 직업이 적합할 수 있습니다.")
