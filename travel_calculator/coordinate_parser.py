from math import sqrt


class CoordinateParser:
    def __init__(self, geo_coordinates: list):
        self.geo_coordinates = geo_coordinates
        self.matrix = [[None for _ in range(len(geo_coordinates))] for _ in range(len(geo_coordinates))]

    def get_distances(self) -> list:
        for i in range(len(self.matrix)):
            for j in range(i, len(self.matrix[0])):
                if i == j:
                    self.matrix[i][j] = 0
                else:
                    distance = self._formula(self.geo_coordinates[i], self.geo_coordinates[j])
                    self.matrix[i][j] = distance
                    self.matrix[j][i] = distance

        return self.matrix

    def _formula(self, from_point: list, to_point: list):
        return sqrt((from_point[0] - to_point[0]) ** 2 + (from_point[1] - to_point[1]) ** 2)
