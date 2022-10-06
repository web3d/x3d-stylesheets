# NumpyExample.py

"""
Script to demonstrate setting the values of the coordinates, colors (by vertex), and index arrays defining
an IndexedTriangleSet from data values in numpy arrays.

Tested Feb 24 2022 with x3d version 4.0.51   installed with pip

Vince Marchetti 24 Feb 2022
license : https://creativecommons.org/licenses/by/4.0/
"""
from x3d import *
import numpy as np

def colored_tetrahedron( radius ):
    """
    returns (3,) tuple of numpy arrays
    points_coordinate : a (N,3) array of vertex coordinates
    points_colors : (N,3) array of colors
    face_indices : (K,3) array of integer indices into points_* arrays
    
    where N = number of vertices in mesh (N=4 for this tetrahedron)
          K = number of triangle faces in mesh (K=5 for tetrahedron)
          
    defines a mesh for a tetrahedron inscribed in sphere of with radius specified by argument
    centered at origin
    """
    point_coordinates = np.array([
        ( 0.000,  1.000,   0.000),
        (-0.816, -0.344,   0.471),
        ( 0.816, -0.344,   0.471),
        ( 0.000, -0.344,  -0.942),
    ]) * radius
    
    point_colors = np.array([
        (1.00,1.00,0.40),
        (0.70,0.40,1.00),
        (0.00,0.80,0.00),
        (1.00,0.80,0.90),
    ])
    face_indices = np.array([
        (0,1,2),
        (0,2,3),
        (0,3,1),
        (3,2,1)
    ])
    
    return point_coordinates,point_colors,face_indices
    
    
point_coordinates,point_colors,face_indices = colored_tetrahedron( 2.0 )


newModel=X3D(profile='Immersive',version='3.3',
  head=head(
    children=[
    meta(content='NumpyExample.x3d',name='title'),
    meta(content='example of using Numpy library to generate coordinate geometry and color',name='description'),
    meta(content='24 Feb 2022',name='created'),
    meta(content='Vince Marchetti',name='creator'),
    meta(content='https://www.web3d.org/x3d/content/examples/license.html',name='license')
  ]),
  Scene=Scene(
    
    children=[
    WorldInfo(title='NumpyExample.x3d'),
    Viewpoint(DEF='ViewUpClose', description='Initial Viewpoint'),

    Shape(geometry=IndexedTriangleSet(
                # following code converts rank-2 numpy array of integers into a python list for setting value of index field
                index = list( face_indices.flatten() ),
                
                # following code converts rank-2 numpy array of float values into a Python list of Python tuples of floats
                # to set x3d values of type MFVec3f and MFColor
                coord = Coordinate( point = [ tuple(pt) for pt in point_coordinates] ),
                color = Color( color = [tuple(c) for c in point_colors])
                )
          )
    ])
) 


newModelXML= newModel.XML() 
print(newModelXML) 
