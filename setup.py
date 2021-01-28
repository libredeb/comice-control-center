import glob
from setuptools import setup, find_packages
from comicecontrolcenter import __version__

setup(
    name='comice-control-center',
    version=__version__,
    description='A simply control center to monitor connections, monitor brightness and sound volume',
    author='Juan Lozano',
    author_email='libredeb@gmail.com',
    scripts=['comice-control-center'],
    data_files=[
        ('share/pixmaps/', ['icons/ccc.svg']),
        ('share/pixmaps/', ['icons/ccc-dark.svg']),
    ],
    python_requires='>=3.6',
    license='GNU GPL',
    platforms='linux',
)
