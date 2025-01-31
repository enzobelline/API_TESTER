from setuptools import setup, find_packages

setup(
    name="API_TESTER",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "slowapi",
        "pydantic",
        "pyjwt",
    ],
    entry_points={
        "console_scripts": [
            "yourlibrary = yourlibrary.main:create_api",
        ],
    },
)
