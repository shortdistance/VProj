#!/bin/env python
from script import create_app
from script.models.database import db_session
from script.config import USE_GCLOUD, DEBUG
import logging

app = create_app()
from werkzeug.contrib.fixers import ProxyFix

# Flask will automatically remove database sessions at the end
# of the request or when the application shuts down
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if not USE_GCLOUD and __name__ == '__main__':
    handler = logging.FileHandler('flask.log')
    app.logger.addHandler(handler)
    app.run(host='127.0.0.1', port=5001, debug=DEBUG)

# start the application
# cd /path/to/opendata_coursework2
# gunicorn app:app
