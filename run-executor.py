import os 
import sys 

from docarray import Document
from jina import Flow

print(sys.argv[1], os.environ.get('JINA_HUBBLE_REGISTRY'))
f = Flow().add(uses=sys.argv[1])

with f:
  print(f.post('/', Document()))
