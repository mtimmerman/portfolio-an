import re

from django.http.response import HttpResponseRedirect
from django.conf import settings
from django.utils.translation import check_for_language, ugettext_lazy as _
from django.utils import translation
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import EmailMultiAlternatives

from portfolio_an.forms import ContactForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail.message import EmailMessage

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
    """
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.
    Try to save the new language in the User's profile.
    """

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


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()

            message = render_to_string("email.html", {'contact': contact})

            msg = EmailMessage('Info verzoek van anverhuizen.be',
                               message,
                               contact.email,
                               ['anverhuizen@gmail.com'])
            msg.content_subtype = "html"

            if 'attachment' in request.FILES:
                request.FILES['attachment'].seek(0)
                msg.attach(request.FILES['attachment'].name,
                           request.FILES['attachment'].read(),
                           request.FILES['attachment'].content_type)

            msg.send(fail_silently=False)

            messages.success(request, _("Ik heb jouw bericht ontvangen en zal zo snel mogelijk contact opnemen."))

            return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactForm()

    return render_to_response('home.html',
                              {'form': form},
                              RequestContext(request))
