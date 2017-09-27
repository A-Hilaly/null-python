import os

NULL_DIRECTORY = os.path.abspath(os.path.dirname(__file__))[:-len(__file__) - 1]
NULL_TESTS_MAIN_EXC = '{0}/tests/test_null.py'

def run_tests():
    os.system('chmod +x {0}'.format(NULL_TESTS_MAIN_EXC))
    os.system(NULL_TESTS_MAIN_EXC)
