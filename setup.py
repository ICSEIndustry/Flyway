from distutils.core import setup

setup(name='flyway',
      version='0.1',
      description='Tool to migrate resources between multiple clouds',
      url='https://github.com/OpenAcademy-OpenStack/Flyway',
      packages=[
            'flyway'
      ],
      install_requires = [
		'taskflow>=0.1.3',
		'mysql-connector-python==1.1.5',
		'python-cinderclient==1.0.8',
		'python-glanceclient==0.12.0',
		'python-keystoneclient==0.6.0',
		'python-neutronclient==2.3.4',
		'python-novaclient==2.15.0',
		'python-swiftclient==2.0.2',
		'requests==2.2.1',
		'Fabric==1.8.2',
		'kombu==3.0.12',
		'oslo.config==1.2.1'
      ]
)
