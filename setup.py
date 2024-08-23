from setuptools import setup, find_packages

setup(
    name="lumpkin",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "imaplib2",
    ],
    entry_points={
        'console_scripts': [
            'lumpkin=lumpkin:main',  # This assumes 'main' is in __init__.py
        ],
    },
    author="Alex Ruco",
    author_email="alex@ruco.pt",
    description="A package for handling emails with hashing functionality.",
    url="https://github.com/alexruco/lumpkin",
)
