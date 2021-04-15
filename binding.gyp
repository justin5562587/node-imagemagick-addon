{
    "variables": {
        "MAGICK_ROOT%": "/",
    },
    "targets": [
        {
            "target_name": "j_image_addon",
            "sources": ["src/imageHander.cpp"],
            'cflags!': ['-fno-exceptions'],
            'cflags_cc!': ['-fno-exceptions'],
            "include_dirs": [
                "<!(node -e \"require('node-addon-api')\")"
            ],
            "conditions": [
                ['OS=="mac"', {
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'OTHER_CFLAGS': [
                            '<!@(pkg-config --cflags ImageMagick++)'
                        ]
                    },
                    "libraries": [
                        '<!@(pkg-config --libs ImageMagick++)',
                    ],
                    'cflags': [
                        '<!@(pkg-config --cflags ImageMagick++)'
                    ],
                    # "libraries": [
                    #     '-l<(MAGICK_ROOT)/lib/CORE_RL_magick_.lib',
                    #     '-l<(MAGICK_ROOT)/lib/CORE_RL_Magick++_.lib',
                    #     '-l<(MAGICK_ROOT)/lib/CORE_RL_wand_.lib',
                    # ],
                    # 'include_dirs': [
                    #     '<(MAGICK_ROOT)/include',
                    # ]
                }],
            ]
        }
    ]
}
