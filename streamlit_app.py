import streamlit as st

st.title("🌸 今日のおすすめプラン")

st.write("気分・天気・予算からおすすめを提案します！")

# 気分を選択
mood = st.selectbox(
    "今日の気分は？",
    ["元気！", "疲れた", "リフレッシュしたい", "おしゃれしたい"]
)

# 天気を選択
weather = st.selectbox(
    "今日の天気は？",
    ["晴れ", "曇り", "雨"]
)

# 予算
budget = st.slider(
    "予算（円）",
    1000,
    10000,
    3000
)

st.divider()

# 気分による基本推薦
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

# 雨の日は屋内施設を優先
if weather == "雨":
    place = "大型ショッピングモール"

# 予算によって食事を変更
if budget <= 2000:
    food = "ファストフード"

elif budget <= 5000:
    food = "カフェ"

else:
    food = "高級レストラン"

# 「おしゃれしたい」の場合は予算も考慮
if mood == "おしゃれしたい":
    if budget >= 7000:
        place = "高級ホテルラウンジ"
        food = "フレンチ"

    elif budget >= 3000:
        place = "ショッピング"
        food = "イタリアン"

    else:
        place = "雑貨屋巡り"
        food = "カフェ"

st.success("あなたへのおすすめ")

st.write(f"📍 行き先：{place}")
st.write(f"🍽 食事：{food}")
st.write(f"💰 予算：約{budget}円")
