/* eslint-disable no-console */
const { promises: { readdir, writeFile } } = require('fs');
const { join } = require('path');

const manifest = require('./manifest.json');
const pkg = require('./package.json');

const lsr = async (path) => {
  const files = [];
  const entries = await readdir(path, { withFileTypes: true });
  await Promise.all(entries.map(async (entry) => {
    if (entry.isFile()) {
      files.push(join(path, entry.name));
    } else if (entry.isDirectory()) {
      const children = await lsr(join(path, entry.name));
      children.forEach((child) => {
        files.push(child);
      });
    }
  }));
  return files;
};

(async () => {
  manifest.version = pkg.version;
  manifest.web_accessible_resources = await lsr('./src');
  console.log(`Web-accessible:\n\t${manifest.web_accessible_resources.join('\n\t')}`);
  writeFile('./manifest.json', `${JSON.stringify(manifest, null, 2)}\n`);
  console.log('Updated manifest.json');
})();
