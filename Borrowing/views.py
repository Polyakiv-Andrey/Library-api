from rest_framework import viewsets

from Borrowing.models import Borrowing
from Borrowing.serializers import BorrowingListSerializer, BorrowingDitailSerializer, BorrowingCreateSerializer
from Borrowing.permissions import OnlyForAuthenticatedUser


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    permission_classes = (OnlyForAuthenticatedUser,)

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        if self.action == "create":
            return BorrowingCreateSerializer
        return BorrowingDitailSerializer

    def perform_create(self, serializer):
        serializer.save(User_id=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff is False:
            return self.queryset.filter(User_id=self.request.user)
        is_active = self.request.query_params.get("Actual_return_date")
        if is_active:
            return self.queryset.filter(Actual_return_date=None)
        return self.queryset


