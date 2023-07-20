from jina import Executor, requests


class SanityCheck(Executor):
    @requests(on="/get-tensor")
    def foo(self, docs, **kwargs):
        return docs
