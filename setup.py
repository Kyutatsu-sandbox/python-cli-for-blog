from setuptools import setup


setup(
        name='python-cli-tool-template',
        version='1.1.0',
        install_requires=['termcolor>=1.1.0'],
        py_modules = ['cli'],
        entry_points={
            "console_scripts": ['mycli = cli:main', 'mycli_color = cli:color']
        }
)

