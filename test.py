import streamlit as st
from PIL import Image
import os # 이미지 경로를 위해

# --- 1. 앱 기본 설정 (제목, 설명 등) ---
st.set_page_config(layout="wide", page_title="애니X명화 스토리 매칭 시스템")

st.title("🎨 애니메이션/만화 X 서양 명화: 스토리 연결고리 탐색 📚")
st.markdown("""
좋아하는 애니메이션/만화의 장르나 테마를 선택해주세요!
당신의 취향과 놀랍도록 닮은 서양 미술 작품과 그 스토리를 알려드릴게요.
""")

# --- 2. 명화 이미지 폴더 설정 (예시) ---
# 실제 이미지를 'art_images' 폴더 안에 넣어두세요.
# 예를 들어, art_images/judith.jpg, art_images/perseus.jpg
ART_IMAGES_DIR = "art_images"
# 만약 'art_images' 폴더가 없다면 생성 (Streamlit Cloud에서는 직접 업로드해야 할 수 있음)
if not os.path.exists(ART_IMAGES_DIR):
    os.makedirs(ART_IMAGES_DIR)

# --- 3. 핵심! 애니/만화 테마와 명화 데이터베이스 (네가 직접 채워 넣을 부분!) ---
# 이 딕셔너리가 너의 핵심 '큐레이션 데이터'가 될 거야!
# 여기에 '애니/만화 테마'별로 '매칭되는 명화 정보'를 상세하게 넣어두면 돼.
# 'image_path': art_images 폴더 안의 이미지 파일명
# 'story': 명화가 담고 있는 핵심 이야기
# 'connection': 왜 이 명화가 해당 애니/만화 테마와 연결되는지 설명
anime_art_mapping = {
    "복수극/다크 히어로": [
        {
            "title": "홀로페르네스의 목을 자르는 유디트",
            "artist": "아르테미시아 젠틸레스키",
            "image_path": os.path.join(ART_IMAGES_DIR, "judith.jpg"),
            "story": "구약성서 '유디트기'에 나오는 이야기로, 홀로페르네스 장군에게 함락 위기에 처한 이스라엘 백성을 구하기 위해 유디트가 적장을 유혹하여 참수하는 극적인 장면을 그린 작품입니다. 절박한 상황 속에서 강인한 여성 영웅이 복수와 구원을 행하는 잔혹하면서도 영웅적인 서사를 담고 있습니다.",
            "connection": "힘없는 존재가 압도적인 강자에 맞서 복수하고 승리하는 서사는 많은 복수극 애니메이션/만화에서 찾아볼 수 있습니다. '정의 구현을 위한 폭력', '어둠 속에서 피어나는 강인함'과 같은 테마가 강렬하게 연결됩니다."
        },
        # 다른 복수극 관련 명화 추가
    ],
    "소년만화/성장/모험": [
        {
            "title": "페르세우스와 안드로메다",
            "artist": "피에르-폴 루벤스",
            "image_path": os.path.join(ART_IMAGES_DIR, "perseus.jpg"),
            "story": "그리스 신화 속 영웅 페르세우스가 괴물 케토스로부터 공주 안드로메다를 구하는 장면입니다. 페르세우스는 메두사의 목을 벤 후 돌아오던 길에 이 장면을 목격하고, 자신의 용기와 힘으로 위험에 처한 존재를 구원합니다. 영웅의 모험과 성장, 그리고 구원이 담긴 이야기입니다.",
            "connection": "전형적인 소년만화에서 흔히 볼 수 있는 '성장하는 영웅이 고난과 시련을 극복하며 동료를 구하고 세상을 지킨다'는 서사와 맞닿아 있습니다. '용기', '희생', '새로운 세계로의 여정'과 같은 키워드가 명확히 드러납니다."
        },
        # 다른 소년만화/성장/모험 관련 명화 추가
    ],
    "로맨스/금지된 사랑": [
        {
            "title": "피그말리온과 갈라테아",
            "artist": "장-레옹 제롬",
            "image_path": os.path.join(ART_IMAGES_DIR, "pygmalion.jpg"),
            "story": "오비디우스의 '변신 이야기'에 나오는 일화로, 조각가 피그말리온이 자신이 조각한 완벽한 여인상 갈라테아를 너무나 사랑한 나머지, 비너스 여신이 조각상에 생명을 불어넣어 둘이 이루어지는 기적 같은 사랑 이야기입니다. 불가능해 보이는 사랑이 현실이 되는 순간을 담고 있습니다.",
            "connection": "애니메이션/만화에서 자주 등장하는 '넘을 수 없는 벽을 뛰어넘는 사랑', '이루어질 수 없어 보이는 관계가 결국 이어지는 기적', 또는 '피조물과 창조자 간의 특별한 유대'와 같은 로맨틱한 판타지 서사와 유사합니다."
        },
        # 다른 로맨스/금지된 사랑 관련 명화 추가
    ],
    "일상/성장 드라마": [
        {
            "title": "만종",
            "artist": "장-프랑수아 밀레",
            "image_path": os.path.join(ART_IMAGES_DIR, "angelus.jpg"),
            "story": "황혼녘, 감자를 캐던 농부 부부가 멀리서 들려오는 종소리(만종)에 맞춰 경건하게 기도를 올리는 모습을 담은 작품입니다. 고단한 일상 속에서도 평화와 경건함을 잃지 않는 농민들의 소박하지만 숭고한 삶의 단면을 보여줍니다.",
            "connection": "화려한 사건보다 인물들의 내면, 소박한 일상, 잔잔한 감정의 변화에 초점을 맞추는 일상/성장 드라마 장르와 연결됩니다. '소박한 삶 속의 의미', '노동의 가치', '공동체의 유대' 등 평범함 속에서 비범함을 찾는 이야기에 해당합니다."
        },
        # 다른 일상/성장 드라마 관련 명화 추가
    ]
    # 여기에 더 많은 장르/테마와 매칭되는 명화를 추가하세요!
    # 예: "이세계물/판타지", "메카물/SF", "학원물/청춘", "공포/미스터리" 등
}

