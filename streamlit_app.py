import streamlit as st

st.title("🌸 今日のおすすめプラン")

st.write("気分・天気・予算からおすすめを提案します！")

mood = st.selectbox(
    "今日の気分は？",
    ["元気！", "疲れた", "リフレッシュしたい", "おしゃれしたい"]
)

weather = st.selectbox(
    "今日の天気は？",
    ["晴れ", "曇り", "雨"]
)

budget = st.slider("予算（円）", 1000, 10000, 3000)

st.divider()

if mood == "元気！":
    place = "遊園地"
    food = "焼肉"
elif mood == "疲れた":
    place = "温泉"
    food = "和食"
elif mood == "リフレッシュしたい":
    place = "水族館"
    food = "カフェ"
else:
    place = "ショッピング"
    food = "イタリアン"

if weather == "雨":
    place = "大型ショッピングモール"

st.success("あなたへのおすすめ")

st.write(f"📍 行き先：{place}")
st.write(f"🍴 食事：{food}")
st.write(f"💰 予算：約{budget}円")
