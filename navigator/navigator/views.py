
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        ''' <h1> 
                Hello!
            </h1></br>
            <a href="http://yogeshseralia.xyz">Yogesh Seralia Blog</a>
            '''
    )