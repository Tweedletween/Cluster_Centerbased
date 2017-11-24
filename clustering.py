import attributes
from evaluation import hamming_distance
from evaluation import classification_error_distance


class Cluster(object):
    # Represents a cluster

    def __init__(self, clustering_data):
        self.clustering_data = clustering_data
        self.examples_index = []
        self.center = clustering_data[0]
        return

    def set_center(self, center):
        self.center = center

    def get_center(self):
        return self.center

    def append(self, index):
        assert isinstance(index, int), "Not an index"
        self.examples_index.append(index)

    def get_examples_index(self):
        return self.examples_index

    def get_examples(self):
        examples = []
        for index in self.examples_index:
            examples.append(self.clustering_data[index])
        return examples

    def clean_up(self):
        self.examples_index = []
        self.center = None

    def get_stat(self, label):
        stat = {name: 0 for name in label.values}
        for index in self.examples_index:
            example = self.clustering_data[index]
            name = example.get_value(label)
            stat[name] = stat[name] + 1
        return stat


class Clustering(object):
    # Represents a clustering algorithm

    def __init__(self, clustering_data, attribute_set, label, k):
        self.clustering_data = clustering_data
        self.attribute_set = attribute_set
        self.label = label
        self.k = k
        self.clusters = [Cluster(clustering_data) for _ in range(k)]

        #self.do_clustering()
        return

    def do_clustering(self):
        return

    def get_clusters_stat(self):
        return [cluster.get_stat(self.label) for cluster in self.clusters]

    def test(self, label):
        return 0.0

    def dump(self):
        print("Clustering result: ")
        for i, cluster in enumerate(self.clusters):
            print(cluster.get_examples_index())
        print("Hamming distance to ref: ")
        print(hamming_distance(self.clustering_data, self.clusters, self.label, self.k))

        print("Miss classification error: ")
        print(classification_error_distance(self.get_clusters_stat(), self.label, len(self.clustering_data)))
        return ""
