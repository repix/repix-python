from repix import Client


def test_client_with_default_api_account():
    c = Client(server_urls='https://unique')
    assert str(c.image_url('foo')) == 'https://unique/foo'


def test_client_with_default_api_account_and_private_key():
    c = Client(server_urls='https://unique', private_key='foo')
    assert str(c.image_url('foo')).startswith('https://unique/foo?cs=')


def test_client_access_token_generation():
    c = Client(server_urls='https://unique', user='foo', public_key='foo', private_key='foo')
    assert str(c.image_url('foo')) == 'https://unique/users/foo/images/foo?publicKey=foo&cs=ioLU1cJB'
