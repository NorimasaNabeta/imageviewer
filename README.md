# ImageViewer

Do you have a bunch of images with meta information that you would like to go through (or share)?

This is a web-based image viewer for that.

It is a small [flask](http://flask.pocoo.org/) app, build with [bootstrap](http://getbootstrap.com/),
which will display images and their meta information in a table, with pagination.

**NOTE:** This app was built to run locally for my own convenience and
to share with a small number of collaborators. In `app.py`, the entire table is
loaded to a global variable `table`. This can be problematic if the table is large,
and the app receives a lot of traffic, as it will load the data for every process.
You'll want to setup a proper database. See

- [this stackoverflow question](http://stackoverflow.com/questions/28141454/flask-using-a-global-variable-to-load-data-files-into-memory)
- flask documentation on databases


## Test out

Do
```shell
git clone 
conda env create    # setup environment specified in environment.yml
python app.py
```
and point your browser to `localhost:5000`.
This will show images inside `example/images/` directory with the related information in `fakecatalog.csv`.

Configure static file paths in `app.py` and modify templates in `templates/`
according to your needs. Flask uses the [jinja](http://jinja.pocoo.org/) template engine.
