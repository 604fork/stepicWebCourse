import urlparse

def app(environ, start_response):
        #data = b"Hello, World!\n"
	#queryDict = urlparse.parse_qs('a=1&b=2')
	data = environ["QUERY_STRING"].replace("&", "\n").encode()
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
