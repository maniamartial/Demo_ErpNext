import unittest

# def sum(a,b):
#     return a+b 
class MyExcept(Exception):
    def __init__(self, msg, error_code):
        super().__init__(msg)
        self.error_code=error_code
        
class SecondExcept(Exception):
    pass

def throw_ex(var):
    if var ==100:
        raise MyExcept("Not a valid number", 1024)
    elif var==200:
        raise SecondExcept("Second Exception passed")
    else:
        return True

class LearnTest(unittest.TestCase):
    
    def test_throw_ex(self):
        # self.assertRaises(MyExcept, throw_ex, 100)
        with self.assertRaises(MyExcept) as context:
            throw_ex(100)
            
        print(context.exception.error_code)
        
        
    # def setUp(self):
    #     print("setup Running...")
    #     self.a=10
    #     self.b=20
        
    # def tearDown(self):
    #     print("tearDown Running...")
    #     self.a=0
    #     self.b=0
    
    # def test_sum(self):
    #     print("test_sum Running...")
    #     #Act'
    #     result=sum(self.a, self.b)
    #     #assert
    #     self.assertEqual(result, self.a + self.b)
    
    # def test_sum_2(self):
    #     print("test_sum_2 Running...")
    #     a=45
    #     b=22
    #     result=sum(a,b)
        
    #     self.assertEqual(result, a+b, msg="Sum is not correct")
if __name__ =="__main__":
    unittest.main()