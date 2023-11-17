import unittest
import requests
from unittest.mock import patch, Mock, ANY

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server, smtp_port, from_addr, to_addr, subject, body):
    msg=MIMEMultipart()
    msg['From']=from_addr
    msg['To']=to_addr
    msg['Subject']=subject
    msg.attach(MIMEText(body, 'plain'))
    
    server=smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_addr, "MyPassword")
    text=msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()
    
    
class TestEmail(unittest.TestCase):
    
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        instance=mock_smtp.return_value
        
        send_email("smtp.gmail.com", 587, "martialmania@gmail.com", "josephmania@gmail.com","Subject", "Email Content")
        mock_smtp.assert_called_with('smtp.gmail.com', 587)
        instance.starttls.assert_called()
        instance.login.assert_called_with("martialmania@gmail.com", "MyPassword")
        instance.sendmail.assert_called_with("martialmania@gmail.com", "josephmania@gmail.com",ANY)
        instance.quit.assert_called()
    
    
if __name__=="__main__":
    unittest.main()


'''Mocking the external apis'''
# def get_user_data(user_id):
#     response=requests.get("https://api.github.com/users/{user_id}".format(user_id=user_id))
#     return response.json()

# #mock is used to test the external apis
# #patch is used to test the internal apis

# class TestGetUserData(unittest.TestCase):

#         @patch('requests.get')
#         def test_get_user_data(self, mock_get):
#             mock_response=Mock()
#             response_dict={"login":"test_user", "id":1234}
#             mock_response.json.return_value=response_dict
            
#             mock_get.return_value=mock_response
            
#             user_data=get_user_data(1)
#             mock_get.assert_called_with("https://api.github.com/users/1")
#             self.assertEqual(user_data, response_dict)
            
# if __name__=="__main__":
#     unittest.main()

            