from .models import Request

import json


class SaveRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        Request(
            method=request.method,
            path=request.path,
            status_code=response.status_code,
            body=request.body.decode(),
            headers=request.META
        ).save()
        return response
