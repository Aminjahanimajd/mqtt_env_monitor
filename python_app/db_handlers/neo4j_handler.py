from py2neo import Graph, Node, Relationship

graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))  # replace with your password

def store_device_graph(device_id, network_id):
    device = Node("Device", id=device_id)
    network = Node("Network", id=network_id)
    rel = Relationship(device, "BELONGS_TO", network)
    graph.merge(device, "Device", "id")
    graph.merge(network, "Network", "id")
    graph.merge(rel)
    print(f"Stored device {device_id} in Neo4j")
