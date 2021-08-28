from setuptools import setup, find_packages

with open("README.rst", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="pygame-2048",
    version="1.9.4",
    author="Dai Zhengcheng",
    author_email="dzcheng827@gmail.com",
    description="A 2048 game ",
    long_description=long_description,
    license="MIT License",
    url="https://github.com/dzc217/game_2048",
    packages=find_packages(),
    package_data={'': ['*.png', '*.TTF']},
    keyword=['game', '2048', 'pygame'],
    install_requires=[
        'pygame'
    ],
    classifiers=[
        "Topic :: Games/Entertainment :: Puzzle Games",
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.9',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
    ],
    entry_points={
            'console_scripts': ['game-2048=game_2048.game:run_game']
        }
)