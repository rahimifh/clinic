from django.views.generic import TemplateView, ListView, DetailView
from dashboard.mixin import SuperuserRequiredMixin
#from www.forms import GameForm
#from www.models import Game


class GameListView(SuperuserRequiredMixin, ListView):
        template_name = 'dashboard/pages/game_list.html'
        #model = Game

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['title'] = 'لیست بخت آزمایی ها'
                return context


class GameDetailView(SuperuserRequiredMixin, DetailView):
        template_name = 'dashboard/pages/game_detail.html'
        #model = Game

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['title'] = 'جزئیات بخت آزمایی'
                #context['form'] = GameForm(instance=context['game'])
                #context['get_winners'] = reversed(context['game'].get_winners())

                return context


class DashboardView(SuperuserRequiredMixin, TemplateView):
        template_name = 'dashboard/pages/index.html'
