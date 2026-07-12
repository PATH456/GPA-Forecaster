from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Term
from .serializers import TermSerializer


class HealthCheckView(APIView):
    """Confirm that the backend is running."""

    def get(self, request):
        return Response({"status": "ok"})


class TermListCreateView(APIView):
    """List every term or create a new one."""

    def get(self, request):
        terms = Term.objects.all()
        serializer = TermSerializer(terms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TermSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )
