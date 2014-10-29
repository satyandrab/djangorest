from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests

URL = 'https://everest1314921858.zendesk.com/api/v2/suspended_tickets.json'
USER = 'kbse2000@gmail.com'
PWD = 'bismillah2015'


class SuspendedTicketsView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, format=None):

        # Do the HTTP get request
        try:
            response = requests.get(URL, auth=(USER, PWD))
            # Decode the JSON response into a dictionary and use the data
            data = response.json()
            # Check for HTTP codes other than 200
            if response.status_code != 200:
                payload = {
                    'success': False,
                    'Status': response.status_code,
                    'message': 'Problem with the request. Exiting.'
                }
                return Response(payload, response.status_code)
            else:
                return Response(data, status.HTTP_200_OK)
        except Exception as e:
            payload = {
                'success': False,
                'message': e.message
            }
            return Response(payload, response.status_code)