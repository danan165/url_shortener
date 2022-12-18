from setuptools import setup

setup(
    name='url_shortener',
    packages=['url_shortener'],
    include_package_data=True,
    install_requires=[
        "Flask==2.2.2",
    ],
)