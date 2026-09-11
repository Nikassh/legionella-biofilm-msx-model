import unittest
from legionella_msx.msx_writer import EPANETMSXWriter

class TestLegionellaMSX(unittest.TestCase):
    def test_msx_writer_syntax(self):
        content = EPANETMSXWriter.generate_msx_content(k_inact=0.8, k_detach=0.2)
        self.assertIn("[TITLE]", content)
        self.assertIn("[SPECIES]", content)
        self.assertIn("k_inact 0.8", content)
        self.assertIn("[END]", content)

if __name__ == '__main__':
    unittest.main()
