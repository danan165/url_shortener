from flask import request, jsonify
from url_shortener import app
from url_shortener.models import URLShortener

URLShortenerInst = URLShortener()

@app.route("/compress", methods = ['POST'])
def compress():
    print("in compress route...")
    data = dict(request.form)
    if "url" in data:
        compressed = URLShortenerInst.shorten(data["url"])
        return jsonify({
            "data": compressed
        }), 201
    else:
        return jsonify({
            "Error": "No url found in request body."
        }), 400


@app.route("/restore", methods = ['POST'])
def restore():
    data = dict(request.form)
    if "url" in data:
        restored = URLShortenerInst.restore(data["url"])
        return jsonify({
            "data": restored
        }), 200
    else:
        return jsonify({
            "Error": "No url found in request body."
        }), 400

