from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
      This class is responsible for creating a new tag
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        print(f"Creating tag for product {product_code}")
        return HttpResponse(status_code=200, body={"resp": "ok"})
        