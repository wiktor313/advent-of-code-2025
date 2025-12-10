# https://adventofcode.com/2025/day/8#part1
import math

#with open('Day8\\Resources\\Sample.csv', 'r') as file:
with open('Day8\\Resources\\Input.csv', 'r') as file:
    coordinates = []
    for line in file:
        x, y, z = map(int, line.strip().split(','))
        coordinates.append((x, y, z))


def euclidean_distance(v1, v2):
    return math.sqrt((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2 + (v2[2] - v1[2])**2)


class UnionFind:
    """Union-Find structure to track circuits (connected components)"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        
        return True
    
    def get_circuit_sizes(self):
        """Returns sizes of all circuits"""
        circuits = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in circuits:
                circuits[root] = 0
            circuits[root] += 1
        return list(circuits.values())


def get_all_pairs_with_distances(coordinates):
    """Returns all pairs with their distances, sorted by distance"""
    pairs = []
    
    for i, coord1 in enumerate(coordinates):
        for j, coord2 in enumerate(coordinates[i+1:], start=i+1):
            distance = euclidean_distance(coord1, coord2)
            pairs.append((distance, i, j))
    
    pairs.sort()
    return pairs


all_pairs = get_all_pairs_with_distances(coordinates)

uf = UnionFind(len(coordinates))

last_connection = None

for i, (dist, idx1, idx2) in enumerate(all_pairs):
    if uf.union(idx1, idx2):
        circuit_sizes = uf.get_circuit_sizes()
        
        if len(circuit_sizes) == 1:
            last_connection = (idx1, idx2)
            break

if last_connection:
    idx1, idx2 = last_connection
    x1 = coordinates[idx1][0]
    x2 = coordinates[idx2][0]
    result = x1 * x2
    print(f"Answer: {result}")
else:
    print("\nCould not connect all junction boxes into a single circuit!")