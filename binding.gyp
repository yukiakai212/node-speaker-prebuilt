{
  'targets': [
    {
      'target_name': 'speaker-binaries',
      'sources': [
        'src/binding.c',
      ],
      'dependencies': [
        'deps/mpg123/mpg123.gyp:output'
      ],
    }
  ]
}
