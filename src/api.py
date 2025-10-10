# API module for LogCutter

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 2
