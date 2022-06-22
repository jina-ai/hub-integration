import * as core from '@actions/core'
import * as exec from '@actions/exec'
import {context, getOctokit} from '@actions/github'
import * as glob from '@actions/glob'
import * as io from '@actions/io'

process.on('unhandledRejection', handleError)

async function main(): Promise<any> {
  const token = core.getInput('github-token', {required: true})
  const actions = core.getInput('actions', {required: true});
  const github = getOctokit(token)
  return 0;
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