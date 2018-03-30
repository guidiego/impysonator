
from setuptools import setup, find_packages

setup(
    name='impysonator',
    version='0.1.3',
    description='Seja Impessoal!',
    url='http://github.com/guidiego/impysonator',
    author='Guiherme Diego',
    author_email='guilherme.albino.francisco@gmail.com',
    license='MIT',
    packages=find_packages(exclude=["*.tests"]),
    zip_safe=False,
    keywords='python impessoal paper artigo revisão review',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points={
        'console_scripts': [
            'impysonator=impysonator:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/guidiego/impysonator/issues',
        'Source': 'https://github.com/guidiego/impysonator/'
    }
)