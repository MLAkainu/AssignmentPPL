import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """program"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
