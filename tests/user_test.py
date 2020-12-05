import unittest 
from app.models import User

class UserTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the user class
    '''

    def setUp(self):
        '''
        Set up method that will run befor every test
        '''
        self.new_user = User (username='cynthia', password= 'gitz254')

if __name__ =='__main__':
    unittest.main