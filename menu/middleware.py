from django.db import connection

class QueryCountDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # После выполнения запросов
        print(f"Количество запросов к базе данных: {len(connection.queries)}")
        for query in connection.queries:
            print(query['sql'])

        return response