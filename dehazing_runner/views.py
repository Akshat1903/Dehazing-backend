
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from . import runner


class CallImageProcessing(APIView):

    def get(self, request):
        if request.method == 'GET':
            runner.main_runner.delay()

            response = {
                'status': "Image Analysis Completed",
            }
            return JsonResponse(response, status=status.HTTP_200_OK)
