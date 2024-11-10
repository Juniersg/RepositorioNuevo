# index.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Configuración del servidor
HOST = 'localhost'
PORT = 5000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, content):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def do_GET(self):
        # Ruta de inicio para comprobar el estado del backend
        if self.path == '/':
            response_content = json.dumps({"status": "success", "message": "Backend iniciado correctamente!"})
            self._send_response(200, response_content)
            print(f"Solicitud recibida en '/' - Respuesta: {response_content}")
        else:
            # Respuesta para rutas no definidas
            response_content = json.dumps({"status": "error", "message": "Ruta no encontrada"})
            self._send_response(404, response_content)
            print(f"Solicitud recibida en '{self.path}' - Respuesta: {response_content}")

# Inicialización del servidor
def run_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Servidor corriendo en http://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
