from setuptools import setup

package_name = 'proj_bixos'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/launch',
            ['launch/all_nodes_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='Package that handles image publishing, accel publishing, and overlay',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cam_collection_node = proj_bixos.cam_collection_node:main',  # Nome correto do nó
            'data_collection_node = proj_bixos.data_collection_node:main',
            'overlay_test = proj_bixos.overlay_test:main',
        ],
    },
)
