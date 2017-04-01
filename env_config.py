creds = {

    # MySQL Configuration
    '_INSTANCE_NAME': '',
    'dbuser': '',
    'dbpass': '',
    'dbbase': '',
    'dbhost': '',

    # Google Oauth creds
    'GOOGLE_CLIENT_ID': '',
    'GOOGLE_CLIENT_SECRET': '',
    'REDIRECT_URI': '/oauth2callback',
}


# google auth env
google_auth_env = {
        'base_url': 'https://www.google.com/accounts/',
        'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        'request_token_url': None,
        'request_token_params': {
            'scope': 'https://www.googleapis.com/auth/userinfo.email',
            'response_type': 'code'
        },
        'access_token_url': 'https://accounts.google.com/o/oauth2/token',
        'access_token_method': 'POST',
        'access_token_params': {'grant_type': 'authorization_code'},
        'consumer_key': creds['GOOGLE_CLIENT_ID'],
        'consumer_secret': creds['GOOGLE_CLIENT_SECRET']
}


