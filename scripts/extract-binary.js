const fs = require('fs');
const path = require('path');
const tar = require('tar');

const outputDir = path.join(import.meta.dirname, './build/Release');

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

let binFolder = path.join(import.meta.dirname, 'build/stage/');
let name = readdirSync(binFolder)[0];
let file = fs.createReadStream(path.join(binFolder, name));
file.pipe(tar.x({
      C: outputDir
 })).on('end', () => {
      console.log('Binary extracted successfully!');
});
	