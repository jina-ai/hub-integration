# Hub-integration
- Integration test for `jina hub ...`
- it is a reusing workflow

## Includes 

- Base API sanity check, e.g. user, artifact...
- `jina hub push/pull` test

### Base API sanity check

- Includes
  - docarray 
  - executor 
  - artifact 
  - user-api
  - docker-source-combine
		
### `jina hub push/pull`

- For case 1-9 (except for case4) in 
  [test-case](https://github.com/jina-ai/executor-cases)
- Combined test.

  ```python
  Flow().add(uses='jinahub://UUID').add(uses='jinahub+docker://UUID').add(LOCAL_EXECUTOR)
  ```

## How to use

```yaml
on: [push]
jobs:
  hub-actions:
    uses: jina-ai/hub-integration/.github/workflows/main.yml@main
    with:
      # options includes [all, baseline_test, sanity_check]
      actions: 'all' 
   
    secrets: 
      # github personal auth token and use it to pull hubble repo and jina repo
      jina_dev_bot: ${{ secrets.JINA_DEV_BOT }}
      # jina auth token and use it to run sanity_check
      jina_auth_token: ${{ secrets.JINA_AUTH_TOKEN }}
```

