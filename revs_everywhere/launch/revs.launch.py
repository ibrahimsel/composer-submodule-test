from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Agent
    node_agent = Node(
        name="revs_everywhere",
        package="revs_everywhere",
        executable="revs_everywere",
    )
    ld = LaunchDescription()
    ld.add_action(node_agent)
    return ld
