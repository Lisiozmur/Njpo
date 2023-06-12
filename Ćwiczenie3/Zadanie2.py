class HttpRequest:
    def __init__(self, request_type, file_name, user_id, form_data):
        self.request_type = request_type
        self.file_name = file_name
        self.user_id = user_id
        self.form_data = form_data

class RequestHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, request):
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            raise ValueError("No handler available to handle the request")

class RequestTypeHandler(RequestHandler):
    def handle_request(self, request):
        if request.request_type == "GET" or request.request_type == "POST":
            return super().handle_request(request)
        else:
            raise ValueError("Invalid request type")

class FileHandler(RequestHandler):
    def handle_request(self, request):
        if request.file_name is None:
            return super().handle_request(request)
        else:
            raise ValueError("File requests not allowed")

class RateLimitHandler(RequestHandler):
    MAX_REQUESTS_PER_MINUTE = 100

    def __init__(self, next_handler=None):
        self.request_count = 0
        super().__init__(next_handler)

    def handle_request(self, request):
        self.request_count += 1
        if self.request_count <= self.MAX_REQUESTS_PER_MINUTE:
            return super().handle_request(request)
        else:
            raise ValueError("Rate limit exceeded")

class UserRateLimitHandler(RequestHandler):
    MAX_REQUESTS_PER_MINUTE = 10

    def __init__(self, next_handler=None):
        self.user_request_counts = {}
        super().__init__(next_handler)

    def handle_request(self, request):
        if request.user_id is not None:
            user_id = request.user_id
            if user_id not in self.user_request_counts:
                self.user_request_counts[user_id] = 0
            self.user_request_counts[user_id] += 1
            if self.user_request_counts[user_id] <= self.MAX_REQUESTS_PER_MINUTE:
                return super().handle_request(request)
            else:
                raise ValueError("User rate limit exceeded")
        else:
            return super().handle_request(request)

class SqlInjectionHandler(RequestHandler):
    def handle_request(self, request):
        if "'; DROP TABLE" not in request.form_data:
            return super().handle_request(request)
        else:
            raise ValueError("Potential SQL injection detected")

# Przykład użycia
def process_request(request):
    handler_chain = RequestTypeHandler(
        FileHandler(
            RateLimitHandler(
                UserRateLimitHandler(
                    SqlInjectionHandler()
                )
            )
        )
    )
    try:
        handler_chain.handle_request(request)
        print("Request processed successfully")
    except ValueError as e:
        print("Request processing failed:", str(e))

# Tworzenie żądania
request = HttpRequest("POST", None, 123, "form data")
# Przetwarzanie żądania
process_request(request)
