from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

# OAuth Setup
oauth = OAuth()

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret

SECRET_KEY=some-random-secret

# Google OAuth registration
oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

# GitHub OAuth registration
oauth.register(
    name='github',
    client_id=os.getenv('GITHUB_CLIENT_ID'),
    client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'}
)

@app.get("/", response_class=HTMLResponse)
async def homepage():
    return """
    <h1>OAuth Login</h1>
    <a href='/login/google'>Login with Google</a><br>
    <a href='/login/github'>Login with GitHub</a>
    """

@app.get("/login/{provider}")
async def login(request: Request, provider: str):
    if provider not in oauth:
        return HTMLResponse(f"Provider '{provider}' not supported", status_code=400)
    redirect_uri = request.url_for("auth_callback", provider=provider)
    return await oauth.create_client(provider).authorize_redirect(request, redirect_uri)

@app.get("/auth/{provider}/callback")
async def auth_callback(request: Request, provider: str):
    client = oauth.create_client(provider)
    token = await client.authorize_access_token(request)
    user = await client.parse_id_token(request, token) if provider == 'google' else await client.get('user', token=token)
    request.session['user'] = user.json() if provider == 'github' else dict(user)
    return RedirectResponse(url="/profile")

@app.get("/profile")
async def profile(request: Request):
    user = request.session.get("user")
    if not user:
        return RedirectResponse(url="/")
    return HTMLResponse(f"<h2>Logged in as: {user.get('name') or user.get('login')}</h2><a href='/logout'>Logout</a>")

@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")
