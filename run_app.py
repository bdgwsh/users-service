from app import app
from config import PORT
import routes


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
