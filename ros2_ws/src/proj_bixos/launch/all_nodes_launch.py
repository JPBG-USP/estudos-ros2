from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='proj_bixos',
            executable='cam_collection_node',  # Nome correto do nó
            name='cam_collection_node',
            output='screen',
            parameters=[],
            remappings=[]
        ),
        Node(
            package='proj_bixos',
            executable='data_collection_node',
            name='data_collection_node',
            output='screen',
            parameters=[],
            remappings=[]
        ),
        Node(
            package='proj_bixos',
            executable='overlay_test',
            name='overlay_test',
            output='screen',
            parameters=[],
            remappings=[]
        ),
    ])
