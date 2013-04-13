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
            ],
            'include_dirs+': 
            [
              # Not needed now
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
            ]
          }
        ]
      ]
    }
  ]
}
