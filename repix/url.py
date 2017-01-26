import sys
import hmac
import hashlib

from base64 import b64encode

from imboclient.url.image import UrlImage


class ImageURL(UrlImage):
    def __init__(self, base_url, user, public_key, private_key, image_identifier, **kwargs):
        super(ImageURL, self).__init__(base_url, public_key, private_key, image_identifier, user, **kwargs)

    def resource_url(self):
        ext = ''

        if self._type:
            ext = '.' + self._type

        if not self._public_key and not self._user:
            return self.user_url(self._image_identifier + ext)

        return self.user_url('images/' + self._image_identifier + ext)

    def user_url(self, resource):
        u = self._user if self._user else self._public_key

        if not u:
            return self._base_url + '/' + resource

        return self._base_url + '/users/' + u + '/' + resource


class CompactAccessTokenGenerator:
    @classmethod
    def generate_token(cls, url, private_key):
        if sys.version_info < (3,):
            at = hmac.new(private_key, url, hashlib.sha256).digest()
        else:
            at = hmac.new(bytes(private_key, 'utf-8'), bytes(url, 'utf-8'), hashlib.sha256).digest()

        return b64encode(at, b'-_')[:8].decode('ascii')

    def token_key(self):
        return 'cs'
