from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll
from .serializers import PollSerializer
from .custom_responses import (prepare_success_response, prepare_error_response,
                                    prepare_create_success_response)
from .validation_service import validate_poll_data


class PollAPIView(APIView):
   
    def get(self, request):
        poll = Poll.objects.all()
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
       # validate_error = validate_poll_data(request.data)
        #if validate_error is not None:
           # return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = PollSerializer(data=request.data)
        print("Working")
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



