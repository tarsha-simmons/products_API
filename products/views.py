from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def products_list(request):
    # add query here to get all prodcuts from DB and send with response

    return Response('ok')