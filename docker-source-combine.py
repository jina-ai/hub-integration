from docarray import Document
from jina import Flow, requests, Executor

class MyExecutor(Executor):

  @requests
  def foo(self, **kwargs):
    print('goodbye')


f = Flow().add(
  uses='jinahub+docker://Hello'
).add(
  uses='jinahub://Hello'
).add(
  uses=MyExecutor
)

with f:
  f.post('/', Document())
