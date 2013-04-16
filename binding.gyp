{
  "targets": [
    {
      "target_name": "pm",
      "sources": [
        "src/pm.cpp",
        "src/pm.h"
      ],
      'conditions': [
        ['OS=="win"',
          {
            'sources': [
              "src/pm_win.cpp"
            ]
          }
        ],
        ['OS=="mac"',
          {
            'sources': [
              "src/pm_mac.cpp"
            ]
          }
        ],
        ['OS=="linux"',
          {
            "conditions" : 
            [
              ["target_arch=='ia32'", 
                {
                  'include_dirs+': 
                  [
                    '/usr/include/dbus-1.0/',
                    '/usr/include/glib-2.0/',
                    '/usr/lib/i386-linux-gnu/glib-2.0/include/',
                    '/usr/lib/i386-linux-gnu/dbus-1.0/include/'
                  ]
                }
              ],
              ["target_arch=='x64'", 
                {
                  'include_dirs+': 
                  [
                    '/usr/include/dbus-1.0/',
                    '/usr/include/glib-2.0/',
                    '/usr/lib/x86_64-linux-gnu/glib-2.0/include/',
                    '/usr/lib/x86_64-linux-gnu/dbus-1.0/include/'
                  ],
                }
              ]
            ],
            'sources': [
              "src/pm_linux.cpp"
            ],
            'link_settings': {
              'libraries': [
                '-ldbus-glib-1'
              ]
            }
          }
        ]
      ]
    }
  ]
}
