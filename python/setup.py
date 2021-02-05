import setuptools

from setuptools import setup, find_packages

setup(
    name="systemathics.apis",
    version="0.0.39",
    author="Systemathics",
    author_email="contact@systemathics.com",
    description="Python grpc stub for Systemathics APIs.",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    namespace_packages=['systemathics'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    python_requires='>=3.6',
    install_requires=['googleapis-common-protos', 'protobuf', 'grpcio'],
)

## pip install --no-binary=protobuf protobuf