from setuptools import setup

setup(name='SE Plagiarism Control Panel',
      version='0.0.1',
      description='A basic control panel utilized to monitor checks of SE Tag Wikis',
      author='Andy Wegner',
      author_email='se-andy@syntaxtechnology.com',
      url='',
     install_requires=['Flask>=0.10.1', 'pandas>=0.17.1', 'simplejson==3.8.1', 'beautifulsoup4==4.4.0'
	 'sqlalchemy==1.0.9','pymysql==0.6.7','flask-sqlalchemy==2.1'],
     )
