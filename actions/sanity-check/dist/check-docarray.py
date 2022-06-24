from docarray import DocumentArray, Document

def docarray_check():
    d = Document(text='hello')
    d2 = Document(text='world')

    da = DocumentArray([d, d2])
    r = da.push(name='sanity_check_test', show_progress=True)
    assert r.get('name') == 'sanity_check_test'

    da2 = DocumentArray.pull(name='sanity_check_test', show_progress=True)
    assert da2.texts == ['hello', 'world']


docarray_check()
