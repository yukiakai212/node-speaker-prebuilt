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
      "dependencies": [ "speaker-binaries" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/speaker-binaries.node" ],
          "destination": "./build/stage/{node_abi}-{platform}-{arch}/"
        }
      ]
    }
  ]
}
