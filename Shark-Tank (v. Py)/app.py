from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

UPLOAD_FOLDER = 'uploads'

class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        file_data = self.rfile.read(content_length)

        file_name = self.headers['Content-Disposition'].split('filename=')[1].strip('"')
        file_path = os.path.join(UPLOAD_FOLDER, file_name)

        with open(file_path, 'wb') as f:
            f.write(file_data)

        with open(file_path, 'r') as f:
            text = f.read()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(text.encode())

def run():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    print('Server started on port 8000...')
    httpd.serve_forever()
    print("Server running on port 8000")
input("Press Enter")
if __name__ == '__main__':
    run()