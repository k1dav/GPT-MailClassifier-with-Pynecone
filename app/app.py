import pynecone as pc

from app import State
from app.callback import callback
from app.index import index
from app.sorter import sorter

app = pc.App(state=State)
app.add_page(index)
app.add_page(callback, on_load=State.login_google)
app.add_page(sorter)
app.compile()
