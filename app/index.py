import pynecone as pc

from app import State


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.cond(
                State.error_msg,
                pc.heading(State.error_msg, color="red", font_size="1em"),
            ),
            pc.heading("Gmail Sorter", font_size="1.5em"),
            pc.divider(),
            pc.button(
                "Login with Google",
                on_click=[State.get_authorization_url],
                width="100%",
                bg="#ea4335",
                color="white",
            ),
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",  # noqa: E501
    )
