from setuptools import setup

package_name = 'py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='patcharapon',
    maintainer_email='patcharapon@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [

            "py_node = py_pkg.first_node:main",
            "robot_new_station = py_pkg.robot_new_station:main",
            "smartphone = py_pkg.smartphone:main",
            "add_two_ints_server = py_pkg.add_two_ints_server:main",
            "client = py_pkg.client:main",
            "client_oop = py_pkg.client_oop:main",
            "hw_status_publisher = py_pkg.hw_status_publisher:main",
            "led_panel = py_pkg.led_panel:main"

        ],
    },
)
