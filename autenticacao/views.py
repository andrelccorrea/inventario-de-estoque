from django.contrib.auth.views import LoginView

from autenticacao.forms import CustomUserLoginForm


class LoginCustomUser(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomUserLoginForm

    def form_valid(self, form):
        lembrar = form.cleaned_data.get("remember")
        if not lembrar:
            self.request.session.set_expiry(0)
        user = form.get_user()
        user.remember = lembrar
        user.save(update_fields=["remember"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["configuracoes"]
