import re

from django.http.response import HttpResponseRedirect
from django.conf import settings
from django.utils.translation import check_for_language
from django.utils import translation

def change_language_in_path(path, language):
    path = re.sub('^/[a-z]{2}/', '/%s/' % (language,), path) # TODO handle things like en-us
    return path

def set_language_on_response(request, response, lang_code):
    """
    Set the language in session & in cookie on the response
    """

    if hasattr(request, 'session'):
        request.session['django_language'] = lang_code
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    translation.activate(lang_code)

def set_language(request, next=None):
    '''
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.
    Try to save the new language in the User's profile.
    '''
    next = next \
        or request.REQUEST.get('next', None) \
        or request.META.get('HTTP_REFERER', None) \
        or '/'

    response = HttpResponseRedirect(next)
    if request.method == 'GET' or request.method == 'POST':
        lang_code = request.REQUEST.get('language', settings.LANGUAGE_CODE)
        if check_for_language(lang_code):
            # update the language in the url if it's in there
            next = change_language_in_path(next, lang_code)
            response = HttpResponseRedirect(next)

            set_language_on_response(request, response, lang_code)

            # try to save language in the user profile
            if request.user.is_authenticated():
                try:
                    user = request.user
                    user.language = lang_code
                    user.save()
                except:
                    pass

    return response
