from jina import Flow, Document, requests, Executor

class MyExecutor(Executor):

  @requests
  def foo(self, **kwargs):
    print('goodbye')


f = Flow().add(uses='jinahub+docker://MiaoTestExecutor1').add(uses='jinahub://MiaoTestExecutor1').add(uses=MyExecutor)

with f:
  f.post('/', Document())
