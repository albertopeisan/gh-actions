const core = require('@actions/core')
const github = require('@actions/github')
const exec = require('@actions/exec')

function run() {
  // Get input values
  const bucket = core.getInput('bucket', { required: true });
  const region = core.getInput('region', { required: true });
  const folder = core.getInput('dist-folder', { required: true });

  // Execute a command
  exec.exec(`echo ${ bucket }, ${ region }, ${ folder }`)

  // You can access github context in the action
  // github.context.

  core.notice('Hello from my custom javascript action')
}

run();