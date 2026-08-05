from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from apps.documents.models import Document


@login_required
def dashboard_view(request):
    user_documents = Document.objects.filter(
        owner=request.user
    )

    total_documents = user_documents.count()

    category_counts = user_documents.values(
        "category"
    ).annotate(
        total=Count("id")
    )

    category_data = {
        item["category"]: item["total"]
        for item in category_counts
    }

    recent_documents = user_documents.order_by(
        "-created_at"
    )[:5]

    context = {
        "total_documents": total_documents,

        "personal_count": category_data.get(
            "personal", 0
        ),

        "education_count": category_data.get(
            "education", 0
        ),

        "professional_count": category_data.get(
            "professional", 0
        ),

        "certificate_count": category_data.get(
            "certificate", 0
        ),

        "identity_count": category_data.get(
            "identity", 0
        ),

        "recent_documents": recent_documents,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )