#setup.py

from setuptools import setup, find_packages

setup(
    name="lumpkin",
    version="0.1",
    description="A simple Python package for handling emails via IMAP and SMTP.",
    author="Alex Ruco",
    author_email="alex.ruco@mysitefaster.com",
    url="https://github.com/alexruco/lumpkin",
    packages=find_packages(),
    install_requires=[
        # These should match your requirements.txt
        "imaplib2",
        "smtplib",
        "email"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
