from jina import Flow

from docarray import Document

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
                Document(text="vvvv"),
                Document(text="aaaa"),
                Document(text="dddddd aaaa"),
                Document(text="dddddd bbbb"),
            ],
        )
        f.close()


run_flow(prod_demo('jinahub://SanityCheck:sanity@Check'))
run_flow(prod_demo('jinahub+sandbox://SanityCheck:sanity@Check'))
run_flow(prod_demo('jinahub+docker://SanityCheck:sanity@Check'))
