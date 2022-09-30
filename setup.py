from setuptools import find_packages, setup

setup(
    name='images4web',
    packages=find_packages(include=['images4web']),
    version='0.1.0',
    description='From a input folder containing images, it compress images for the web: it creates (and sycronize continuously) an output folder with the compressed images',
    author='Me',
    license='MIT',
    install_requires=['Pillow==9.2.0'],
)