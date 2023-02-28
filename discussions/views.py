from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
from django.contrib import messages

from django.views.generic import ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.dates import timezone_today
from discussions.models import Discussion
from .forms import DiscussionCreateForm
from django.contrib.auth.decorators import login_required

from blog.models import Post


# Create your views here.
class UserDiscussionListView(ListView):
    # Post model in models.py
    model = Discussion
    # html name templates
    template_name = 'discussions/user_discussions.html'

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Discussion.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['discussions_post_user_list'] = queryset.order_by('-date_created')
        return context


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussions/discussion_detail.html'
    context_object_name = 'discussion_detail'


@login_required
def discussion_create(request):
    # if Post request - process the form
    if request.method == 'POST':
        # create a form's instance and insert it request's datas
        # create a form for editing
        form = DiscussionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion.author = request.user
            new_discussion.save()

            messages.success(request, 'Discussion added successfully')
            return redirect(new_discussion.get_absolute_url())

    else:
        # if a get-request (or any other) comes, return an empty form
        form = DiscussionCreateForm()
    return render(request, 'discussions/create_form.html', {'form': form})
