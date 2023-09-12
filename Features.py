#Angel Vargas
#CPSC 46000 Term Project - GeoJSON Visualizer
#Creates and plots the geometries, Only allows for the primitive geometries.
import numpy as np
import matplotlib.pyplot as plt

class FeatureCollection:
    def __init__(self):
        self.features = [] #empty list of for features it will contain
    def getFeatures(self):
        return self.features
    def setFeatures(self, features):
        self.features = features
    def appendFeature(self, feature):
        self.features.append(feature)
    def show(self):
        plt.show()    # displays the features in that FeatureCollection

class Feature:
    def __init__(self, type, coord):
        self.properties = {}    #empty dictionary for properties
        
        if type == "point":     #creates new geometry based on the type
            self.type = Point(coord)
        elif type == "linestring": 
            self.type = LineString(coord)
        elif type == "polygon":
            self.type = Polygon(coord)
    
    def setProperties(self, properties):
        self.properties.update(properties)
    
    def getProperties(self):
        return self.properties
    
    
class Point:
    def __init__(self, coord):
        self.x = coord[0][0]
        self.y = coord[0][1]

        plt.plot(self.x, self.y, "o")      #plots x and y

class LineString:
    def __init__(self, coord):
        self.coord = np.array(coord)

        x, y = self.coord.T
        plt.plot(x, y)         #plots every x and y from the array

class Polygon:
    def __init__(self, coord):
        self.coord = np.array(coord)

        x, y = self.coord.T
        plt.plot(x, y)          #same idea as LineString except last point connects