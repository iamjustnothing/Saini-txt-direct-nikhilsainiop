import unittest

import saini


class ClassplusContentIdTests(unittest.TestCase):
    def test_extracts_content_hash_idl_from_nonstandard_link(self):
        url = (
            "https://media-cdn.classplusapp.com/course/master.m3u8"
            "&contentHashIdl=U2FsdGVkX18+6TX/BV=="
        )
        self.assertEqual(saini.extract_classplus_content_id(url), "U2FsdGVkX18+6TX/BV==")

    def test_extracts_content_hash_id_query_parameter(self):
        url = "https://example.test/master.m3u8?contentHashId=abc+123/xyz&other=1"
        self.assertEqual(saini.extract_classplus_content_id(url), "abc+123/xyz")

    def test_returns_none_without_content_hash(self):
        self.assertIsNone(saini.extract_classplus_content_id("https://example.test/master.m3u8"))


if __name__ == "__main__":
    unittest.main()
