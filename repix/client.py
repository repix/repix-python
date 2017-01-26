import imboclient
from repix.url import (
    ImageURL,
    CompactAccessTokenGenerator,
)


class Client(imboclient.Client):
    def __init__(self, server_urls,
                 user=None,
                 public_key=None,
                 private_key=None,
                 access_token_generator=CompactAccessTokenGenerator):
        super(Client, self).__init__(server_urls=server_urls,
                                     user=user,
                                     public_key=public_key,
                                     private_key=private_key,
                                     access_token_generator=access_token_generator)

    def image_url(self, image_identifier):
        return ImageURL(self._pick_url(image_identifier),
                        user=self._user,
                        public_key=self._public_key,
                        private_key=self._private_key,
                        image_identifier=image_identifier,
                        access_token_generator=self.access_token_generator)


