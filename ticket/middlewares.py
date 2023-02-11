from django.shortcuts import redirect


def check_user_auth(get_response):
    def middleware(request):
        response = get_response(request)
        if not request.user.is_authenticated:
            if not request.path == "/login/":
                return redirect('login')
        return response
    return middleware
