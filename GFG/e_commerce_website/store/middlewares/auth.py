from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']   #  The path that the user is trying to access.
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
           # This query parameter is used to redirect the user back to the original page they were trying to access
           # after they have successfully logged in
           return redirect(f'login?return_url={returnUrl}')  

        response = get_response(request)
        return response

    return middleware