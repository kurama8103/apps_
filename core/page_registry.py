"""Streamlit ページ定義を管理するモジュール。"""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class PageDefinition:
    """ダッシュボード内で表示するページ情報。"""

    file_name: str
    title: str
    description: str
    status: str = "準備中"



def get_page_definitions() -> List[PageDefinition]:
    """トップページで表示するページ一覧を返す。"""

    return [
        PageDefinition(
            file_name="00_getting_started.py",
            title="はじめに",
            description="このアプリの使い方とページ追加ルールを確認します。",
            status="利用可能",
        ),
        PageDefinition(
            file_name="10_kpi_dashboard.py",
            title="KPIダッシュボード",
            description="主要指標をカード形式で表示するためのページです。",
        ),
        PageDefinition(
            file_name="20_data_explorer.py",
            title="データ探索",
            description="テーブル、フィルタ、チャートを配置するページです。",
        ),
        PageDefinition(
            file_name="30_settings.py",
            title="設定",
            description="環境変数や設定値を表示・編集するページです。",
        ),
    ]
