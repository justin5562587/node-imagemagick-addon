# -- /Users/justin/lib_source/ImageMagick-7.0.10/include
# -- /Users/justin/lib_source/ImageMagick-7.0.10/lib/libMagick++-7.Q16HDRI.dylib
{
    "variables": {
        "MAGICK_ROOT%": "/Users/justin/lib_source/ImageMagick-7.0.10",
    },
    "targets": [
        {
            "target_name": "j_image_addon",
            "type": "shared_library",
            "sources": ["src/imageHander.cpp"],
            'cflags!': ['-fno-exceptions'],
            'cflags_cc!': ['-fno-exceptions'],
            "include_dirs": [
                "<!(node -e \"require('node-addon-api')\")",
            ],
            "libraries": [
                "<(MAGICK_ROOT)/lib/libMagick++-7.Q16HDRI.dylib",
            ],
            "conditions": [
                ['OS=="mac"', {
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'OTHER_CFLAGS': [
#                             '<!@(pkg-config --cflags ImageMagick++)'
                        ]
                    },
                    "libraries": [
                        # '<!@(pkg-config --libs ImageMagick++)',
                        "-l<(MAGICK_ROOT)/lib/libMagick++-7.Q16HDRI.dylib",
                    ],
                    'include_dirs': [
                        '<(MAGICK_ROOT)/include',
                    ]
                    # 'cflags': [
                    #     '<!@(pkg-config --cflags ImageMagick++)'
                    # ],
                }],
            ]
        }
    ]
}
