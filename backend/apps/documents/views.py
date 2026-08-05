from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocumentForm
from .models import Document
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import FileResponse

@login_required
def document_download_view(request, pk):
    document = get_object_or_404(
        Document,
        pk=pk,
        owner=request.user,
    )

    if not document.file:
        return redirect("documents:detail", pk=document.pk)

    response = FileResponse(
        document.file.open("rb"),
        as_attachment=True,
        filename=document.file.name.split("/")[-1],
    )

    return response

@login_required
def document_list_view(request):
    documents = Document.objects.filter(
        owner=request.user
    ).order_by("-created_at")

    search_query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    if search_query:
        documents = documents.filter(
            title__icontains=search_query
        )

    if category:
        documents = documents.filter(
            category=category
        )

    paginator = Paginator(documents, 6)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "documents/document_list.html",
        {
            "documents": page_obj,
            "search_query": search_query,
            "selected_category": category,
            "category_choices": Document.CATEGORY_CHOICES,
        },
    )

@login_required
def document_list_view(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    documents = Document.objects.filter(
        owner=request.user,
    )

    if query:
        documents = documents.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
        )

    if category:
        documents = documents.filter(
            category=category,
        )

    documents = documents.order_by("-created_at")

    paginator = Paginator(
        documents,
        6,
    )

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "documents/document_list.html",
        {
            "page_obj": page_obj,
            "documents": page_obj.object_list,
            "query": query,
            "selected_category": category,
            "category_choices": Document.CATEGORY_CHOICES,
        },
    )


@login_required
def document_create_view(request):
    if request.method == "POST":
        form = DocumentForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            document = form.save(commit=False)
            document.owner = request.user
            document.save()

            return redirect(
                "documents:detail",
                pk=document.pk,
            )
    else:
        form = DocumentForm()

    return render(
        request,
        "documents/document_create.html",
        {
            "form": form,
        },
    )


@login_required
def document_detail_view(request, pk):
    document = get_object_or_404(
        Document,
        pk=pk,
        owner=request.user,
    )

    return render(
        request,
        "documents/document_detail.html",
        {
            "document": document,
        },
    )
    
@login_required
def document_update_view(request, pk):
    document = get_object_or_404(
        Document,
        pk=pk,
        owner=request.user,
    )

    old_file = document.file

    if request.method == "POST":
        form = DocumentForm(
            request.POST,
            request.FILES,
            instance=document,
        )

        if form.is_valid():
            updated_document = form.save()

            if (
                old_file
                and updated_document.file
                and old_file.name != updated_document.file.name
            ):
                old_file.delete(save=False)

            return redirect(
                "documents:detail",
                pk=updated_document.pk,
            )

    else:
        form = DocumentForm(
            instance=document,
        )

    return render(
        request,
        "documents/document_update.html",
        {
            "form": form,
            "document": document,
        },
    )
    
@login_required
def document_delete_view(request, pk):
    document = get_object_or_404(
        Document,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        document.delete()
        return redirect("documents:list")

    return render(
        request,
        "documents/document_confirm_delete.html",
        {
            "document": document,
        },
    )