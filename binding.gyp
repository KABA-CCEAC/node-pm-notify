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
            'sources': [
              "src/pm_linux.cpp"
            ],
            'include_dirs+': 
            [
              '/usr/include/dbus-1.0/',
              '/usr/include/glib-2.0/',
              '/usr/lib/i386-linux-gnu/glib-2.0/include/',
              '/usr/lib/i386-linux-gnu/dbus-1.0/include/'
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
