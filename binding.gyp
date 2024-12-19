{
  'targets': [
    {
      'target_name': 'speaker-binaries',
      'sources': [
        'src/binding.c',
      ],
	  "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      'dependencies': [
        'deps/mpg123/mpg123.gyp:output'
      ],
    }
  ]
}
