from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request,
                  "capstone/questionnaire.html",
                  )


def report_page(request):
    return render(request,
                  "capstone/report.html",
                  )
