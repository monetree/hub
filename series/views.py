from django.shortcuts import render
from django.http import JsonResponse
from .models import FibonacciModel

# extend the recursive time limit
import sys
sys.setrecursionlimit(15000)

cache = {}

class FibonacciCalculation:
    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
            cache[n] = result
            return result

    def get_fibonacci(request):
        if request.method == "POST":
            num = int(request.POST.get('number'))
            res = fibonacci(num)
            try:
                obj = FibonacciModel.objects.create(num=num, res=res)
                context = {
                    "msg": "Fibonacci Of {} Is {}".format(num, res)
                }
            except OverflowError:
                context = {
                    "msg": "fibonacci number is too big to store in database"
                }
            return render(request, 'index.html',context)
        else:
            return render(request, 'index.html')

    def get_results(request):
        res = FibonacciModel.objects.all()
        context = {
            "data": res
        }
        return render(request, 'table.html', context)

    def get_results_api(request):
        num = request.GET.get('number', None)
        if num is not None:
            output = fibonacci(int(num))
            try:
                obj = FibonacciModel.objects.create(num=num, res=output)
            except OverflowError:
                return JsonResponse({"code":400, "msg":"fibonacci number is too big to store in database"})
        res = list(FibonacciModel.objects.values())
        return JsonResponse(res, safe=False)
