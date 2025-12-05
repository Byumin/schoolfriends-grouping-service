import logging
import os
from logging.handlers import TimedRotatingFileHandler

# 1. 로그 저장 폴더 생성
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 2. 로거 생성
logger = logging.getLogger("api_server")
logger.setLevel(logging.DEBUG)

# 3. 포맷 (시간 | 레벨 | 파일명:줄번호 | 메시지)
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# 4. 콘솔 핸들러
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# 5. 파일 핸들러 (일별 로테이션, 7일 보관)
file_handler = TimedRotatingFileHandler(
    filename=f"{LOG_DIR}/server.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_logger():
    return logger