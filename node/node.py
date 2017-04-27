class Node:
    def __init__(self, node_type, port):
        self.node_type = node_type
        self.port = port

        if node_type == 'node':
            self._node(self.port)
        elif node_type == 'ch':
            self.clusterhead(self.port)
        elif node_type == 'sink':
            self.sink(self.port)


    # Function to act as
    def _node(self, port):
        pass

    def sink(self, port):
        pass

    def clusterhead(self, port):
        pass

