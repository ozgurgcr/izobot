from setuptools import setup

package_name = 'izobot_v1'

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
    maintainer='rpi',
    maintainer_email='oozgurgucer@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "cb_detector_node = izobot_v1.cb_detector_node:main",
            "my_camera_node = izobot_v1.my_camera_node:main",
            "cb_detector_nodev2 = izobot_v1.cb_detector_nodev2:main",
            "cb_detector_nodev3 = izobot_v1.cb_detector_nodev3:main",
            "cb_detector_nodev4 = izobot_v1.cb_detector_nodev4:main",
            "cb_detector_nodev5 = izobot_v1.cb_detector_nodev5:main",
            "cmd_vel_subscriber = izobot_v1.cmd_vel_subscriber:main",
            "robot_controller_node = izobot_v1.robot_controller_node:main"

        ],
    },
)
