import base64

class URLShortener:
    def __init__(self):
        self.urls = dict()
        self.id = 1

    def shorten(self, url: str):
        # search for duplicates (return if already compressed)
        for key, value in self.urls.items():
            if value == url:
                return key

        base64_bytes = base64.b64encode(str(self.id).encode('utf-8'))
        compressed_url = base64_bytes.decode("utf-8")
        self.urls[compressed_url] = url
        self.id += 1
        return compressed_url

    def restore(self, compressed_url: str):
        if compressed_url in self.urls:
            return self.urls[compressed_url]
        return None