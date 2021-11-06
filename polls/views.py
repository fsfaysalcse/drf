from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll
from .serializers import PollSerializer
from .custom_responses import (prepare_success_response, prepare_error_response,
                                    prepare_create_success_response)


class PollAPIView(APIView):
   
    def get(self, request):
        poll = Poll.objects.all()
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PollDetailsUpdateDeleteView(APIView):

    def get_object(self, pk):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise None
    
    def get(self, request, pk):
        poll = self.get_object(pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        pass
    
    def delete(self, request, pk):
        poll = self.get_object(pk)
        if poll is not None:
            poll.delete()
            return Response(prepare_success_response("Data deleted successfully"), status=status.HTTP_200_OK)
        return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)
