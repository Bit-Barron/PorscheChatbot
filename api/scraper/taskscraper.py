import requests
from bs4 import BeautifulSoup
from flask import Flask, Blueprint
from utils.helper import remove_umlaut

app = Flask(__name__)
taskscraper_bp = Blueprint('taskscraper', __name__)
