from flask import Flask, request, render_template
from solve import SoundCloud
from arrays import DynamicArray

app = Flask("__name__")

@app.route("/")
def main():
	return render_template("lo-fi.html")

@app.route("/", methods=['POST'])
def hello():
	try:
		text = request.form['mood']
		sound = SoundCloud(text)
		if not text == '':
			final = sound.get_widgets()
			return render_template('lo-fi_music.html', final = final, valid = len(final))
		else:
			return render_template('lo-fi_music.html', valid = 0)
	except Exception as error:
		final = DynamicArray()
		return render_template('lo-fi_music.html', final=final)

if __name__ == "__main__":
	app.run()