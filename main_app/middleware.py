from django.utils.translation import activate
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('language_set', False):
            logger.debug("Setting language to 'vi'")
            activate('vi')
            request.session['language_set'] = True

        response = self.get_response(request)
        return response