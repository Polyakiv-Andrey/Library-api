from rest_framework import viewsets

from Borrowing.models import Borrowing
from Borrowing.serializers import BorrowingListSerializer, BorrowingDitailSerializer, BorrowingCreateSerializer
from book.permissions import IsAdminAllowMethodsIsUserAllowListRetrieve


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    permission_classes = (IsAdminAllowMethodsIsUserAllowListRetrieve,)

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        if self.action == "create":
            return BorrowingCreateSerializer
        return BorrowingDitailSerializer

    def perform_create(self, serializer):
        serializer.save(User_id=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(User_id=self.request.user)


