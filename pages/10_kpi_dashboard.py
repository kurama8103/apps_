import streamlit as st

st.title("KPIダッシュボード")
st.caption("主要KPIを表示するためのプレースホルダー")

col1, col2, col3 = st.columns(3)
col1.metric("Daily Active Users", "-", "")
col2.metric("Revenue", "-", "")
col3.metric("Conversion Rate", "-", "")

st.info("ここに実データ連携と可視化コンポーネントを追加してください。")
