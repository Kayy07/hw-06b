# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(5,5,8),'Isoceles','5,5,8 should be isosceles')
    
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 should be scalene')
    
    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 should be invalid')
    
    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 should be invalid')
    
    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle(-1,-2,-3),'InvalidInput','-1,-2,-3 should be invalid')
    
    def testInvalidTriangleD(self):
        self.assertEqual(classifyTriangle(1,1,3),'InvalidInput','1,1,3 should be invalid')

    def testInvalidTriangleE(self):
        self.assertEqual(classifyTriangle(210, 200, 110),'InvalidInput','210,200,110 should be invalid')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

