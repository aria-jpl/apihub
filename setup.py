from setuptools import setup, find_packages
import apihub

setup(
    name='apihub',
    version=apihub.__version__,
    long_description=apihub.__description__,
    url=apihub.__url__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'qquery>=0.0.1',
        'shapely'
    ]
)
