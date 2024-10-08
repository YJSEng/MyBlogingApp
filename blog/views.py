from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .models import Post,Comment
from .forms import EmailPostForm,CommentForm,SubmitForm
from django.core.mail import send_mail,EmailMessage
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(request, 'blog/post/comment.html',
                           {'post': post,
                            'form': form,
                            'comment': comment})
class PostListView(ListView):

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
# Create your views here.

def post_submit(request):
    if request.method == 'POST':
        # Handle form submission
        form = SubmitForm(request.POST,request.FILES)
        if form.is_valid():
            # Process the form data (e.g., save, send email)
            # Redirect to a success page or another view
            prepopulated_fields = {'slug': ('title',)}
            post = form.save(commit=False)
          #  post.author = request.user 
            post.save()
            email = EmailMessage(
                subject='New Post Submission: Awaiting Approval',  # Email subject
                body=f'Post Title: {post.title}\n\nPost Author: {post.author}\n\nPlease review and approve this post.',  # Email body
                from_email=settings.DEFAULT_FROM_EMAIL,  # From email (configured in settings)
                to=['yawarjaleesshamsi@gmail.com'],  # Main recipient email
                cc=[post.email],  # CC recipient(s)
            )
            
            # Send the email
            email.send(fail_silently=False)


          #  return redirect('blog:post_list')  
            messages.success(request, 'Thanks for submitting the post. It is sent for admin approval and will be viewed once approved.')
            return redirect('blog:post_list')
        
        else:
            print(form.errors) 
        # Example success redirect
    else:
        # Show an empty form for GET request
        form = SubmitForm()
    
    # Render the form in the template
    return render(request, 'blog/post/share1.html', {'form': form})

def post_list(request,post):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
         # If page_number is out of range deliver last page of results
     posts = paginator.page(paginator.num_pages)
    except EmptyPage:
         # If page_number is out of range deliver last page of results
     posts = paginator.page(paginator.num_pages)
    comments = post.comments.filter(active=True)
    
    return render(request,
 'blog/post/list.html',
                 {'posts': posts,
                  })

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
     # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()
    return render(request,
 'blog/post/detail.html',
                  {'post': post,
                   'comments':comments,
                   'form':form})
def post_share(request, post_id):
 # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent=False
    if request.method == 'POST':
 # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
    # Form fields passed validation
                cd = form.cleaned_data
                post_url = request.build_absolute_uri(
                    post.get_absolute_url())
                subject = f"{cd['name']} recommends you read " \
                        f"{post.title}"
                message = f"Read {post.title} at {post_url}\n\n" \
                        f"{cd['name']}\'s comments: {cd['comments']}"
                send_mail(subject, message, 'yawarjaleesshamsi@gmail.com',
                        [cd['to']])
                sent = True
 # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
 'form': form,
 'sent':sent})

