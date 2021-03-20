

class KMeans(object):

    def __init__(self, data):
        self.data = data

    def initialize(self, data, k):
        import random 
        centroids = []
        for _ in range(k):
            i = random.randint(0, len(data)-1)
            centroids.append(data[i])
        return centroids


    def fit(self, k=2):

        # k = 3
        centroids = self.initialize(self.data, k)

        # print ("inital", centroids)

        centroids = [[-2,3], [6, 1], [2, 7]]

        print (self.data)
        print ("inital", centroids)

        update, iteration = True, 0
        while update and iteration <= 10:

            labels = self.assign_labels(centroids)
            print (labels)
            # exit(0)
            new_centroids = self.update_centroids(labels)
            print (iteration, centroids, new_centroids)
            update = self.ifStop(centroids, new_centroids)

            centroids[:] = new_centroids[:]

            # if update:
            #     for i in range(len(centroids)):
            #         for j in range(len(centroids[0])):
            #             centroids[i][j] += 0.1*(new_centroids[i][j]-centroids[i][j])

            # print (centroids)

            print ()
            iteration += 1
            print ('-------------')

        print (centroids, labels)

    def update_centroids(self, labels):
        f = len(self.data[0])
        n_data_class = {}

        new_centroids = {}
        for i in range(len(self.data)):
            c = labels[i]
            n_data_class[c] = n_data_class.get(c, 0) + 1
            if c not in new_centroids:
                new_centroids[c] = [0]*f

            for j in range(f):
                new_centroids[c][j] += self.data[i][j]

        for c in range(len(new_centroids)):
            for j in range(f):
                new_centroids[c][j] = float(new_centroids[c][j])/n_data_class[c]

        return [new_centroids[c] for c in new_centroids]



    def ifStop(self, centroids, new_centroids, epsilon = 0.01):
        for i in range(len(centroids)):
            for j in range(len(centroids[0])):
                if abs(centroids[i][j]-new_centroids[i][j]) >= epsilon:
                    return True
        return False

    def assign_labels(self, centroids):
        labels = []
        for i in range(len(self.data)):

            min_dist, c = self.get_distance(self.data[i], centroids[0]), 0
            for k in range(1, len(centroids)):
                dist = self.get_distance(self.data[i], centroids[k])
                if dist < min_dist:
                    min_dist, c = dist, k
            labels.append(c)

        return labels

    def get_distance(self, point1, point2):
        return sum([(point1[i]-point2[i])**2 for i in range(len(point1))])




data = [[1, 1], [0, 3], [6, 0], [7, 4], [0.5, -1], [6.5, 2], [3, 10], [3.5, 11]]
obj = KMeans(data)
obj.fit(k=3)