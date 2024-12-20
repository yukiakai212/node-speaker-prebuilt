const fs = require('fs');
const path = require('path');
const tar = require('tar');

const outputDir = path.join(__dirname, './build/Release');

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

let binFolder = path.join(__dirname, 'build/stage/');
if(fs.existsSync(binFolder))
{
	let name = readdirSync(binFolder)[0];
let file = fs.createReadStream(path.join(binFolder, name));
file.pipe(tar.x({
      C: outputDir
 })).on('end', () => {
      console.log('Binary extracted successfully!');
});
}
	