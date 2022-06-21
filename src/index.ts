import * as core from '@actions/core'
import * as exec from '@actions/exec'
import {context, getOctokit} from '@actions/github'
import * as glob from '@actions/glob'
import * as io from '@actions/io'
import {callAsyncFunction} from './async-function'
import {wrapRequire} from './wrap-require'

process.on('unhandledRejection', handleError)

async function main(): Promise<any> {
  const token = core.getInput('github-token', {required: true})
  const actions = core.getInput('actions', {required: true});
  const github = getOctokit(token)

  let result;
  if ( actions === 'baseline-test') {
    result = await github.rest.actions.createWorkflowDispatch({
      owner: 'jina-ai',
      repo: 'hub-integration',
      workflow_id: 'baseline-test.yml',
      ref: 'main'
    });
  } else if (actions === 'docker-source-combine') {
    result = await github.rest.actions.createWorkflowDispatch({
      owner: 'jina-ai',
      repo: 'hub-integration',
      workflow_id: 'docker-source-combine.yml',
      ref: 'main'
    });
  } else {
    const baselineResult = await github.rest.actions.createWorkflowDispatch({
      owner: 'jina-ai',
      repo: 'hub-integration',
      workflow_id: 'baseline-test.yml',
      ref: 'main'
    });
    const combineResult = await github.rest.actions.createWorkflowDispatch({
      owner: 'jina-ai',
      repo: 'hub-integration',
      workflow_id: 'docker-source-combine.yml',
      ref: 'main'
    });
    result = Object.assign({}, baselineResult, combineResult );
  }
  return result;
}

function handleError(err: any): void {
  console.error(err)
  core.setOutput('result', false)
  core.setFailed(`Unhandled error: ${err}`)
}

try {
  const result = await main();
  core.setOutput('result', result)
} catch (err) {
  handleError(err);
}