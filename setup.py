from setuptools import setup, find_packages

setup(
    name="rutos-api-lib",
    description="Teltonika RutOS API client library",
    url="https://github.com/ChistokhinSV/rutos-api-lib",
    author="Sergei Chistokhin",
    author_email="mail4headless@gmail.com",
    license="BSD-3-Clause",
    include_package_data=True,
    packages=find_packages(exclude=["tests", "tests.*"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "requests>=2.20.0,<3.0",
    ],
    zip_safe=False,
    keywords=["teltonika", "rutos"],
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)
