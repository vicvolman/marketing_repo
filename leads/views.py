from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .forms import LeadForm
from .models import Lead
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test view is working!")

def lead_list(request):
    """View to display all leads."""
    leads = Lead.objects.all().order_by('-created_at')
    return render(request, 'leads/lead_list.html', {'leads': leads})

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

def lead_detail(request, pk):
    """View to display a specific lead's details."""
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})

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

def lead_delete(request, pk):
    """View to delete a lead."""
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        lead.delete()
        messages.success(request, "Lead deleted successfully!")
        return redirect('lead_list')
        
    return render(request, 'leads/lead_confirm_delete.html', {'lead': lead})
