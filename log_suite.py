import unittest
from tests.login_page_tests import LoginNegative, LoginPositive
from tests.forgot_password_page_tests import ForgotPasswordTests

log_suite_tests = unittest.TestSuite()

'''Positive test cases of login page'''
'''Test Case ID - 300'''
log_suite_tests.addTest(LoginPositive('test_correct_email_and_password_entered_by_existing_user'))
'''Test Case ID - 301'''
log_suite_tests.addTest(LoginPositive('test_forgot_password_link'))

'''Negative test cases of login page'''
'''Test Case ID - 302'''
log_suite_tests.addTest(LoginNegative('test_no_email_entered_by_existing_user'))
'''Test Case ID - 303'''
log_suite_tests.addTest(LoginNegative('test_invalid_email_entered_by_existing_user'))
'''Test Case ID - 304'''
log_suite_tests.addTest(LoginNegative('test_no_password_entered_by_existing_user'))
'''Test Case ID - 305'''
log_suite_tests.addTest(LoginNegative('test_invalid_password_entered_by_existing_user'))
'''Test Case ID - 306'''
log_suite_tests.addTest(LoginNegative('test_no_email_and_password_entered'))
'''Test Case ID - 307'''
log_suite_tests.addTest(LoginNegative('test_no_existing_user_log_in'))

'''Positive tests cases of forgot password page'''
'''Test Case ID - 308'''
log_suite_tests.addTest(ForgotPasswordTests('test_enter_email_of_existing_user'))

'''Negative test cases of forgot password page'''
'''Test Case ID - 309'''
log_suite_tests.addTest(ForgotPasswordTests('test_enter_email_of_no_existing_user'))
'''Test Case ID - 310'''
log_suite_tests.addTest(ForgotPasswordTests('test_empty_field_email'))
'''Test Case ID - 311'''
log_suite_tests.addTest(ForgotPasswordTests('test_incorrect_email_format'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(log_suite_tests)