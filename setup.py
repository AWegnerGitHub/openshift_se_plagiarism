from setuptools import setup
import sys

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name='SE Plagiarism Control Panel',
      version='0.0.1',
      description='A basic control panel utilized to monitor checks of SE Tag Wikis',
      author='Andy Wegner',
      author_email='se-andy@syntaxtechnology.com',
      url='',
     install_requires=['Flask>=0.10.1', 'pandas>=0.17.1', 'simplejson==3.8.1', 'beautifulsoup4==4.4.0',
	 'sqlalchemy==1.0.9','pymysql==0.6.7','flask-sqlalchemy==2.1','pytest>=2.8.0','hypothesis==1.9.0',
	 'pytest-runner==2.6.2', 'flask-migrate>=1.6.0'],
	 setup_requires=[] + pytest_runner,
	 tests_require=['pytest']
     )
