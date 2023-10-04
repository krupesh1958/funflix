#!/usr/bin/env python3
"""
Run Funflix flask application.
"""
from config import server as server


if __name__ == "__main__":
    server.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
