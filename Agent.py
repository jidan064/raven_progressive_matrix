# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image
#import numpy

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    def get_object_diff(self, object1, object2):
        final_diff = 0
        action = []
        for attributeName in object1.attributes:
            if attributeName not in object2.attributes:
                final_diff += 8
                action.append("deleted")
                continue
            if object1.attributes[attributeName] != object2.attributes[attributeName]:
                if attributeName == 'size': # scaled
                    final_diff += 1
                    action.append('scaled')
                elif attributeName == 'shape':
                    final_diff += 8
                    action.append('reshaped')
                elif attributeName == 'angle': # rotated
                    final_diff += 2
                    action.append('rotated')

        return final_diff, action

    def get_matching_map(self, figure1, figure2):
        matching_map = []
        for objectName1 in figure1.objects:
            object1 = figure1.objects[objectName1]
            matching_object_name = ''
            min_diff = 100
            final_action = []
            for objectName2 in figure2.objects:
                object2 = figure2.objects[objectName2]
                diff, action = self.get_object_diff(object1, object2)
                if diff < min_diff:
                    matching_object_name = objectName2
                    min_diff = diff
                    final_action = action
            matching_map.append(min_diff)
        return matching_map

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        if problem.problemType == '2x2':
            figureA = problem.figures['A']
            figureB = problem.figures['B']
            matching_map_AB = self.get_matching_map(figureA, figureB)
            matching_map_AB.sort()
            figureC = problem.figures['C']
            for figureName in problem.figures:
                if figureName != 'A' and figureName != 'B' and figureName != 'C':
                    figure = problem.figures[figureName]
                    diff_map = self.get_matching_map(figureC, figure)
                    diff_map.sort()
                    if matching_map_AB == diff_map:
                        print(figureName)
                        return int(figureName)
        return -1