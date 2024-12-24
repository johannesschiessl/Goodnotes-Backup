#!/usr/bin/env python3

import os
from wsgidav.wsgidav_app import WsgiDAVApp
from wsgidav.fs_dav_provider import FilesystemProvider
from cheroot import wsgi
from pyngrok import ngrok

STORAGE_PATH = os.getenv('STORAGE_PATH')
HOST = "0.0.0.0"
PORT = 8080
NGROK_AUTH_TOKEN = os.getenv('NGROK_AUTH_TOKEN')

def setup_ngrok():
    """Setup ngrok with auth token and get URL."""
    if NGROK_AUTH_TOKEN:
        ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    
    try:
        tunnel = ngrok.connect(PORT, "http")
        print(f"ngrok tunnel established at: {tunnel.public_url}")
        return tunnel
    except Exception as e:
        print(f"Failed to establish ngrok tunnel: {e}")
        return None

def create_storage_if_not_exists():
    """Create the storage directory if it doesn't exist."""
    if not os.path.exists(STORAGE_PATH):
        os.makedirs(STORAGE_PATH)
        print(f"Created storage directory at: {STORAGE_PATH}")

def main():
    create_storage_if_not_exists()
    
    tunnel = setup_ngrok()

    config = {
        "provider_mapping": {
            "/": FilesystemProvider(STORAGE_PATH)
        },
        "simple_dc": {
            "user_mapping": {"*": True}
        },
        "http_authenticator": {
            "accept_basic": True,
            "accept_digest": False,
            "default_to_digest": False,
        },
        "verbose": 1,
        "logging": {
            "enable_loggers": []
        }
    }

    app = WsgiDAVApp(config)
    
    server_addr = (HOST, PORT)
    server = wsgi.Server(server_addr, app)
    
    print(f"WebDAV server running at http://{HOST}:{PORT}")
    print(f"ngrok tunnel established at: {tunnel.public_url}")
    print(f"Storage path: {STORAGE_PATH}")
    print("Press Ctrl+C to quit.")
    
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nShutting down WebDAV server...")
        if tunnel:
            ngrok.disconnect(tunnel.public_url)
        server.stop()

if __name__ == "__main__":
    main()
    