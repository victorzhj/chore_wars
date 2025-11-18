import os, pymysql, dotenv

dotenv.load_dotenv()

class Config:
    def __init__(self):
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")

    def create_connection(self):
        return pymysql.connect(
            host=self.DB_HOST,
            port=int(self.DB_PORT),
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            database=self.DB_NAME,
        )
