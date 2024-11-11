from setuptools import find_packages, setup

package_name = 'revs_everywhere'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sel',
    maintainer_email='ibrahim.sel@eteration.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'revs_everywere = revs_everywhere.revs_everywere:main'
        ],
    },
)
