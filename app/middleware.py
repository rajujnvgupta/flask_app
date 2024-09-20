from flask import request

def before_request_logging():
    print(f"Request: {request.method} {request.url}")
    if request.data:
        print(f"Request Body: {request.data}")

def after_request_logging(response):
    print(f"Response: {response.status_code}")
    return response
