# Middlewares

class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add Response

        response = self.get_response(request)
        response['alpha'] = 'Gen A'
        response['z'] = 'Gen Z'
        return response
