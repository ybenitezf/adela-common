from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='adelacommon',
    version='0.0.2',
    url='https://github.com/ybenitezf/adela-common',
    license='GPL',
    author='Yoel Benítez Fonseca',
    author_email='ybenitezf@gmail.com',
    description='Modulos y librerias comunes para aldenate.cu',
    long_description=read('README.md'),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        "Flask>=0.8",
        "Flask-Migrate"
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest', 
        'pytest-cov'
    ],
    classifiers=[
        'Environment :: Web Environment', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent', 
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
