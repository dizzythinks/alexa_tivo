__author__    = "Phil Hendren aka dizzythinks"
__credits__   = ["Phil Hendren"]
__version__   = "1.0"

from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)