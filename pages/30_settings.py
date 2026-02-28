import configparser
from pathlib import Path

import streamlit as st

st.title("設定")
st.caption("config.ini の内容を確認するページ")

config_path = Path("config.ini")

if not config_path.exists():
    st.error("config.ini が見つかりません。")
else:
    parser = configparser.ConfigParser()
    parser.read(config_path, encoding="utf-8")

    sections = parser.sections()
    if not sections:
        st.warning("config.ini にセクションが定義されていません。")

    for section in sections:
        st.subheader(section)
        st.json({key: value for key, value in parser.items(section)})
