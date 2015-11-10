# Create your views here.
from django.http import HttpResponse
import datetime
from models import Book,Author
from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponseRedirect




#from blog.models import Author,Book
'''
def hello(request):
    return HttpResponse("Hello world")

#def Author(request):
    
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</html></body>" % now
    return HttpResponse(html)

'''
def showrecord(requestttt):
    
	Book_list = Book.objects.all()
	c = Context({"Book_list": Book_list })
	return render_to_response("showifm.html", c)



def search(request):
	#word=""
	if request.GET:
         word = request.GET["word"]
         p = Author.objects.get(Name=word)
         q = Book.objects.filter(AuthorID=p)
         c = Context({"result_list": q, "result_len": len(q)})
         return render_to_response("result.html", c)
	return HttpResponseRedirect("/showifm/")

def delete(request):
	dltid = request.GET["id"]
	if len(Book.objects.filter(id=dltid)) > 0:
         Book.objects.filter(id=dltid).delete()
         return HttpResponseRedirect("/showifm/")


def click_result(request):
    dltid = request.GET["id"]
    book = Book.objects.get(id=dltid)
    author = book.AuthorID
    c = Context({"Book": book,"Author": author})
    return render_to_response("click_result.html", c)
    
    
    #c = Context({"Author_list ":Author_list })
    #return render_to_response("click_result.html", c)
    #"Book_list": Book_list,"