# hub-integration
Integration test for `jina hub ...`

Tests list:

- Baseline test. For case 1-9 (except for case4) in https://github.com/jina-ai/executor-cases
- Combined test.

  ```python
  Flow().add(uses='jinahub://UUID').add(uses='jinahub+docker://UUID').add(LOCAL_EXECUTOR)
  ```