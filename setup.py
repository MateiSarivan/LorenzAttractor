from setuptools import setup

setup(
    name="lorat",
    version="0.1",
    description="Lorenz attractor implementation",
    long_description="Lorenz attractor implementation",
    author="Ioan-Matei Sarivan",
    author_email="ioanms@mp.aau.dk",
    packages=[
        "lorat"
    ],
    package_dir={
        "lorat":"lorat"
        },
    entry_points={
        "console_scripts": [
            "lorat=lorat.__init__:main"
        ]
    },
    # package_data={
    #     "swserver": ["json/*"
    #      ]
    # },
    # include_package_data=True,
    install_requires=[
        "pandas"
    ],
    zip_safe=False,
    keywords="lorat",
    classifiers=[
        "Development Status :: Experimental",
        "Intended Audience :: Researchers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8"
    ]

)