import unittest
import aftersales

class TestScript(unittest.TestCase):

    #def test_(self):   
        #self.assertEqual(aftersales.([]),)
        #self.assertEqual(aftersales. )
        #self.assertEqual(chris_paftersalesroject_1.( ))

    def test_extend_service_duration(self):
        self.assertEqual( extend_service_duration(service_contract_durations, vins, "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b" , 3) , [4,3,3,2,1,2,5,5,5,5,5,3,2,2,3,3,1,2,4,3,2,4,1,4,2,1,3,2,1] )

if __name__ == "__main__":
    unittest.main()


