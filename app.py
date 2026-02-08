"""
Market Research Parallel Analyzer — Flask Application.

Upload market research documents for Moldova, Georgia, and Armenia,
discover cross-market parallels, and generate audience profiles
with social media campaign ideas.
"""

import os
import json

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

from analyzer import (
    analyze_single_market,
    generate_all_outputs,
)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(__file__), "uploads")
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50 MB
ALLOWED_EXTENSIONS = {"docx", "xlsx"}

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """Accept up to 3 files (one per market), run analysis, return JSON results."""
    markets = ["moldova", "georgia", "armenia"]
    analyses = []
    errors = []

    for market in markets:
        file = request.files.get(market)
        if not file or file.filename == "":
            continue
        if not allowed_file(file.filename):
            errors.append(f"{market.title()}: unsupported file type (use .docx or .xlsx)")
            continue

        filename = secure_filename(f"{market}_{file.filename}")
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(path)

        try:
            analysis = analyze_single_market(path, market)
            # Don't send raw tokens/text back to frontend
            analyses.append(analysis)
        except Exception as e:
            errors.append(f"{market.title()}: error parsing file — {e}")

    if len(analyses) < 2:
        return jsonify({
            "success": False,
            "errors": errors or ["Please upload documents for at least 2 markets."],
        }), 400

    results = generate_all_outputs(analyses)

    # Prepare a serialisable summary of each market
    market_summaries = []
    for a in analyses:
        market_summaries.append({
            "market": a["market"].title(),
            "word_count": a["word_count"],
            "top_themes": sorted(a["themes"].items(), key=lambda x: -x[1])[:5],
            "key_phrases": a["key_phrases"][:10],
        })

    return jsonify({
        "success": True,
        "errors": errors,
        "market_summaries": market_summaries,
        "parallels": {
            "shared_themes": results["parallels"]["shared_themes"],
            "unique_themes": results["parallels"]["unique_themes"],
            "overlapping_phrases": results["parallels"]["overlapping_phrases"][:15],
            "opportunities": results["parallels"]["parallel_opportunities"],
        },
        "profiles": results["profiles"],
        "campaigns": results["campaigns"],
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
