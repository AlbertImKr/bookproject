from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = 'main.html'  # 메인 페이지로 사용할 템플릿 파일 지정
