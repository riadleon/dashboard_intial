import json
from django.shortcuts import render
from .models import ParsedOutput, DirtySEOMetadata, CleanList
from django.db.models import Count, Q
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views.decorators.http import require_POST


def dashboard(request):
    # For ParsedOutput model
    parsed_output_counts = {
        'url': ParsedOutput.objects.exclude(url__isnull=True).count(),
        'title': ParsedOutput.objects.exclude(title__isnull=True).count(),
        'favicon': ParsedOutput.objects.exclude(favicon__isnull=True).count(),
        'locale': ParsedOutput.objects.exclude(locale__isnull=True).count(),
        'type': ParsedOutput.objects.exclude(type__isnull=True).count(),
        'names': ParsedOutput.objects.exclude(names__isnull=True).count(),
        'emails': ParsedOutput.objects.exclude(emails__isnull=True).count(),
        'phone_numbers': ParsedOutput.objects.exclude(phone_numbers__isnull=True).count(),
        'ip_address': ParsedOutput.objects.exclude(ip_address__isnull=True).count(),
        'location': ParsedOutput.objects.exclude(location__isnull=True).count(),
        'keywords': ParsedOutput.objects.exclude(keywords__isnull=True).count(),
    }

    # For DirtySEOMetadata model (assuming you have fields named 'metadata' and 'language')
    dirty_seo_counts = {
        'metadata': DirtySEOMetadata.objects.exclude(dirty_seo_metadata__isnull=True).exclude(dirty_seo_metadata="").count(),
        'language': DirtySEOMetadata.objects.exclude(language__isnull=True).exclude(language="").count(),
    }

    context = {
        'parsed_output_counts_json': json.dumps(parsed_output_counts),
        'dirty_seo_counts_json': json.dumps(dirty_seo_counts)
    }
    
    return render(request, 'dashboard.html', context)

def dirty_seo_view(request):
    all_data = DirtySEOMetadata.objects.all().order_by('id')  # Ordered by id
    paginator = Paginator(all_data, 10)  # Show 10 records per page for demonstration
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    # Count non-None values
    counts = {
        'dirty_seo_metadata_count': all_data.exclude(dirty_seo_metadata__isnull=True).count(),
        'language_count': all_data.exclude(language__isnull=True).count()
    }

    context = {
        'data': data,
        'counts': counts,
    }

    return render(request, 'dirty_seo.html', context)


@require_POST
def move_to_cleanlist(request):
    # Get keyword IDs from POST request
    keyword_ids = request.POST.getlist('keyword_ids')
    
    # For each keyword, transfer to CleanList and delete from DirtySEOMetadata
    for keyword_id in keyword_ids:
        keyword = DirtySEOMetadata.objects.get(pk=keyword_id)
        CleanList.objects.create(keyword=keyword.dirty_seo_metadata, language=keyword.language)
        keyword.delete()
    
    return redirect('dirty_seo')


def cleanlist_view(request):
    clean_keywords = CleanList.objects.all().order_by('id')
    context = {
        'clean_keywords': clean_keywords,
    }
    return render(request, 'cleanlist.html', context)


def parsed_output_view(request):
    all_data = ParsedOutput.objects.all().order_by('id')  # Ordered by id
    paginator = Paginator(all_data, 10)  # Show 10 records per page for demonstration
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    # Count non-None values
    counts = {
        'url_count': all_data.exclude(url__isnull=True).count(),
        'title_count': all_data.exclude(title__isnull=True).count(),
        'favicon_count': all_data.exclude(favicon__isnull=True).count(),
        'locale_count': all_data.exclude(locale__isnull=True).count(),
        'type_count': all_data.exclude(type__isnull=True).count(),
        'names_count': all_data.exclude(names__isnull=True).count(),
        'emails_count': all_data.exclude(emails__isnull=True).count(),
        'phone_numbers_count': all_data.exclude(phone_numbers__isnull=True).count(),
        'ip_address_count': all_data.exclude(ip_address__isnull=True).count(),
        'location_count': all_data.exclude(location__isnull=True).count(),
        'keywords_count': all_data.exclude(keywords__isnull=True).count(),
    }
    
    context = {
        'data': data,
        'counts': counts,
    }

    return render(request, 'parsed_output.html', context)
