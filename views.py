#
# LazyCook
# Copyright (c) 2011 Sporetree.com
#
from django.http import HttpResponse

def home(request):
    return HttpResponse("Who are you calling a lazy cook?!");
