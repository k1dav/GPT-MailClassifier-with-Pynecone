import pynecone as pc
import os

CLERK_PUBLISHABLE_KEY = os.environ["CLERK_PUBLISHABLE_KEY"]

config = pc.Config(
    app_name="app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
