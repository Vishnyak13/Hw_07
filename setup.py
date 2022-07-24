from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1.0',
    description='Hw07 Clean_folder',
    author='Eugene Vyshnytsky',
    author_email='evgeniy.vishn@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
)
