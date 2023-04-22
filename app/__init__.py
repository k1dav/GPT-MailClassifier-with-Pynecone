from uuid import uuid4
import pynecone as pc
from google_auth_oauthlib.flow import Flow
from urllib.parse import urlencode


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
]

REDIRECT_URI = "https://react--main--mailsorter--dave.coder.k1dav.fun/callback"


def get_flow():
    flow = Flow.from_client_secrets_file("client_secret.json", SCOPES)
    flow.redirect_uri = REDIRECT_URI
    return flow


class State(pc.State):
    token: str = ""
    state: str = ""
    error_msg: str = ""

    def get_authorization_url(self):
        self.token = ""
        self.error_msg = ""

        flow = get_flow()
        self.state = str(uuid4())
        authorization_url, _ = flow.authorization_url(state=self.state)
        return pc.redirect(authorization_url)

    def login_google(self):
        if self.get_query_params()["state"] != self.state:
            self.error_msg = "Login Fail"
            return pc.redirect("/")

        full_url = f"{REDIRECT_URI}?{urlencode(self.get_query_params())}"
        flow = get_flow()
        flow.fetch_token(authorization_response=full_url)
        self.token = flow.credentials.token

        return pc.redirect("/sorter")
