from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# RDS 엔드포인트(틀 : mysql+pymysql://USERNAME:PASSWORD@ENDPOINT:3306/DBNAME)
DATABASE_URL = "mysql+pymysql://sf_admin:Ehfosf2025$@sf-db1.cl8w602g8n4s.ap-northeast-2.rds.amazonaws.com:3306/SCHOOL_FRIEND"
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()