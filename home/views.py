from django.shortcuts import redirect, render,redirect
from .models import *
# Create your views here.
def home(request):
    profile = Profile.objects.filter(user=request.user).first()
    expenses= Expense.objects.filter(user=request.user)
    if request.method=='POST':
        text=request.POST.get('text')
        amount=request.POST.get('amount')
        expense_type=request.POST.get('expense_type')
        
        expense=Expense(user=request.user,name=text,amount=amount,expense_type=expense_type)
        expense.save()

        if expense_type=='Positive':
            profile.balance+=float(amount)
        else:
            profile.expenses+=float(amount)
            profile.balance-=float(amount)
        profile.save()
        return redirect('/',)

    
    context={'profile':profile,'expenses':expenses}
    return render(request,'home.htm',context)