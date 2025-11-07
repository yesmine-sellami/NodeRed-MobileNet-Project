import unittest
from scripts.modeltest import predict_image
from pathlib import Path

class TestMobileNet(unittest.TestCase):
    def setUp(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.model_path = BASE_DIR / "plante_model_finetuned.h5"

    def test_malade_image(self):
        image_path = Path(__file__).resolve().parent / "images" / "malade.jpg"
        etat, pourcentage = predict_image(str(image_path), str(self.model_path))
        self.assertIn(etat, ["Feuille malade", "Feuille saine"])
        self.assertGreaterEqual(pourcentage, 0)
        self.assertLessEqual(pourcentage, 100)

    def test_saine_image(self):
        image_path = Path(__file__).resolve().parent / "images" / "s.jpg"
        etat, pourcentage = predict_image(str(image_path), str(self.model_path))
        self.assertIn(etat, ["Feuille malade", "Feuille saine"])
        self.assertGreaterEqual(pourcentage, 0)
        self.assertLessEqual(pourcentage, 100)

if __name__ == "__main__":
    unittest.main()
