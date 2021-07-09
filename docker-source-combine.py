from jina import Flow, Document, requests, Executor

class MyExecutor(Executor):

  @requests
  def foo(self, **kwargs):
    print('goodbye')


f = Flow().add(uses='jinahub+docker://MiaoExec').add(uses='jinahub://MiaoExec').add(uses=MyExecutor)

with f:
  f.post('/', Document())