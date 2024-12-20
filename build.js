const fs = require('fs');
const path = require('path');
const pkg = require('./package.json');
const source = path.join(__dirname, './prebuilds/all-x64/' + pkg.name + '.node');
const dsc = path.join(__dirname, './build/' + pkg.binary.module_name + '.node');
fs.copyFileSync(source, dsc);
