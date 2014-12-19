{
  'includes':[
    '../common/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'tizen_filesystem',
      'type': 'loadable_module',
      'variables': {
        'packages': [
          'capi-appfw-application',
          'pkgmgr-info',
        ],
      },
      'sources': [
        # filesystem_api.js is generated by inject_encodings action below
        '<(INTERMEDIATE_DIR)/filesystem_api.js',
        'filesystem_extension.cc',
        'filesystem_extension.h',
        'filesystem_instance.cc',
        'filesystem_instance.h',
        '../common/virtual_fs.cc',
        '../common/virtual_fs.h',
      ],
      'includes': [
        '../common/pkg-config.gypi',
      ],
      'actions': [
        {
          'action_name': 'inject_encodings',
          'inputs': [
            'tools/inject_encodings.py',
            'filesystem_api.src.js'
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/filesystem_api.js'
          ],
          'action' : ['python', 'tools/inject_encodings.py', 
                      'filesystem_api.src.js', '<(INTERMEDIATE_DIR)/filesystem_api.js']
        }
      ]
    },
  ],
}