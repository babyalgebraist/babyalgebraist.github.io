# python3

import sys
import os
import threading
from collections import namedtuple

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
        def read_examples(self):

        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
        
        def read_solutions(self):
                self.path = sys.stdin.readline()
                self.dir_list = os.listdir(self.path)
        # print("The Files at {} are \n: {}".format(path, dir_list))
        
                results_files = [filename for filename in self.dir_list if filename.endswith('.a')]
                results_files.sort()

                std_results = []
                for filename in results_files:
                        with open(os.path.join(path, filename), 'r') as file:
                                # print("Now Processing file {}".format(filename))
                                expected = int(file.readline())
                                std_results.append(expected)
                        # print("Standard results now stored as: \n {}".format(std_results))
                print(len(std_results))
        return std_results                         
        # except:
        #         print("Just got an error. Not quite sure what.")
        def read_tests(path):
                 """
                Returns a tuple of (n, parents): the number of entries in the list of 'parent' nodes.
                """

                dir_list = os.listdir(path)
                # print("The Files at {} are \n: {}".format(path, dir_list))
                
                test_files = [filename for filename in dir_list if not filename.endswith('.a')]
                test_files.sort()

                tests = []
                for filename in test_files:
                        with open(os.path.join(path, filename), 'r') as file:
                                # print("Now Processing file {}".format(filename))
                                n = int(file.readline())
                                parents = list(
                                        map(int, file.readline().split()))
                                tests.append((n, parents))
                        # print("Tests are now stored as: \n {}".format(tests))
                print(len(tests))
                return tests
                # except:
                #         print("Just got an error. Not quite sure what.")
                
        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)
                return maxHeight

# end class





def run_tests(path_to_tests):
        tests = read_tests(path_to_tests)
        solutions = read_solutions(path_to_tests)

        assert len(tests) == len(solutions)

        for i, example in enumerate(tests):
                print("Now testing: \nn = {}\n parents = {}\n".format(n, example))
                tree = TreeHeight()
                tree.read_examples()
                result = tree.compute_height()
                
                if result == solutions[i]:
                        print('Ok')
                else:
                        print("Value mismatch:\n")
                        print("Standard Result: \n{}\n".format(solutions[i]))
                        print("Computed Result: \n{}\n".format(result))
                        break
     


def main():
        # tree=TreeHeight()
#   tree.read()
#   print(tree.compute_height())
# Testing
        path_to_files = 'psets/wk1/tree_height/tests'
        run_tests(path_to_files)
        

threading.Thread(target = main).start()
