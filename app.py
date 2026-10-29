from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

GENRE_OPENINGS = {
    "Fantasy": "Beyond the edge of the known map, where old magic still breathed,",
    "Science Fiction": "In an age when humanity had learned to listen to the stars,",
    "Mystery": "The first clue arrived before sunrise, tucked where nobody thought to look,",
    "Romance": "Some meetings feel ordinary until the moment you remember them forever,",
    "Adventure": "The journey began with a strange map, a borrowed compass, and one impossible promise,",
    "Horror": "The house had been empty for twenty years, yet every night a light appeared upstairs,",
    "Literary": "Years later, the smallest detail would be the one that stayed,",
}
GENRE_TURNS = {
    "Fantasy": "A symbol shimmered across the ancient stone, revealing that the legend was not a legend at all.",
    "Science Fiction": "A signal answered from a place that, according to every chart, did not exist.",
    "Mystery": "The evidence pointed in three directions, and every witness had a reason to lie.",
    "Romance": "A familiar voice interrupted the silence, carrying a truth neither person had been ready to say.",
    "Adventure": "At the next crossroads, the safe route vanished—and the real path revealed itself.",
    "Horror": "Then the locked door opened from the other side.",
    "Literary": "For the first time, the past seemed less like a memory and more like a question.",
}
GENRE_ENDINGS = {
    "Fantasy": "By dawn, the kingdom would have a new story to tell—and a new name to remember.",
    "Science Fiction": "The future was no longer a destination. It was a choice they had to make together.",
    "Mystery": "The final answer was simple; finding the courage to face it was not.",
    "Romance": "Neither knew what tomorrow would bring, but for once, they were willing to find out.",
    "Adventure": "They stepped forward, not because the danger had passed, but because the discovery mattered.",
    "Horror": "And somewhere in the dark, something quietly learned their name.",
    "Literary": "Nothing changed all at once, yet everything was different after that.",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "The Story Begins").strip()[:100]
    protagonist = (data.get("protagonist") or "Alex").strip()[:80]
    genre = data.get("genre") or "Fantasy"
    if genre not in GENRE_OPENINGS:
        genre = "Fantasy"
    setting = (data.get("setting") or "a forgotten place at the edge of the world").strip()[:160]
    mood = (data.get("mood") or "wonder").strip()[:60]
    seed = (data.get("seed") or "a mysterious discovery").strip()[:180]
    length = data.get("length", "Short")
    opening = GENRE_OPENINGS[genre]
    turn = GENRE_TURNS[genre]
    ending = GENRE_ENDINGS[genre]
    paragraphs = [
        f"{opening} {protagonist} arrived in {setting}. The air carried a feeling of {mood}, and nothing seemed quite as ordinary as it should.",
        f"It all began with {seed}. At first, {protagonist} treated it as a coincidence, something to file away and forget. But the details kept returning: a pattern, a sound, a small inconsistency that refused to disappear.",
        turn,
        f"{protagonist} took a breath and made a decision. There would be questions, risks, and consequences—but standing still had become its own kind of danger.",
        ending
    ]
    if length == "Micro":
        paragraphs = [paragraphs[0], paragraphs[2], paragraphs[4]]
    elif length == "Long":
        paragraphs.insert(2, f"Every step deeper into the mystery made the world feel larger and more uncertain. {protagonist} gathered the few clues available, testing each one against the quiet instinct that had brought them this far.")
        paragraphs.insert(4, "For a moment, doubt threatened to win. Then one overlooked detail connected everything, turning scattered fragments into a path forward.")
    return jsonify({"title": title, "genre": genre, "story": "\n\n".join(paragraphs)})

if __name__ == "__main__":
    app.run(debug=True)
