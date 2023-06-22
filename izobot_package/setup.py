from setuptools import setup

package_name = 'izobot_package'

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
    maintainer='ozgur',
    maintainer_email='oozgurgucer@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "cmd_vel_subscriber = izobot_package.cmd_vel_subscriber:main",
            "image_processor_pub = izobot_package.ImageProcessorPub:main",
            "lead_to_cbs_sub_node = izobot_package.LeadToCBSSubscriber:main",
            "autonomous_move_node = izobot_package.autonomous_move_node:main",
            "display_video_node=izobot_package.display_video_node:main",
            "display_detected_stream_node=izobot_package.display_detected_stream_node:main"
        ],
    },
)
