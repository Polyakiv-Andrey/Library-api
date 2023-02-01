from rest_framework import serializers

from Borrowing.models import Borrowing
from book.models import Book
from book.serializers import BookSerializer


class BorrowingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrowing
        fields = "__all__"


class BorrowingDitailSerializer(BorrowingListSerializer):
    Book_id = BookSerializer(many=False, read_only=True)


class BorrowingCreateSerializer(BorrowingListSerializer):

    class Meta:
        model = Borrowing
        fields = ("id", "Book_id", "Expected_return_date")

    def create(self, validated_data):
        if validated_data["Book_id"].Inventory == 0:
            raise ValueError("Unfortunately we have not that book now")
        book = validated_data["Book_id"]
        book.Inventory -= 1
        book.save()
        return Borrowing.objects.create(**validated_data)

