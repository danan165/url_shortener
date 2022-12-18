import unittest
from url_shortener.models import URLShortener

class TestURLShortener(unittest.TestCase):
    def test_multiple_compress_restore(self):
        urls = [
            "https://www.nationalgeographic.com/animals/mammals/facts/cabybara-facts",
            "https://www.britannica.com/animal/capybara-genus",
            "https://www.worldatlas.com/articles/10-delightful-facts-about-capybaras.html",
            "https://duckduckgo.com/?t=ffab&q=capybara&ia=web"

        ]
        URLShortenerInst = URLShortener()

        for url in urls:
            compressed_url = URLShortenerInst.shorten(url)
            self.assertNotEqual(compressed_url, url)
            self.assertTrue(len(compressed_url) < len(url))

        self.assertEqual(len(urls), len(URLShortenerInst.urls))

    def test_compress_duplicates(self):
        urls = [
            "https://www.nationalgeographic.com/animals/mammals/facts/cabybara-facts",
            "https://www.nationalgeographic.com/animals/mammals/facts/cabybara-facts",
            "https://www.nationalgeographic.com/animals/mammals/facts/cabybara-facts",
            "https://duckduckgo.com/?t=ffab&q=capybara&ia=web"

        ]
        URLShortenerInst = URLShortener()

        for url in urls:
            compressed_url = URLShortenerInst.shorten(url)
            self.assertNotEqual(compressed_url, url)
            self.assertTrue(len(compressed_url) < len(url))

        print(URLShortenerInst.urls)

        self.assertEqual(len(URLShortenerInst.urls), 2)

    def test_nonexistent_restore(self):

        URLShortenerInst = URLShortener()

        restored_url = URLShortenerInst.restore("GQ==")
        self.assertEqual(restored_url, None)
        self.assertEqual(len(URLShortenerInst.urls), 0)

    def test_basic_compress_and_restore(self):
        urls = [
            "https://www.nationalgeographic.com/animals/mammals/facts/cabybara-facts",
            "https://www.britannica.com/animal/capybara-genus",
            "https://www.worldatlas.com/articles/10-delightful-facts-about-capybaras.html",
            "https://duckduckgo.com/?t=ffab&q=capybara&ia=web"

        ]
        URLShortenerInst = URLShortener()

        for url in urls:
            compressed_url = URLShortenerInst.shorten(url)
            self.assertNotEqual(compressed_url, url)
            self.assertTrue(len(compressed_url) < len(url))

            restored_url = URLShortenerInst.restore(compressed_url)
            self.assertEqual(url, restored_url)

        self.assertEqual(len(urls), len(URLShortenerInst.urls))

if __name__=="__main__":
    unittest.main()

