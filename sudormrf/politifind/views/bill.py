from django.shortcuts import render

def bill(request, id):
    
    

    return render(
        request,
        'bill.html',
        context={
            
        }
    )
