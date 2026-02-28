import pandas as pd
import streamlit as st

st.title("データ探索")
st.caption("フィルタ・テーブル表示ページのプレースホルダー")

sample_df = pd.DataFrame(
    {
        "category": ["A", "B", "C"],
        "value": [10, 20, 30],
    }
)

selected = st.multiselect("category", options=sample_df["category"].tolist())
if selected:
    sample_df = sample_df[sample_df["category"].isin(selected)]

st.dataframe(sample_df, use_container_width=True)
