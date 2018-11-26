"""
Setup Module to setup Python Handlers (Git Handlers) for the Git Plugin.
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='kyso_jupyterlab',
    version='0.4.4',
    author='Git Intern Team, Noah Stapp, Jenna Landy, Alena Mueller',
    description="A server extension for JupyterLab's git extension",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
        'psutil'
    ],
    package_data={'kyso_jupyterlab': ['*']},
)
