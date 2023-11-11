from setuptools import find_packages, setup

package_name = 'drone_test'

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
    maintainer='vagrant',
    maintainer_email='vagrant@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = drone_test.comandos_test:main',
                'listener = drone_test.listener_test:main',
                'listener_comandos = drone_test.listenerComandos:main',
                'listener_swarm = drone_test.listener_drone_swarm:main',
        ],
},
)
