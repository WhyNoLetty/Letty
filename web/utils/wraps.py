from quart import session, redirect

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        
        api_token = session.get('token')
        if api_token is None:
            return redirect('/url/login')

        return f(*args, **kwargs)
    return wrapper

