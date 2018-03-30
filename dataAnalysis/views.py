from django.shortcuts import render
# from django.contrib.auth.decorators import login_required


def heatmap_index(request):
    return render(request, 'dataAnalysis/index.html', locals())
