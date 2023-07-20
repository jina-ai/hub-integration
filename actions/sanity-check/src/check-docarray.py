from docarray import BaseDoc, DocList

def docarray_check():
    class SimpleDoc(BaseDoc):
        text: str

    docs = DocList[SimpleDoc]([SimpleDoc(text='hello'), SimpleDoc(text='world')])

    r = docs.push(url='jac://sanity_check_test', show_progress=True)
    assert r.get('name') == 'sanity_check_test'

    r = DocList[SimpleDoc].pull(url='jac://sanity_check_test', show_progress=True, local_cache=False)
    assert r[0].text == 'hello'
    assert r[1].text == 'world'

docarray_check()
