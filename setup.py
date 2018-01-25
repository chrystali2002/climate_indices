from setuptools import setup

setup(
    name='indices_python',
    version='0.1.0',
    url='https://github.com/monocongo/indices_python',
    license='GPL 2.0',
    author='James Adams',
    author_email='james.adams@noaa.gov',
    description=('Community reference implementations of climate indices '
                 'algorithms in Python. Including Palmers (PDSI, scPDSI,  '
                 'PHDI, and Z-Index), SPI, SPEI, PET, and PNP.'),
    packages=['indices_python'],
    install_requires=[
        "numpy",
        "numba",
        "pycurl",
        "pandas",
        "scipy",
        "netcdf4",
    ],
    tests_require=[
        "nose",
    ],
    test_suite='tests',
    keywords=('indices climate climate_indices drought drought_indices pdsi '
              'spi spei evapotranspiration'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: Physics',
    ],
)
