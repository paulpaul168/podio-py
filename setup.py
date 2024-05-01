from setuptools import setup

setup(
    name="podiopy",
    version="0.2",
    description="Python wrapper for the Podio API",
    author="Podio",
    author_email="mail@podio.com",
    url="https://github.com/podio/podio-py",
    license="MIT",
    packages=["podiopy"],
    install_requires=["httplib2"],
    tests_require=["nose", "mock", "tox"],
    test_suite="nose.collector",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
