"""
    Author      : CHINY Antoine
    Date        : mer. 04 juil. 2018 15:13:13 CEST
    Description :
    Usage       :

"""

from flask import Flask
from .resources import get_config

app = Flask(__name__)
config = get_config()

if __name__ == '__main__':
    app.run()
