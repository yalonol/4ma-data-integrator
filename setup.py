from setuptools import setup

with open('VERSION', 'r') as version_file:
    version = version_file.read().strip()

setup(name='4ma-dict-model',
      version=version,
      author='Yalon Fishbein',
      author_email='yalon@4m-a.com',
      description='Model for filters layers and groups them by category and subcategory based on regex dictionary',
      url='https://github.com/4ma/4ma-layer-filter',
      python_requires = ">=3.8",
      include_package_data=True,
      packages=[TODO: 'dict_model_utils',
                TODO: 'example',
                TODO: 'dict_model_utils.utils',
                TODO: 'dict_model_utils.helpers'],
      install_requires=[
            TODO: 'boto3==1.23.7',
            TODO: 'botocore==1.26.7',
      ]
 )
