#!/usr/bin/env python3

from lib.flask.app import create_app
from lib.flask.flask_config import Config

app = create_app(None)
app.config.from_object(Config)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(Config.FLASK_PORT), debug=True)