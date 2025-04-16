from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Lead
from django.http import HttpResponse
from django.utils import timezone
from .forms import LeadForm, PublicLeadForm  # Add PublicLeadForm import
from django.contrib.auth.decorators import login_required


def test_view(request):
    return HttpResponse("Test view is working!")

@login_required
def lead_list(request):
    """View to display all leads."""
    leads = Lead.objects.all().order_by('-created_at')
    return render(request, 'leads/lead_list.html', {'leads': leads})

@login_required
def lead_create(request):
    """View to create a new lead."""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Lead created successfully!")
            return redirect('lead_list')
    else:
        form = LeadForm()

    return render(request, 'leads/lead_form.html', {'form': form, 'title': 'Add New Lead'})

@login_required
def lead_detail(request, pk):
    """View to display a specific lead's details."""
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})

@login_required
def lead_update(request, pk):
    """View to update an existing lead."""
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Lead updated successfully!")
            return redirect('lead_detail', pk=lead.pk)
    else:
        form = LeadForm(instance=lead)

    return render(request, 'leads/lead_form.html', {
        'form': form, 
        'lead': lead,
        'title': f'Update Lead: {lead.full_name}'
    })

@login_required
def lead_delete(request, pk):
    """View to delete a lead."""
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        lead.delete()
        messages.success(request, "Lead deleted successfully!")
        return redirect('lead_list')
        
    return render(request, 'leads/lead_confirm_delete.html', {'lead': lead})

def public_lead_form(request):
    """View for public lead submissions"""
    if request.method == 'POST':
        form = PublicLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.status = 'new'  # Set the default status
            # If you added the optional fields
            lead.is_public_submission = True
            lead.public_submission_date = timezone.now()
            lead.save()
            
            # Use Django's messaging framework to show a confirmation
            messages.success(request, "Thank you for your interest! We'll be in touch soon.")
            return redirect('public_lead_thanks')
    else:
        form = PublicLeadForm()
    
    return render(request, 'public/lead_form.html', {'form': form})

def public_lead_thanks(request):
    """Thank you page after form submission"""
    return render(request, 'public/lead_thanks.html')

def home_view(request):
    """Home page with options for salespeople or potential clients"""
    return render(request, 'home.html')