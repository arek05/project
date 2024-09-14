import unittest
from tests.registration_page_tests import RegistrationPositiveTest, RegistrationNegativeTest

register_suite_tests = unittest.TestSuite()

'''Positive test cases of registration new user page'''
'''Test Case ID - 200'''
register_suite_tests.addTest(RegistrationPositiveTest('test_register_new_user_succes'))

'''Negative test cases of registration new user page'''
'''Test Case ID - 201'''
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_all_fields'))
'''Test Case ID - 202'''
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_field_name'))
'''Test Case ID - 203'''
register_suite_tests.addTest((RegistrationNegativeTest('test_register_new_user_with_empty_field_surname')))
'''Test Case ID - 204'''
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_field_email'))
'''Test Case ID - 205'''
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_field_password'))
'''Test Case ID - 206'''
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_field_confirm_password'))
'''Test Case ID - 207'''
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_too_short_password'))
'''Test Case ID - 208'''
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_incorrect_password_confirmation'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(register_suite_tests)