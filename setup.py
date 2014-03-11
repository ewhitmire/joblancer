from setuptools import setup

import os

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.
packages = ['Django<=1.6',
                  'CherryPy', # If you want serve Django through CherryPy
                  'static3',  # If you want serve the static files in the same server
                  'south',
                  'django-autoslug',
                  'Pillow',
                  'django-allauth'
                   #  'mysql-connector-python',
                   #  'pymongo',
                   #  'psycopg2',
      ]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='Connector', version='0.1',
      description='OpenShift Python-3.3 / Django-1.6 Community Cartridge based application',
      author='Eric Whitmire and Michelle Hall', author_email='ewhitmire@outlook.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
     )
