from django.db import models

class Lead(models.Model):
    # Basic contact information
    full_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    
    # Public submission tracking
    is_public_submission = models.BooleanField(default=False)
    public_submission_date = models.DateTimeField(blank=True, null=True)
    
    # Tourism project details
    TOURISM_FOCUS_CHOICES = [
        ('cultural', 'Cultural Tourism'),
        ('ecotourism', 'Ecotourism'),
        ('adventure', 'Adventure Tourism'),
        ('community', 'Community-Based Tourism'),
        ('digital', 'Digital Tourism Solutions'),
        ('gastronomy', 'Gastronomic Tourism'),
        ('other', 'Other'),
    ]
    tourism_focus = models.CharField(max_length=50, choices=TOURISM_FOCUS_CHOICES, blank=True, null=True)
    
    PROJECT_STAGE_CHOICES = [
        ('idea', 'Idea Stage'),
        ('prototype', 'Prototype/MVP'),
        ('operating', 'Operating Business'),
        ('scaling', 'Scaling Phase'),
    ]
    project_stage = models.CharField(max_length=50, choices=PROJECT_STAGE_CHOICES, blank=True, null=True)
    
    FUNDING_NEEDS_CHOICES = [
        ('<10k', 'Less than $10,000'),
        ('10k-50k', '$10,000 - $50,000'),
        ('50k-100k', '$50,000 - $100,000'),
        ('100k-500k', '$100,000 - $500,000'),
        ('>500k', 'More than $500,000'),
        ('unknown', 'Not sure yet'),
    ]
    funding_needs = models.CharField(max_length=50, choices=FUNDING_NEEDS_CHOICES, blank=True, null=True)
    
    # Lead details
    LEAD_SOURCE_CHOICES = [
        ('website', 'Website'),
        ('referral', 'Referral'),
        ('social_media', 'Social Media'),
        ('event', 'Tourism Event'),
        ('partner', 'Partner Organization'),
        ('other', 'Other'),
    ]
    source = models.CharField(max_length=50, choices=LEAD_SOURCE_CHOICES)
    
    LEAD_STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('assessment', 'Under Assessment'),
        ('proposal', 'Proposal'),
        ('negotiation', 'Negotiation'),
        ('incubation', 'In Incubation'),
        ('closed_won', 'Successful Project'),
        ('closed_lost', 'Not Proceeding'),
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