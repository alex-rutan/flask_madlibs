from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def pick_story():
    """Creates form to pick a story from a list of story templates"""

    return render_template(
        "story-choice.html",
        stories=stories.values())


@app.route('/questions')
def create_form():
    """Creates form from given word types in the chosen story prompt""" 

    story_name = request.args["story_name"]
    story = stories[story_name]
    
    return render_template(
        "questions.html",
        story_name=story_name,
        title=story.title,
        prompts=story.prompts)


@app.route('/<story_name>/results')
def create_story(story_name):
    """Creates story from the inputs from the form submitted on the storyform page"""
    
    story = stories[story_name]
    story = story.generate(request.args)

    return render_template(
        "story.html",
        story=story)


