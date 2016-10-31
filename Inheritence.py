class Enge(object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    des __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return Edge.__str__(self) + " (" + str(self.weight) + ")"
