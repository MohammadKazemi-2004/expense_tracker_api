import django_filters
from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Expense

class FilterPubDate(django_filters.FilterSet):
    pub_date_filter = django_filters.ChoiceFilter(
        field_name = "pub_date",
        method = "filter_by_period",
        choices = [
            ('past_week', 'Past Week'),
            ('past_month', 'Past Month'),
            ('last_3_month', 'Last 3 month'),
            ('custome', 'Custome Range'),
        ],
    )
    
    start_date = django_filters.DateFilter(field_name='pub_date',
                                           lookup_expr='gte',
                                           widget=forms.DateInput(attrs={"type": "date"})
                                           )
    end_date = django_filters.DateFilter(field_name='pub_date',
                                         lookup_expr='lte',
                                         widget=forms.DateInput(attrs={"type": "date"})
                                        )
    
    class Meta:
        model = Expense
        fields = [] # ??
    
    def filter_by_period(self, queryset, name, value):
        now = timezone.now()
        
        if value == "past_week":
            start = now - timedelta(weeks=1)
            return queryset.filter(pub_date__gte = start)
        
        if value == "past_month":
            start = now - timedelta(days=30)
            return queryset.filter(pub_date__gte = start)
        
        if value == "last_3_month":
            start = now - timedelta(days=90)
            return queryset.filter(pub_date__gte = start)
        
        if value == "custome":
            start = self.data.get('start_date')
            end = self.data.get('end_date')
            if start and end:
                return queryset.filter(pub_date__range = [start, end])
            elif start:
                return queryset.filter(pub_date__gte = start)
            elif end:
                return queryset.filter(pub_date__gte = end)
            
        return queryset
                