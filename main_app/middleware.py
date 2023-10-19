from django.utils.translation import activate
from django.conf import settings


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the language hasn't been set for this user session
        if not request.session.get('language_set', False):
            # Set the language to 'vi' by default
            activate('vi')
            request.session['language_set'] = True

        response = self.get_response(request)
        return response