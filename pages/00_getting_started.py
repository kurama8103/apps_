import streamlit as st

st.title("はじめに")
st.write("このページでは、ダッシュボードの基本構成とページ追加手順を説明します。")

st.markdown(
    """
## ページ追加の流れ
1. `pages/` 配下に `NN_feature_name.py` 形式でファイルを作成
2. UIコードをページファイルに実装
3. 共通ロジックは `core/` に切り出して再利用
4. 必要に応じて `core/page_registry.py` に説明を追加
"""
)

st.success("このページをベースに、機能ごとのページを増やしてください。")
