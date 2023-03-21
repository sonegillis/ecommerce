from django.utils.deprecation import MiddlewareMixin


class ApiResponseMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        # Code that is executed in each request before the view is called
        response = self.get_response(request)
        # Code that is executed in each request after the view is called
        return response

    def process_template_response(self, request, response):
        if hasattr(response, "data"):
            response.data = {
                "erc": 1,
                "msg": "success",
                "data": response.data
            }
        return response
