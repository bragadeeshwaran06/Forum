import hashlib
from urllib.parse import urlencode
from django import template

register = template.Library()

@register.filter
def gravatar(user, size=256):
    """
    Returns the Gravatar URL for the given user’s email address.

    :param user: The user object with an email attribute.
    :param size: The size of the Gravatar image in pixels.
    :return: The Gravatar URL.
    """
    email = user.email.lower().encode('utf-8')
    default = 'mm'  # 'mm' stands for 'mystery man', a default image provided by Gravatar
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url
