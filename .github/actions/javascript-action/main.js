const core = require('@actions/core');
// const github = require('@actions/github');
const exec = require('@actions/exec');

function run() {
  // 1) Get some input values
  const bucket = core.getInput('bucket', { required: true });
  const bucketRegion = core.getInput('bucket-region', { required: true });
  const distFolder = core.getInput('dist-folder', { required: true });

  core.setOutput('website-url', 'localhost:8000')

  exec.exec(`echo folder: ${distFolder}, bucket: ${bucket}, region: ${bucketRegion}`);
}

run();
