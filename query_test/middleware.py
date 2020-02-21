
from django.utils.deprecation import MiddlewareMixin


CORS_ALLOW_HEADERS = [
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'cache-control',
    'x-http-method-override',
    'x-bulk-operation',
    'x-frame-options',
]


class CorsMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, PUT, PATCH, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = ', '.join(CORS_ALLOW_HEADERS)
        response['Access-Control-Max-Age'] = 86400

        return response

