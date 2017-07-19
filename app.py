#!/bin/env python
from script import create_app
import os

app = create_app()

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=5001)