# --- 4. 사용자 입력 섹션 ---

# 작품 사진 업로드 (선택 사항 - 사진 분석은 안 되고, 사용자 흥미 유발 및 컨텍스트 제공용)
uploaded_file = st.file_uploader("좋아하는 애니메이션/만화의 한 장면을 업로드해보세요 (선택 사항)", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="업로드한 작품", use_column_width=True)
    st.write("멋진 작품이네요! 이제 아래에서 장르를 선택해 주세요.")

# 장르 선택 (드롭다운)
selected_genre = st.selectbox(
    "1. 당신이 좋아하는 애니메이션/만화의 핵심 '장르/테마'를 선택해주세요:",
    ["선택하세요"] + list(anime_art_mapping.keys())
)

# 검색 버튼
if st.button("🖼️ 명화 찾기!"):
    if selected_genre == "선택하세요":
        st.warning("장르를 선택해주세요!")
    else:
        st.subheader(f"✨ '{selected_genre}' 테마와 어울리는 명화들을 찾았어요! ✨")

        if selected_genre in anime_art_mapping:
            art_recommendations = anime_art_mapping[selected_genre]

            # 여러 개의 매칭 결과를 보여줄 수 있도록 반복
            for i, art_info in enumerate(art_recommendations):
                st.markdown("---")
                col1, col2 = st.columns([1, 2]) # 이미지와 설명을 나란히 배치

                with col1:
                    try:
                        # 이미지 파일을 불러와 표시
                        img_path = art_info["image_path"]
                        if os.path.exists(img_path):
                            image = Image.open(img_path)
                            st.image(image, caption=f"'{art_info['title']}'", use_column_width=True)
                        else:
                            st.error(f"이미지 파일을 찾을 수 없습니다: {img_path}")
                            st.write("예시 이미지를 `art_images` 폴더에 넣어주세요.")
                    except Exception as e:
                        st.error(f"이미지를 로드하는 중 오류가 발생했습니다: {e}")

                with col2:
                    st.markdown(f"### <span style='color:#FF6347;'>{art_info['title']}</span>", unsafe_allow_html=True) # 제목 강조
                    st.write(f"**작가:** {art_info['artist']}")
                    st.markdown(f"#### 작품 속 이야기:")
                    st.write(art_info["story"])
                    st.markdown(f"#### 🔎 애니메이션/만화와의 연결고리:")
                    st.info(art_info["connection"]) # info 박스로 강조

        else:
            st.error("아직 해당 장르에 대한 명화 정보가 없네요. 다른 장르를 선택해주세요.")

st.markdown("---")
st.markdown("### 👩‍💻 개발자 노트")
st.write("""
이 프로그램은 미술과 애니메이션/만화의 경계를 넘어선 스토리텔링의 유사성을 탐구합니다.
사용자의 취향을 반영한 맞춤형 예술 경험을 제공하며,
고전 예술의 현대적 재해석 가능성을 보여줍니다.
(생기부에 이 부분에 너가 뭘 배우고 느꼈는지 더 풍성하게 쓰면 된다!)
""")
