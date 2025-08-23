import streamlit as st
# from PIL import Image # 이미지 관련 라이브러리 제거
# import os # 파일 시스템 접근 라이브러리 제거

# --- 0. Streamlit 앱 기본 설정 ---
# Noto Serif KR 폰트 (전통적 미감)와 Nanum Pen Script (손글씨 느낌)을 불러온다.
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;400;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

st.set_page_config(
    layout="wide", # 화면을 넓게 사용
    page_title="🎨 애니X명화: 스토리 연결고리 탐색 📚",
    initial_sidebar_state="expanded" # 사이드바를 시작부터 열어둠
)

# ✨ 앱 꾸미기 (CSS 스타일링) - 민하음의 '우와' 요소 듬뿍! ✨
st.markdown(
    """
    <style>
    /* 전체 페이지 배경색 및 폰트 */
    .stApp {
        background-color: #F8F8F8; /* 기본 배경: 아주 연한 백색 */
        /* 배경에 은은한 그라데이션과 한지 느낌 추가 (외부 이미지 파일 없음!) */
        background: linear-gradient(135deg, #F8F8F8 0%, #EEEEF2 50%, #F8F8F8 100%);
        font-family: 'Noto Serif KR', serif; /* Noto Serif KR 폰트 적용 */
        animation: fadeIn 1s ease-in-out; /* 전체 페이지 페이드인 애니메이션 */
    }
    
    /* 전체 페이드인 애니메이션 */
    @keyframes fadeIn {
      0% { opacity: 0; }
      100% { opacity: 1; }
    }

    /* 메인 콘텐츠 영역 (종이 같은 느낌, 전통 문양과 대비) */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        padding-left: 6rem;
        padding-right: 6rem;
        background-color: rgba(255, 255, 255, 0.95); /* 콘텐츠 영역은 거의 불투명하게 */
        border-radius: 15px; /* 둥근 모서리 */
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1); /* 그림자 효과 */
        animation: slideInFromTop 0.7s ease-out; /* 콘텐츠 영역 위에서 슬라이드인 애니메이션 */
    }

    /* 콘텐츠 영역 슬라이드인 애니메이션 */
    @keyframes slideInFromTop {
      0% { transform: translateY(-50px); opacity: 0; }
      100% { transform: translateY(0); opacity: 1; }
    }


    /* 사이드바 배경색 (비취색 계열) */
    .css-1d391kg { /* Streamlit의 사이드바 CSS 클래스 */
        background-color: #E6FFE6; /* 연한 비취색 계열 */
        border-right: 2px solid #88B04B; /* 비취색 선 */
    }

    /* 제목 스타일 (다홍색 계열로 강조, 전통적인 느낌) */
    h1 {
        color: #B22222; /* 벽돌색/다홍색 계열 */
        text-align: center;
        font-size: 3.5em; /* 글자 크기 키우기 */
        margin-bottom: 0.5em; /* 여백 추가 */
        letter-spacing: -2px; /* 글자 간격 살짝 줄이기 */
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2); /* 제목 그림자 */
        font-family: 'Nanum Pen Script', cursive; /* 손글씨 폰트 적용 */
        animation: titleEntry 1s ease-out forwards; /* 제목 등장 애니메이션 */
        opacity: 0; /* 초기 투명도 0 */
    }
    /* 제목 등장 애니메이션 (살짝 커지면서 나타남) */
    @keyframes titleEntry {
      0% { transform: scale(0.8); opacity: 0; }
      80% { transform: scale(1.05); opacity: 1; }
      100% { transform: scale(1); }
    }

    h2 {
        color: #3CB371; /* 미디엄 씨 그린 (비취색 계열) */
        font-size: 2.2em;
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        border-bottom: 2px solid #88B04B; /* 비취색 하단 선 */
        padding-bottom: 0.5em;
    }
    h3 {
        color: #A020F0; /* 보라색 계열 (전통 조화) */
        font-size: 1.8em;
    }

    /* 일반 텍스트 스타일 */
    .stMarkdown p {
        font-size: 1.1em;
        line-height: 1.8;
        color: #333; /* 먹색 계열 */
    }

    /* 버튼 스타일 (다홍색 계열, 유니크한 효과) */
    .stButton>button {
        background-color: #FF6347; /* 다홍색 계열 */
        color: white;
        border-radius: 10px;
        border: 2px solid #CD5C5C; /* 테두리 추가 */
        padding: 12px 25px;
        font-size: 1.2em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    .stButton>button:hover {
        background-color: #FF4500; /* 호버 시 색상 변경 */
        transform: translateY(-3px) scale(1.02);
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
        border-color: #B22222;
    }
    .stButton>button:active {
        transform: translateY(0) scale(0.98);
        box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    
    /* 알림창 (info, success, warning) 스타일 - 전통색감과 어울리게 */
    .stAlert {
        border-radius: 10px;
        font-size: 1.1em;
        border-left: 8px solid;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .st-bu { /* st.info 박스 */
        background-color: #EBF7EB; /* 연한 비취색 계열 배경 */
        border-color: #66CDAA; /* 비취색 선 */
        color: #2E8B57; /* 짙은 초록 글자 */
    }
    .st-cq { /* st.success 박스 */
        background-color: #EEFFEE;
        border-color: #28a745;
        color: #28a745;
    }
    .st-bV { /* st.warning 박스 */
        background-color: #FFF2E6; /* 연한 다홍 계열 배경 */
        border-color: #FF7F50; /* 다홍빛 주황 선 */
        color: #CD5C5C; /* 벽돌색 계열 글자 */
    }

    /* 명화 결과 카드 등장 애니메이션 */
    @keyframes slideInFromRight {
      0% { transform: translateX(100px); opacity: 0; }
      100% { transform: translateX(0); opacity: 1; }
    }
    .art-result-card { /* 각 명화 결과 div에 적용할 클래스 */
        animation: slideInFromRight 0.8s ease-out forwards;
        opacity: 0; /* 초기 투명도를 0으로 설정 */
        margin-bottom: 2em; /* 카드 사이 간격 */
        padding: 1.5em;
        border: 1px solid #DDD; /* 연한 테두리 */
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.9);
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True # HTML/CSS 코드 적용 허용
)

# --- 2. 데이터 매핑: 애니/만화 테마와 명화 ---
# 이 부분의 데이터는 이전과 동일하게 유지!
anime_art_mapping = {
    "복수극/다크 히어로": [
        {
            "title": "홀로페르네스의 목을 자르는 유디트",
            "artist": "아르테미시아 젠틸레스키",
            "story": "구약성서 '유디트기'에 나오는 이야기로, 홀로페르네스 장군에게 함락 위기에 처한 이스라엘 백성을 구하기 위해 유디트가 적장을 유혹하여 참수하는 극적인 장면을 그린 작품입니다. 절박한 상황 속에서 강인한 여성 영웅이 복수와 구원을 행하는 잔혹하면서도 영웅적인 서사를 담고 있습니다.",
            "connection": "힘없는 존재가 압도적인 강자에 맞서 복수하고 승리하는 서사는 많은 복수극 애니메이션/만화에서 찾아볼 수 있습니다. '정의 구현을 위한 폭력', '어둠 속에서 피어나는 강인함'과 같은 테마가 강렬하게 연결됩니다."
        },
        {
            "title": "다비드와 골리앗",
            "artist": "카라바조",
            "story": "어린 다윗이 거인 골리앗을 물리치고 그의 목을 베는 구약성서의 이야기입니다. 연약하고 보잘것없어 보이는 존재가 거대한 악을 상대로 정의를 실현하는 극적인 순간을 보여줍니다. 이후 다윗의 자비로운 시선이 인상적입니다.",
            "connection": "압도적인 적에 맞서 약자가 승리하고 복수를 이뤄내는 영웅 서사는 많은 다크 히어로물과 맞닿아 있습니다. 단순히 물리치는 것을 넘어 승리 후의 고뇌나 정의에 대한 재해석도 찾아볼 수 있습니다."
        }
    ],
    "소년만화/성장/모험": [
        {
            "title": "페르세우스와 안드로메다",
            "artist": "피에르-폴 루벤스",
            "story": "그리스 신화 속 영웅 페르세우스가 괴물 케토스로부터 공주 안드로메다를 구하는 장면입니다. 페르세우스는 메두사의 목을 벤 후 돌아오던 길에 이 장면을 목격하고, 자신의 용기와 힘으로 위험에 처한 존재를 구원합니다. 영웅의 모험과 성장, 그리고 구원이 담긴 이야기입니다.",
            "connection": "전형적인 소년만화에서 흔히 볼 수 있는 '성장하는 영웅이 고난과 시련을 극복하며 동료를 구하고 세상을 지킨다'는 서사와 맞닿아 있습니다. '용기', '희생', '새로운 세계로의 여정'과 같은 키워드가 명확히 드러납니다."
        },
        {
            "title": "헤라클레스와 히드라",
            "artist": "안토니오 델 폴라이올로",
            "story": "그리스 신화의 영웅 헤라클레스가 아홉 개의 머리를 가진 괴물 히드라를 물리치는 장면입니다. 아무리 잘라도 다시 생겨나는 히드라의 머리를 베는 난관을 극복하고, 끊임없이 도전하며 더욱 강해지는 영웅의 모습을 보여줍니다.",
            "connection": "주인공이 강력한 적과의 싸움에서 한계를 느끼고 좌절하지만, 동료의 도움이나 새로운 기술/능력을 얻어 더욱 성장하는 소년만화의 전개와 매우 흡사합니다. '끝없는 시련과 극복', '끈기', '점진적인 강해짐'이 주제입니다."
        }
    ],
    "로맨스/금지된 사랑": [
        {
            "title": "피그말리온과 갈라테아",
            "artist": "장-레옹 제롬",
            "story": "오비디우스의 '변신 이야기'에 나오는 일화로, 조각가 피그말리온이 자신이 조각한 완벽한 여인상 갈라테아를 너무나 사랑한 나머지, 비너스 여신이 조각상에 생명을 불어넣어 둘이 이루어지는 기적 같은 사랑 이야기입니다. 불가능해 보이는 사랑이 현실이 되는 순간을 담고 있습니다.",
            "connection": "애니메이션/만화에서 자주 등장하는 '넘을 수 없는 벽을 뛰어넘는 사랑', '이루어질 수 없어 보이는 관계가 결국 이어지는 기적', 또는 '피조물과 창조자 간의 특별한 유대'와 같은 로맨틱한 판타지 서사와 유사합니다."
        },
        {
            "title": "다나에",
            "artist": "구스타프 클림트",
            "story": "그리스 신화 속 다나에는 아버지가 감금했지만, 제우스가 황금비의 형태로 다가가 아들을 낳게 한 이야기입니다. 이 작품은 황금비가 그녀에게 쏟아지는 관능적이고 신비로운 순간을 포착했습니다. 금지되었거나 운명적인 만남, 신비롭고 관능적인 사랑을 암시합니다.",
            "connection": "운명적인 끌림, 비밀스럽거나 금지된 관계, 혹은 초월적인 존재와의 로맨스를 다루는 애니메이션/만화와 통합니다. 시각적으로 화려하면서도 숨겨진 이야기가 매력적입니다."
        }
    ],
    "일상/성장 드라마": [
        {
            "title": "만종",
            "artist": "장-프랑수아 밀레",
            "story": "황혼녘, 감자를 캐던 농부 부부가 멀리서 들려오는 종소리(만종)에 맞춰 경건하게 기도를 올리는 모습을 담은 작품입니다. 고단한 일상 속에서도 평화와 경건함을 잃지 않는 농민들의 소박하지만 숭고한 삶의 단면을 보여줍니다.",
            "connection": "화려한 사건보다 인물들의 내면, 소박한 일상, 잔잔한 감정의 변화에 초점을 맞추는 일상/성장 드라마 장르와 연결됩니다. '소박한 삶 속의 의미', '노동의 가치', '공동체의 유대' 등 평범함 속에서 비범함을 찾는 이야기에 해당합니다."
        },
        {
            "title": "강물",
            "artist": "안드레아스 아헨바흐",
            "story": "잔잔하게 흐르는 강물과 그 주변의 풍경, 뱃놀이를 하는 사람들의 평화로운 모습을 그렸습니다. 특별한 사건 없이 흐르는 자연의 모습과 인간의 일상이 조화롭게 어우러진 그림으로, 평온함과 사색을 느끼게 합니다.",
            "connection": "큰 갈등 없이 인물들의 잔잔한 일상과 내면의 성장을 다루는 '치유물' 또는 '슬라이스 오브 라이프' 장르 애니메이션과 어울립니다. 느린 호흡 속에서 삶의 작은 아름다움을 발견하는 스토리에 적합합니다."
        }
    ],
    "판타지/이세계물": [
        {
            "title": "최후의 심판",
            "artist": "미켈란젤로 (시스티나 성당 프레스코)",
            "story": "세상의 종말과 심판의 날, 죽은 자들이 부활하여 그리스도 앞에 서는 장엄하고 거대한 장면을 그렸습니다. 천국과 지옥, 선과 악의 대결, 혼돈 속의 질서, 그리고 인간의 운명이 결정되는 압도적인 스케일의 서사를 담고 있습니다.",
            "connection": "이세계물이나 판타지에서 흔히 볼 수 있는 '새로운 세상으로의 전이', '종말론적인 위기', '선과 악의 명확한 대립', '신적 존재와 마법적 능력' 같은 거대한 세계관과 깊은 연관성이 있습니다. 압도적인 스케일과 다양한 군상의 묘사가 특징입니다."
        },
        {
            "title": "천지창조 (아담의 창조)",
            "artist": "미켈란젤로 (시스티나 성당 프레스코 일부)",
            "story": "하나님이 아담에게 생명의 불꽃을 불어넣는 창조의 순간을 담았습니다. 신적 존재가 새로운 생명이나 세상을 창조하는 경이로운 순간을 표현하며, 태초의 시작과 기원에 대한 상징적인 의미를 지닙니다.",
            "connection": "이세계물의 시작점인 '새로운 세계의 탄생', 혹은 주인공이 '새로운 능력을 각성하거나 힘을 부여받는 순간'과 연결됩니다. 세계관의 기원이나 주인공의 초월적인 힘을 다루는 판타지 서사에 적합합니다."
        }
    ],
    "학원물/청춘/성장통": [
        {
            "title": "사춘기",
            "artist": "에드바르 뭉크",
            "story": "어둠 속에 앉아 불안하고 혼란스러운 표정으로 정면을 응시하는 소녀의 모습입니다. 미지의 존재처럼 드리워진 어두운 그림자는 내면의 불안과 성장에 대한 두려움, 그리고 홀로 마주해야 하는 청소년기의 고민을 상징적으로 보여줍니다.",
            "connection": "청소년기의 예민한 감정, 정체성 혼란, 우정의 미묘함, 미래에 대한 막연한 불안감 등 학원물과 청춘 드라마에서 다루는 보편적인 성장통의 주제와 일치합니다. 내면 묘사가 중요한 작품에 해당합니다."
        },
        {
            "title": "들판의 춤",
            "artist": "피에르 오귀스트 르누아르",
            "story": "푸른 들판에서 춤을 추는 두 남녀의 모습을 밝고 생동감 넘치는 터치로 그렸습니다. 햇살 가득한 배경과 인물들의 행복한 표정에서 젊음의 활기와 풋풋한 사랑, 혹은 순수한 기쁨이 느껴집니다. 특별한 사건보다는 순간의 아름다움을 포착했습니다.",
            "connection": "학창 시절의 풋풋한 로맨스, 친구들과의 즐거운 일상, 청춘의 빛나는 순간들을 다루는 학원 로맨스나 성장 애니메이션의 밝고 따뜻한 분위기와 연결됩니다. '찬란한 시절', '함께하는 즐거움'이 주제입니다."
        }
    ],
    "스릴러/미스터리/심리물": [
        {
            "title": "절규",
            "artist": "에드바르 뭉크",
            "story": "다리 위에서 귀를 막고 비명을 지르는 듯한 인물의 모습과 뒤틀린 배경은 극심한 불안과 공포, 고독, 그리고 현대인의 실존적 위기를 표현합니다. 내면의 소용돌이치는 감정이 외적인 형태로 폭발하는 순간을 시각화했습니다.",
            "connection": "정신적인 압박감, 극한의 공포, 해결되지 않는 미스터리로 인한 긴장감, 그리고 인물의 불안정한 심리를 파고드는 스릴러/심리물 애니메이션과 깊이 연결됩니다. 예측 불가능한 상황과 비극적인 결말을 암시하기도 합니다."
        },
        {
            "title": "사투르누스가 아들을 삼키다",
            "artist": "프란시스코 고야",
            "story": "그리스 신화의 크로노스(로마 신화의 사투르누스)가 자신의 왕좌를 빼앗길까 두려워 자식들을 잡아먹는 잔혹한 신화를 그렸습니다. 광기 어린 표정과 어두운 색감은 인간 내면의 광기와 공포, 파괴적인 본성을 여과 없이 보여줍니다.",
            "connection": "숨겨진 비밀, 비인간적인 행위, 통제 불가능한 광기, 그리고 잔혹하고 피폐한 세계관을 다루는 하드코어 스릴러나 다크 판타지 애니메이션과 유사합니다. 인물의 타락이나 집착에 대한 심리 묘사와도 연결됩니다."
        }
    ],
    "음악/예술 관련 (아이돌/음악 애니)": [
        {
            "title": "피아노 치는 소녀들",
            "artist": "피에르 오귀스트 르누아르",
            "story": "피아노를 함께 연주하며 즐거운 시간을 보내는 두 소녀의 모습을 포착했습니다. 밝고 따뜻한 색감과 부드러운 터치로 음악이 주는 즐거움, 그리고 예술 활동을 통해 교감하고 성장하는 모습을 담았습니다.",
            "connection": "아이돌이나 음악을 테마로 한 애니메이션에서 흔히 볼 수 있는 '함께 음악을 만들며 교감하고 성장하는 우정', '예술 활동을 통한 자아 실현', '재능을 꽃피우는 아름다운 순간'과 연결됩니다. 즐겁고 긍정적인 분위기가 특징입니다."
        },
        {
            "title": "발레 수업",
            "artist": "에드가 드가",
            "story": "발레 연습실의 일상적인 모습을 그린 작품으로, 무대 위의 화려함 뒤에 숨겨진 발레리나들의 꾸밈없는 연습 모습과 힘든 노력을 담고 있습니다. 예술가의 피땀 어린 노력과 열정, 그리고 보이지 않는 곳에서의 고군분투를 묘사합니다.",
            "connection": "겉으로 화려해 보이는 예술 세계의 이면에 숨겨진 끊임없는 연습과 노력, 경쟁, 그리고 꿈을 향한 열정을 다루는 애니메이션과 유사합니다. '성공을 위한 땀과 눈물', '예술가의 고뇌와 성장'을 보여줍니다."
        }
    ]
}

# --- 3. 사이드바 (꾸밈 + 사용 가이드) ---
with st.sidebar:
    st.markdown("<h2 style='color:#4B0082;'>✨ 내 취향 명화 찾기 도우미 ✨</h2>", unsafe_allow_html=True)
    st.write("안녕하세요, 민하음님! 이 앱은 애니메이션/만화 장르와 서양 명화 스토리를 연결해주는 매칭 시스템입니다. 🎨📚")

    st.markdown("---")
    st.subheader("💡 사용 가이드")
    st.write("1. 좋아하는 애니/만화의 **장르/테마**를 메인 화면에서 선택하세요.")
    st.write("2. '명화 찾기! 뿅!' 버튼을 누르면 관련된 명화를 볼 수 있어요. 🚀")
    st.write("")
    st.info("""
    **🚨 중요 안내 🚨**

    이 버전은 명화 이미지를 직접 표시하지 않고
    스토리 매칭 기능에 집중하도록 개선되었습니다.
    어떤 이미지 파일도 불러오지 않으므로
    더 이상 이미지 로딩 오류가 발생하지 않습니다!
    """)
    st.markdown("---")

# --- 4. 메인 앱 인터페이스 ---
st.markdown("<h1 style='text-align: center;'>🎨 애니메이션/만화 X 서양 명화: 스토리 연결고리 탐색 📚</h1>", unsafe_allow_html=True)

# ✨ GIF 이미지 추가 부분은 이제 없음! ✨

st.markdown("<p style='text-align: center; font-size: 1.2em; color: #555;'>좋아하는 애니메이션/만화의 장르나 테마를 선택해주세요!<br>당신의 취향과 놀랍도록 닮은 서양 미술 작품과 그 스토리를 찾아드릴게요. 💫</p>", unsafe_allow_html=True)

st.write("---")

# 사용자 이미지 업로드 섹션도 이제 없음!
# 예전의 col_upload, col_select 컬럼 분할 제거하고 전체 폭 사용
st.subheader("👇 핵심 '장르/테마'를 선택해주세요!")
selected_genre = st.selectbox(
    "어떤 테마의 작품을 좋아하시나요?",
    ["🤔 장르를 선택해주세요..."] + list(anime_art_mapping.keys()),
    index=0 # 기본 선택값을 첫 번째 옵션으로 지정
)
st.write("") # 간격 띄우기

if st.button("🚀 명화 찾기! 뿅!"):
    if selected_genre == "🤔 장르를 선택해주세요...":
        st.warning("앗! 장르를 먼저 선택해 주셔야 명화를 찾아드릴 수 있어요! 😥")
    else:
        st.markdown(f"<h2 style='color:#8A2BE2;'>✨ '{selected_genre}' 테마와 어울리는 명화들! ✨</h2>", unsafe_allow_html=True)
        st.write("당신의 취향은 생각보다 깊고 넓었군요! 두근두근... 어떤 명화와 연결될까요? 두둥탁! 🌟")

        if selected_genre in anime_art_mapping:
            art_recommendations = anime_art_mapping[selected_genre]

            # 매칭된 명화들을 하나씩 표시 (CSS 애니메이션 클래스 적용!)
            for i, art_info in enumerate(art_recommendations):
                st.markdown(f"""
                <div class="art-result-card" style="animation-delay: {i * 0.15}s;"> <!-- 순차적 등장 딜레이 -->
                    <h3 style='color:#A020F0;'>🖼️ {art_info['title']}</h3>
                    <p><strong>🎨 작가:</strong> {art_info['artist']}</p>
                    <p style='font-weight: bold; color: #6A5ACD;'>📖 작품 속 이야기:</p>
                    <p>{art_info["story"]}</p>
                    <p style='font-weight: bold; color: #BA55D3;'>🔗 애니/만화와의 연결고리:</p>
                    <div class="stAlert st-cq" style="margin-left: 0; margin-right: 0;">
                        <p>{art_info["connection"]}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.error("😭 아쉽지만, 해당 장르에 대한 명화 정보는 아직 없네요. 다른 장르를 선택해주세요!")

st.write("---")
st.markdown("<p style='text-align: center; font-size: 0.9em; color: #777;'>✨ 이 앱은 미술과 애니메이션/만화의 경계를 넘어선 스토리텔링의 유사성을 탐구합니다. ✨</p>", unsafe_allow_html=True)

# 푸터/개발자 노트 (깔끔하게 익스팬더로 숨겨두기)
with st.expander("📚 개발자 노트 / 생기부 활용 팁"):
    st.markdown("""
    이 프로젝트는 단순한 코딩을 넘어, **서양 미술사와 애니메이션 스토리텔링을 연결하는 융합적 사고**를 보여줍니다.
    생기부에 기록할 때 다음 포인트를 강조해 보세요:
    -   **융합적 사고:** 고전 예술과 현대 콘텐츠의 연결고리를 탐구하며 장르 간 경계를 허물었음.
    -   **큐레이션 능력:** 직접 명화와 애니메이션 테마를 매칭하며 스토리 분석 및 연결 능력을 증명.
    -   **인문학적 통찰:** 미술 작품에 내재된 깊이 있는 메시지를 이해하고, 이를 애니메이션에 적용할 방안 모색.
    """)
