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
	  
    },
	{
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
