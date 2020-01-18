from member.models import Member


class MemberMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        # Cria o membro caso o usuário logado não tenha um membro vinculado
        if request.user.pk and not Member.objects.filter(id=request.user.pk).exists():
            Member(
                id=request.user.pk,
                first_name=request.user.first_name,
                last_name=request.user.last_name,
                email=request.user.email,
                is_admin=request.user.is_staff,
                is_superuser=request.user.is_superuser,
                is_active=True
            ).save()

        return response
