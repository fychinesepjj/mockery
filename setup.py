# -*- coding: utf-8 -*-
import os
import sys
from distutils.sysconfig import get_python_lib
try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

# Avoid duplication of installation of Mockery by python setup.py install 
overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        lib_abs_path = os.path.abspath(lib_path)
        for name in os.listdir(lib_abs_path):
            find_path = os.path.abspath(os.path.join(lib_abs_path, name))
            if os.path.isdir(find_path) and name.lower().startswith('mockery'):
                existing_path = find_path
                overlay_warning = True
                break


EXCLUDE_FROM_PACKAGES = []

version = __import__('mockery').VERSION

if overlay_warning:
    sys.stderr.write("""

========
WARNING!
========

You have just installed Mockery over top of an existing
installation, without removing it first. Because of this,
your install may now include extraneous files from a
previous version that have since been removed from
Mockery. This is known to cause a variety of problems. You
should manually remove the

%(existing_path)s

directory and re-install Mockery.

""" % {"existing_path": existing_path})

else:
    setup(
        name='Mockery',
        version=version,
        url='https://github.com/fychinesepjj',
        author='jjpan',
        author_email='fychinesepjj@126.com',
        description=('Mockery is one of the methods of Black-box Testing designed for api test'),
        packages = find_packages(exclude=EXCLUDE_FROM_PACKAGES),
        include_package_data=True,
        scripts = ['mockery/bin/mockery-manager.py'],
        install_requires = [  # 安装依赖的其他包
            'requests>=2.10.0',
            'termcolor>=1.1.0',
            'cookiecutter>=1.4.0'
        ],
        entry_points={'console_scripts': [
            'mockery = mockery.management:execute_from_command_line',
        ]},
        zip_safe=False
    )