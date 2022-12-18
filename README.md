# URL Shortener

## Usage

1. Ensure you are running the app from the proper directory:
```
/c/Users/you$ pwd
    /url_shortener

/c/Users/you$ ls
    README.md  setup.py  url_shortener
```

2. Setup virtual env and setup the Flask app
```
python -m venv env
source env/bin/activate
pip install -e .
flask --app url_shortener run
```

3. Run the unit tests
```
python -m unittest 
```


## References

- [Flask Docs: Large Applications as Packages](https://flask.palletsprojects.com/en/2.2.x/patterns/packages/)
- [Stack Overflow: Common folder/file structure in Flask app](https://stackoverflow.com/questions/14415500/common-folder-file-structure-in-flask-app)
- [Flask Docs: Testing Flask Applications](https://flask.palletsprojects.com/en/1.0.x/testing/)

