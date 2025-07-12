from django.shortcuts import render

def goal_list(request):
    return render(request, 'goals/goal_list.html')

def goal_form(request):
    return render(request, 'goals/goal_form.html')

def goal_fulfillment(request):
    return render(request, 'goals/goal_fulfillment.html')
