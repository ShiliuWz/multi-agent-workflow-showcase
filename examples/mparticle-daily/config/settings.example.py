"""Public-safe example settings for the mparticle daily workflow."""

from pathlib import Path

BASE_URL = "https://your-mparticle-host.example.com"
API_BASE = f"{BASE_URL}/api"
KB_BASE = f"{BASE_URL}/kb"

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
DB_PATH = DATA_DIR / "mparticle_daily.example.db"

TIMEZONE = "Asia/Shanghai"
MAX_ARTICLES_PER_REPORT = 100
SUMMARY_MAX_TOKENS = 300
REQUEST_TIMEOUT = 30
RETRY_COUNT = 3
RETRY_DELAY = 2
CONCURRENT_FETCH = 5

FEISHU_TARGET = "user_or_chat_id_here"
FEISHU_WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/replace_me"
