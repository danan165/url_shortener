# URL Shortener

A lightweight Python Flask API for URL shortening and restoring.

[![Python Package](https://github.com/danan165/url_shortener/actions/workflows/python-package.yml/badge.svg)](https://github.com/danan165/url_shortener/actions/workflows/python-package.yml)

---

## Description

This Python Flask app exposes two routes for URL shortening:
1. **compress**

    Shortens the given URL to an alphanumeric string.
    
    Example call:

    ```
    curl --location --request POST 'http://127.0.0.1:5000/compress' 
    --header 'Content-Type: application/json' 
    --form 'url="http://exploreflask.com/en/latest/blueprints.html";type=application/json'
    
    ```

    Example response (201 CREATED):

    ```
    {
        "data": "MQ=="
    }
    ```

2. **restore**

    Given the shortened URL, returns the original URL (or returns `None` if the shortened URL is not recognized).

    Example call:

    ```
    curl --location --request POST 'http://127.0.0.1:5000/restore' 
    --header 'Content-Type: application/json' 
    --form 'url="MQ==";type=application/json'
    ```

    Example response (200 OK):

    ```
    {
        "data": "http://exploreflask.com/en/latest/blueprints.html"
    }
    ```

---

## Design

The URL shortener works by assigning a unique ID to each URL that is provided for shortening. The unique ID/URL are stored as a key/value pair (respectively) in a Python dictionary. This dictionary is persisted in memory so that URLs can be compressed/decompressed by performing inserts and lookups into this dictionary.

**Pseudocode for URL shortening**:

1. If the given URL does not already exist in the dictionary, return it's shortened URL. This is an O(N) operation, where N represents the number of URLs given to this application so far. Meaning, the time it takes for this operation scales linearly with the amount of URLs that have been processed so far.

2. If the given URL does not exist, then compress it. This is done by base64 encoding a unique integer (1 for the first URL processed, 2 for the second URL processed, etc). The resulting string is then stored as the key, and the URL is stored as the value in the dictionary.


**Pseudocode for URL restoring**:

1. Given a shortened URL, return the value stored in the dictionary where the key is equal to the shortened URL. This is a constant-time O(1) lookup.

2. If the shortened URL is not in the dictionary, return `None`.

See implementation details in `url_shortener/models.py`.

---

## Usage

1. Ensure you are running the app from the proper directory:
```
/c/Users/you$ pwd
    /url_shortener

/c/Users/you$ ls
    README.md  setup.py  tests  url_shortener
```

2. Setup virtual env and setup the Flask app
```
python -m venv env
source env/bin/activate
pip install -e .
flask --app url_shortener run
```

3. Run the unit tests and calculate code coverage
```
python -m unittest 
coverage run -m unittest
coverage report
```

---

## TODO: Future Enhancements

1. Write unit tests in `tests/test_flask_routes.py` to test the functions in `url_shortener/routes.py`. Will need to do some mocking setup of the flask app.

2. CI for code coverage: tried coveralls, but it couldn't pick up my most recent repos (only showed me my old repos). Will look into codecov.

3. `compress` Flask route should return 200 OK if the given URL has already been shortened. Currently, returns 201 CREATED for all URLs.

4. Current `URLShortener` instantiation in `url_shortener/routes.py` isn't best practice -- it's a global instance. 

---

## References

- [Flask Docs: Large Applications as Packages](https://flask.palletsprojects.com/en/2.2.x/patterns/packages/)
- [Stack Overflow: Common folder/file structure in Flask app](https://stackoverflow.com/questions/14415500/common-folder-file-structure-in-flask-app)
- [Flask Docs: Testing Flask Applications](https://flask.palletsprojects.com/en/1.0.x/testing/)
- [Stack Overflow: Idea for Base64 encoding an Integer (needed an alphanumeric short string)](https://stackoverflow.com/questions/1497504/how-to-make-unique-short-url-with-python)

