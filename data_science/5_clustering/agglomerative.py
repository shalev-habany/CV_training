class SegmentedAgglomerativeImage:
    def __init__(self, img, dist_matrix, n_clusters):
        self.img = img
        self.dist_matrix = dist_matrix
        self.n_clusters = n_clusters
        
    