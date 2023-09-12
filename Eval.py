#Angel Vargas
#CPSC 46000 Term Project - GeoJSON Visualizer
#Evaluates the tree and creates the specified features.
import Features
geometries = ["point", "linestring", "polygon"]     #list of possible geometries

def eval(tree):
    if tree.getValue().type == "VALUE":    
        if tree.getValue().value == "featurecollection":
            featureCollection = Features.FeatureCollection()
            features = eval(tree.getChildren()[0])
            featureCollection.setFeatures(features)
            featureCollection.show()        #end of file
        elif tree.getValue().value == "feature":       
            feature = eval(tree.getChildren()[0])   #will receive a feature
            return feature
        elif tree.getValue().value in geometries:   #valid feature
            geometry = tree.getValue().value
            coordinates = eval(tree.getChildren()[0])
            feature = Features.Feature(geometry, coordinates)
            return feature
        else:   #invalid feature, must be a property
            return tree.getValue().value
    elif tree.getValue().type == "ID":
        if tree.getValue().value == "type:":
            value = eval(tree.getChildren()[0])
            return value
        elif tree.getValue().value == "features:":
            features = []
            for node in tree.getChildren():
                features.append(eval(node))         #will include all the features for the collection
            return features
        elif tree.getValue().value == "geometry:":
            feature = eval(tree.getChildren()[0])       #geometry type
            properties = eval(tree.getChildren()[1])    #geometry properties
            feature.setProperties(properties)
            return feature
        elif tree.getValue().value == "coordinates:":
            coordinates = []
            i = 0
            while i < len(tree.getChildren()) :
                coordinates.append([float(tree.getChildren()[i].getValue().value), float(tree.getChildren()[i + 1].getValue().value)])
                i += 2
            return coordinates
        elif tree.getValue().value == "properties:":
            properties = eval(tree.getChildren()[0])
            return properties
        else:   #must be a key for the properties
            value = eval(tree.getChildren()[0])
            key = tree.getValue().value
            return {key : value}    #returns dictionary entry for properties