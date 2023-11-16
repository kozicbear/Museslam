from flask import Flask
from poem_generator import PoemGenerator

app = Flask(__name__)

generator = PoemGenerator()

@app.route("/poem")
def poem():
        return {"poem": generator.get_poem() }

if __name__ == '__main__':
	app.run(debug=True)