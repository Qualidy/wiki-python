import unittest
import wiki.material.Projekt_1B.stuecklistenaufloesung as stuecklistenaufloesung

class TestScript(unittest.TestCase):

    def test_stuecklistenaufloesung(self):   
        self.assertEqual(stuecklistenaufloesung.stuecklistenaufloesung([]),(0,0,0,0,0,0))
        self.assertEqual(stuecklistenaufloesung.stuecklistenaufloesung([ "30 mal Modul_A", "50 mal Modul_B" , "70 mal Modul_C"]),(500, 500, 2590, 48000, 8195.0, 1385.0))
        self.assertEqual(stuecklistenaufloesung.stuecklistenaufloesung([ "345 mal Modul_A", "123 mal Modul_B" , "456 mal Modul_C"]),(2586, 1230, 17919, 342600, 48802.200000000004, 4258.5))


    def test_lagerbestand(self):
        self.assertEqual(stuecklistenaufloesung.lagerbestand() , (5, 3, 7, 1, 200, 7000) )

if __name__ == "__main__":
    unittest.main()