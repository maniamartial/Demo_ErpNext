from .fs import print_contents_of_cwd, process_api_data, ServiceChecker
from unittest import TestCase, mock
from unittest.mock import patch


# class TestExamples(TestCase):
    
#     @mock.patch('demo_app.demo_app.doctype.driver1.fs.check_output', return_value=b'kayes')
#     def test_print_contents_of_cwd(self, mock_check_output):
#         actual_result=print_contents_of_cwd()
        
#         expected_directory=b'kayes'
#         self.assertIn(expected_directory, actual_result)
    
    
class TestExamples(TestCase):
    def setUp(self):
        self.patcher=mock.patch('demo_app.demo_app.doctype.driver1.fs.check_output', return_value=b'kayes')
        self.patcher.start()
        
    def tearDown(self):
        self.patcher.stop()
        
    def test_print_contents_of_cwd(self):
        actual_result=print_contents_of_cwd()
        
        expected_directory=b'kayes'
        self.assertIn(expected_directory, actual_result)
        
    @patch('requests.get')
    def test_process_data(self, mock_get):
        mock_get.return_value.json.return_value={'current_user_url':'https://api.github.com/user'}
        actual_result=process_api_data()
        
        expected_result='https://api.github.com/user'
        self.assertEqual(expected_result, actual_result)
        
    @patch('demo_app.demo_app.doctype.driver1.fs.ExternalService')
    def test_service_checker(self, mock_external_service):
        mock_external_service.return_value.get_status.return_value='OK'
        service_checker=ServiceChecker()
        result=service_checker.check_service_status()
        self.assertTrue(result, 'Service is not OK')