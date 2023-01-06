from setuptools import setup

setup(
    name='clean_folder',
    version='1.0.8',
    description='File sorting script',
    url='https://github.com/Mashimur/hw_python_core',
    author='Maria Palona',
    author_email='marjapalenaja90@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)
