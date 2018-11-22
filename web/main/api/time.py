from flask import Blueprint, redirect, url_for
from web.main.service.time import health_check, time


api = Blueprint('api', __name__)

@api.route('/')
def index():
    return redirect(url_for('api.now'))

@api.route('/now')
def now():
    return time()

@api.route('/health')
def health():
    return health_check()
