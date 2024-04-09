from django.db import models

class Author(models.Model):
    AuthorID = models.IntegerField(primary_key=True)
    AuthorName = models.CharField(max_length=100)
    BirthDate = models.DateField(null=True, blank=True)
    Nationality = models.CharField(max_length=50)

class Book(models.Model):
    BookID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=20)
    AuthorID = models.ForeignKey(Author, on_delete=models.CASCADE)
    Genre = models.CharField(max_length=50)
    PublishedDate = models.DateField(null=True, blank=True)
    QuantityAvailable = models.IntegerField()

class Borrower(models.Model):
    BorrowerID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Address = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.EmailField()

class Transaction(models.Model):
    TransactionID = models.IntegerField(primary_key=True)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowerID = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    CheckoutDate = models.DateField()
    ReturnDate = models.DateField()
    Status = models.CharField(max_length=20)

class Fine(models.Model):
    FineID = models.IntegerField(primary_key=True)
    TransactionID = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    FineAmount = models.DecimalField(max_digits=10, decimal_places=2)
    Paid = models.BooleanField()