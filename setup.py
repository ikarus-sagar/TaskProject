from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='flowci',
    version='1.0.0',
    author='Sagar Gupta',
    author_email='Sagar@email.com',
    description='Test Task Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ikarus-sagar/taskproject',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'flowci=main:main',
        ],
    },
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
)
