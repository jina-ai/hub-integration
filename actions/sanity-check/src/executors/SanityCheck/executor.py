from jina import Executor, DocumentArray, requests


class SanityCheck(Executor):
    @requests(on="/get-tensor")
    def foo(self, docs: DocumentArray, **kwargs):
        docs[0].text = "SanityCheck foo doc0"
        print("SanityCheck.foo", docs)
        return docs
