import os
import unittest
from main import analyze_image

class TestTournamentSorter(unittest.TestCase):
    
    def setUp(self):
        self.assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
        
    def test_tournament_ocr_extraction(self):
        # Ensure the assets directory exists
        if not os.path.exists(self.assets_dir):
            self.fail(f"Assets directory not found: {self.assets_dir}")
            
        images = [f for f in os.listdir(self.assets_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        # Check if there are images
        if not images:
            self.fail(f"No test images found in {self.assets_dir}")
            
        for img_name in images:
            img_path = os.path.join(self.assets_dir, img_name)
            
            # The correct folder name is the file name without extension
            expected_name = os.path.splitext(img_name)[0]
            
            # Process the image directly
            actual_name = analyze_image(img_path)
            
            self.assertIsNotNone(actual_name, f"Failed to process image: {img_path}")
            
            # Assert that the extracted name matches the expected name
            # We use assertIn to allow partial matching or exact matching based on needs,
            # but usually exact matching is better if the file names are exact.
            self.assertEqual(expected_name, actual_name, 
                             f"OCR failed for {img_name}. Expected: '{expected_name}', Got: '{actual_name}'")

if __name__ == '__main__':
    unittest.main()
