from py2neo import Graph, Node, Relationship

graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

def store_device_graph(device_id, network_id):
    device = Node("Device", id=device_id)
    network = Node("Network", id=network_id)
    graph.merge(device, "Device", "id")
    graph.merge(network, "Network", "id")
    graph.merge(Relationship(device, "CONNECTED_TO", network))
    print(f"Stored device {device_id} in Neo4j")
