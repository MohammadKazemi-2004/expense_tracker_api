from django.db import models
from django.utils import timezone

expense_categories = [(x,x) for x in ['Groceries', 'Leisure', 'Electronics','Utilities', 'Clothing', 'Health', 'Others']] 
class Expense(models.Model):
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name='expense')
    title = models.CharField(max_length=100, choices=expense_categories)
    expense = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    