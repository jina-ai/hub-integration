from jina import Flow

from docarray import BaseDoc, DocList

class SimpleDoc(BaseDoc):
    text: str

def prod_demo(uses: str):
    f = Flow().add(
        uses=uses,
        force_update=True
    )
    return f


def run_flow(f):
    with f:
        f.post(
            "/get-tensor",
            [
                SimpleDoc(text="vvvv"),
                SimpleDoc(text="aaaa"),
                SimpleDoc(text="dddddd aaaa"),
                SimpleDoc(text="dddddd bbbb"),
            ],
        )
        f.close()


run_flow(prod_demo('jinahub://SanityCheck:sanity@Check'))
# run_flow(prod_demo('jinahub+sandbox://SanityCheck:sanity@Check'))
run_flow(prod_demo('jinahub+docker://SanityCheck:sanity@Check'))
