from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from . models import ActionsCategory, Action
# Create your views here.


def action(request, category_slug=None):
    category = get_object_or_404(ActionsCategory, en_slug=category_slug)
    action_list = Action.objects.filter(category=category)
    paginator = Paginator(action_list, 4)
    page = request.GET.get('page')
    action_lists = paginator.get_page(page)

    actions_categories = ActionsCategory.objects.all()

    # Calculate the count of action_lists
    action_lists_count = action_list.count()
    return render(request, 'actions.html', {'action_lists': action_lists,
                                            'actions_categories': actions_categories,
                                            'category': category,
                                            'action_lists_count': action_lists_count})


def single_post(request, en_slug=None, category_slug=None):
    single_post = Action.objects.filter(en_slug=en_slug).first()
    category = get_object_or_404(ActionsCategory, en_slug=category_slug)
    return render(request, 'post.html', {'single_post': single_post,
                                         'category': category})