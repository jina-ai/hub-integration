# Hub-integration
- Integration test for `jina hub ...`
- it is a reusing workflow

## Includes 

	- Sanity_check
	- Baseline_test
	- Docker_source_combine

### Sanity_check
- Includes
  - docarray 
  - executor 
  - artifact 
  - user-api
		
### Baseline_test

- For case 1-9 (except for case4) in 
  [test-case](https://github.com/jina-ai/executor-cases)
- Combined test.

  ```python
  Flow().add(uses='jinahub://UUID').add(uses='jinahub+docker://UUID').add(LOCAL_EXECUTOR)
  ```
 
### Docker_source_combine
 - test jina, clone jina, install it and run case executor

 
## How to use it
- In your workflow jobs

```
on: [push]
jobs:
  hub-actions:
    uses: jina-ai/hub-integration/.github/workflows/main.yml@master
    with:
      actions: 'baseline_test' 
        ### options includes [all, baseline_test, sanity_check, docker_source_combine]
      secrets: 
        jina_dev_bot: ${{ secrets.JINA_DEV_BOT }}
        ### "github personal auth token and use it to pull hubble repo and jina repo"
        jina_auth_token: ${{ secrets.JINA_AUTH_TOKEN }}
        ### "jina auth token and use it to run sanity_check"
```

