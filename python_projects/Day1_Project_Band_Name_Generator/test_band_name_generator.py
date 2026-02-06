import unittest

from band_name_generator import generate_band_name

class TestBandNameGenerator(unittest.TestCase):
    
    def test_normal_names(self):
        result = generate_band_name("Cape Town", "Buddy")
        self.assertEqual(result, "Cape Town Buddy")
        
    def test_empty_city(self):
        result = generate_band_name("", "Max")
        self.assertEqual(result, " Max")
        
    def test_empty_pet(self):
        result = generate_band_name("London", "")
        self.assertEqual(result, "London ")
        
    def test_both_empty(self):
        result = generate_band_name("", "")
        self.assertEqual(result," ")
        
 
if __name__ == "__main__":
    unittest.main        