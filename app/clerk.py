import pynecone as pc

from pcconfig import CLERK_PUBLISHABLE_KEY


class ClerkProvider(pc.Component):
    library = "@clerk/clerk-react"
    tag = "ClerkProvider"
    publishable_key: pc.Var[str] = CLERK_PUBLISHABLE_KEY


class SignedIn(pc.Component):
    library = "@clerk/clerk-react"
    tag = "SignedIn"


class SignedOut(pc.Component):
    library = "@clerk/clerk-react"
    tag = "SignedOut"


class SignIn(pc.Component):
    library = "@clerk/clerk-react"
    tag = "SignIn"


class UserButton(pc.Component):
    library = "@clerk/clerk-react"
    tag = "UserButton"


clerk_provider = ClerkProvider.create
signed_in = SignedIn.create
signed_out = SignedOut.create
sign_in = SignIn.create
user_button = UserButton.create
