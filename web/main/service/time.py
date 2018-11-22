from flask import jsonify
import datetime

def health_check():
    status = {'status' : 'OK'}
    return jsonify(status), 200

def time():
    time = {'Current time' : str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")) }
    return jsonify(time), 200
