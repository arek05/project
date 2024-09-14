
import unittest
from tests.home_page_tests import HomePageTest

navigation_test_suite = unittest.TestSuite()

'''Test Case ID - 100'''
navigation_test_suite.addTest(HomePageTest('test_home_page_loaded_correctly'))
'''Test Case ID - 101'''
navigation_test_suite.addTest(HomePageTest('test_open_login_page'))
'''Test Case ID - 102'''
navigation_test_suite.addTest(HomePageTest('test_open_register_page'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(navigation_test_suite)