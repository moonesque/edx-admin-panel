"""
Views for iknito_admin_panel.
"""

from rest_framework import views
from rest_framework import response
from rest_framework import status
from rest_framework.permissions import AllowAny


class HelloEdx(views.APIView):
    """Simply test out the app by responding with hello."""

    permission_classes = [AllowAny]

    def get(self, request):
        """Test get method."""
        return response.Response(
            {"message": "Hello Openedx"}, status=status.HTTP_200_OK
        )
