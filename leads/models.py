from django.db import models

class Lead(models.Model):
    # Basic contact information
    full_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    
    # Lead details
    LEAD_SOURCE_CHOICES = [
        ('website', 'Website'),
        ('referral', 'Referral'),
        ('social_media', 'Social Media'),
        ('cold_call', 'Cold Call'),
        ('trade_show', 'Trade Show'),
        ('other', 'Other'),
    ]
    source = models.CharField(max_length=50, choices=LEAD_SOURCE_CHOICES)
    
    LEAD_STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('proposal', 'Proposal'),
        ('negotiation', 'Negotiation'),
        ('closed_won', 'Closed Won'),
        ('closed_lost', 'Closed Lost'),
    ]
    status = models.CharField(max_length=50, choices=LEAD_STATUS_CHOICES, default='new')
    
    # Additional information
    notes = models.TextField(blank=True, null=True)
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Optional: Next follow-up date
    next_follow_up = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.company or 'No Company'}"
