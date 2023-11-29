
from stories import Story
from flask import Flask, request, render_template

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route('/')
def display_home():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story')
def show_story():
    madlib = story.generate(request.args)

    return render_template('story.html',madlib=madlib)