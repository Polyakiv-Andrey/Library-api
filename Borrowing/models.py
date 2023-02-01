from django.db import models
from django.db.models import CheckConstraint, Q, F

from Customer.models import User
from book.models import Book


class Borrowing(models.Model):
    Borrow_date = models.DateTimeField(auto_now_add=True)
    Expected_return_date = models.DateTimeField(null=False, blank=False)
    Actual_return_date = models.DateTimeField(blank=True, null=True)
    Book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(Expected_return_date__gt=F("Borrow_date")), name="Expected_return_date"
            ),
            CheckConstraint(
                check=Q(Actual_return_date__lte=F("Expected_return_date")), name="Actual_return_date"
            )
        ]

    def __str__(self):
        return f"Expected_return_date: {self.Expected_return_date}"
