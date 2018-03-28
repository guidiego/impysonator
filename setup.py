
from setuptools import setup

setup(
    name='impysonator',
    version='0.1',
    description='Seja Impessoal!',
    url='http://github.com/guidiego/impysonator',
    author='Guiherme Diego',
    author_email='guilherme.albino.francisco@gmail.com',
    license='MIT',
    packages=['impysonator'],
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
    }
)