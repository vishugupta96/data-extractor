from django.http.response import HttpResponse


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                print(allowed_roles, group)
                return view_func(request)
            else:
                return HttpResponse('not authorized')


        return wrapper_func
    return decorator

