from rest_framework import viewsets
from .models import Conversation
from rest_framework.response import Response
from .serializers import MessageSerializer
from .schemas import list_message_docs


class MessageViewSet(viewsets.ViewSet):
    @list_message_docs
    def list(self, request):
        channel_id = request.query_params.get("channel_id")
        try:
            conversation = Conversation.objects.get(channel_id=channel_id)
            message = conversation.message.all()
            serializier = MessageSerializer(message, many=True)
            return Response(serializier.data)
        except Conversation.DoesNotExist:
            return Response([])
