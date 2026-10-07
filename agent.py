import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from app.core.diagnostics import run_basic_diagnostics


HOST = "127.0.0.1"
PORT = 8765


class AgentHandler(BaseHTTPRequestHandler):

    def _send_json(self, data, status=200):
        payload = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()

        self.wfile.write(payload)

    def do_GET(self):
        if self.path == "/health":
            self._send_json({
                "agent": "NETNEXUS Local Agent",
                "status": "ONLINE"
            })
            return

        if self.path == "/diagnose":
            try:
                evidence = run_basic_diagnostics()

                self._send_json({
                    "agent": "NETNEXUS Local Agent",
                    "status": "ONLINE",
                    "evidence": evidence
                })

            except Exception as exc:
                self._send_json({
                    "agent": "NETNEXUS Local Agent",
                    "status": "ERROR",
                    "error": str(exc)
                }, 500)

            return

        self._send_json({
            "error": "Endpoint not found"
        }, 404)


if __name__ == "__main__":
    print()
    print("==============================================")
    print("       NETNEXUS LOCAL DIAGNOSTIC AGENT")
    print("==============================================")
    print(f"Agent: http://{HOST}:{PORT}")
    print(f"Health: http://{HOST}:{PORT}/health")
    print(f"Diagnosis: http://{HOST}:{PORT}/diagnose")
    print("==============================================")
    print()

    server = HTTPServer((HOST, PORT), AgentHandler)
    server.serve_forever()
