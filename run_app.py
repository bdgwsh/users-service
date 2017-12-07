from app import app
from config import DevelopmentConfig
import routes


if __name__ == '__main__':
    app.run(port=DevelopmentConfig.PORT)
