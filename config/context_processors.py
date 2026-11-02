from .models import CompanyInfo


def company(request):
    return {'company': CompanyInfo.objects.first()}