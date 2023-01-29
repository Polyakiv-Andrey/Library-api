from rest_framework import serializers

from Borrowing.models import Borrowing
from book.serializers import BookSerializer


class BorrowingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrowing
        fields = "__all__"


class BorrowingDitailSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False, read_only=True)
