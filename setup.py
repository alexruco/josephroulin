from setuptools import setup, find_packages

setup(
    name="lumpkin",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "imaplib2",
        # 'smtplib' and 'email' have been removed because they are part of the standard library
    ],
    entry_points={
        'console_scripts': [
            'lumpkin=lumpkin:main',  # Adjust this according to your entry point
        ],
    },
    author="Alex Ruco",
    author_email="alexruco@example.com",
    description="A package for handling emails with hashing functionality.",
    url="https://github.com/alexruco/lumpkin",
)
