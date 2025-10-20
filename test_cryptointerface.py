# test_cryptointerface.py
"""
Tests for CryptoInterface module.
"""

import unittest
from cryptointerface import CryptoInterface

class TestCryptoInterface(unittest.TestCase):
    """Test cases for CryptoInterface class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoInterface()
        self.assertIsInstance(instance, CryptoInterface)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoInterface()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
