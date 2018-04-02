"""
Model View Controller example implementation
Example uses Flask framework which will generate Jinja html template from Python code

Intended to separate internal representations of data (domain objects) 
from the ways it is presented to/accepted from the user

Model is the internal representation (database table etc)
View is the output returned by the application (html page)
Controller is the broker which handles requests, fetching from the model and returning to view
"""

import Flask

@app.route('/')
def example_page():
    """ Searched database for entries, then displays them """
    db = get_db()
    query = db.execute("SELECT * FROM entries ORDER BY id DESC")
    entries = query.fetchall()
    return render_template("example_page.html", entries = entries)

