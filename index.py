# -*- coding: utf-8 -*-

import streamlit as st

from core.page_registry import get_page_definitions

st.set_page_config(page_title="Dashboard Index", page_icon="📊", layout="wide")

st.title("📊 Dashboard Index")
st.caption("Streamlitマルチページ構成のトップページ")

st.markdown(
    """
このアプリは、`pages/` 配下に機能単位でページを追加できる構成です。

- **トップページ（この画面）**: 全体インデックス
- **サブページ**: 1ページ1機能で拡張
- **共通ロジック**: `core/` に配置
"""
)

st.subheader("ページ一覧")
page_definitions = get_page_definitions()
for page in page_definitions:
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {page.title}")
            st.write(page.description)
            st.code(f"pages/{page.file_name}", language="bash")
        with col2:
            st.metric("Status", page.status)

st.info("新しい機能ページを追加する場合は `pages/` に新しい `.py` ファイルを作成してください。")
