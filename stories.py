"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, name, title, words, text):
        """Create story with words and template text."""
        self.name = name
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

silly_story = Story(
    "silly",
    "A Silly Story",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in a long-ago {place}, there lived an exceptionally
       {adjective} {noun}. It loved to {verb} with {plural_noun}."""
)

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

excited_story = Story(
    "excited",
    "An Excited Story",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

weird_story = Story(
    "weird",
    "A Weird Story",
    ["noun", "verb", "place", "adjective", "plural_noun", "past_tense_verb"],
    """It was deathly quiet in the courtyard. The {noun} struck midnight in {place}. {plural_noun} poured out of the doors of their homes and {past_tense_verb} into their {adjective} automobiles. Their cars could {verb} very quickly. Soon it was quiet once again."""
)


stories = {story.name: story for story in [silly_story, excited_story, weird_story]}