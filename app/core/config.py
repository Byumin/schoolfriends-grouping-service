from pydantic_settings import BaseSettings
# BaseSettings 동작 방식:
# config 클래스가 있는지 확인
# config 안에 env_file 같은 속성이 있는지 확인
# 있으면 .env 파일을 찾아서 읽는다 -> main.py가 있는 폴더 기준(cwd) -> 따로 경로지정 필요없음
# 읽은 값을 Settings 필드에 자동 매핑한다 -> key=value 형식으로 매핑함

class Settings(BaseSettings):
    app_host: str = "127.0.0.1"
    app_port: int = 8090

    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    @property
    def db_url(self) -> str:
        # MySQL 접속 URL 형식: 
        # mysql+pymysql://아이디:비번@주소:포트/DB명
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"

# 앞서 만든 settings 객체를 실행하면, 위와 같은 방식(BaseSettings)으로 동작함
settings = Settings()