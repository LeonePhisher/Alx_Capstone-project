from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Todo

@login_required(login_url='login')
def home(request):
    user = request.user

    if request.method == 'POST':
        task = request.POST.get('task')
        if not task:
            messages.error(request, 'Task content cannot be empty.')
            return redirect('home')

        Todo.objects.create(user=user, content=task)
        messages.success(request, 'New task saved successfully!')
        return redirect('home')

    # Tasks owned by the user
    owned_tasks = Todo.objects.filter(user=user)

    # Tasks shared with the user
    shared_tasks = Todo.objects.filter(shared_with=user)

    # Combine both
    all_tasks = (owned_tasks | shared_tasks).distinct().order_by('-timestamp')

    finished_tasks = all_tasks.filter(is_completed=True).count()
    unfinished_tasks = all_tasks.filter(is_completed=False).count()

    context = {
        'tasks': all_tasks,
        'finished_tasks': finished_tasks,
        'unfinished_tasks': unfinished_tasks,
    }

    return render(request, 'homepage/index.html', context)
@login_required(login_url='login')
def home(request):
    user = request.user

    if request.method == 'POST':
        task = request.POST.get('task')
        if not task:
            messages.error(request, 'Task content cannot be empty.')
            return redirect('home')

        Todo.objects.create(user=user, content=task)
        messages.success(request, 'New task saved successfully!')
        return redirect('home')

    # Tasks owned by the user
    owned_tasks = Todo.objects.filter(user=user)

    # Tasks shared with the user
    shared_tasks = Todo.objects.filter(shared_with=user)

    # Combine both
    all_tasks = (owned_tasks | shared_tasks).distinct().order_by('-timestamp')

    finished_tasks = all_tasks.filter(is_completed=True).count()
    unfinished_tasks = all_tasks.filter(is_completed=False).count()

    context = {
        'tasks': all_tasks,
        'finished_tasks': finished_tasks,
        'unfinished_tasks': unfinished_tasks,
    }

    return render(request, 'homepage/index.html', context)

@login_required(login_url='login')
def delete_task(request, task_id):
    
    try:
        task = Todo.objects.get(id=task_id)
        task.delete()
        messages.success(request, 'Task deleted successfully!')
    except Todo.DoesNotExist:
        messages.error(request, 'Task not found or you do not have permission to modify it.')
    return redirect('home')


@login_required(login_url='login')
def update_task_status(request, task_id):

    try:
        task = Todo.objects.get(id=task_id)
        if task.is_completed:
         task.is_completed = False
         
        else:
         task.is_completed = True
        task.save()
   
       
        messages.success(request, 'Task status updated successfully!')
    except Todo.DoesNotExist:
        messages.error(request, 'Task not found or you do not have permission to modify it.')
    return redirect('home')


@login_required(login_url='login')
def share_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)

    if request.method == 'POST':
        identifier = request.POST.get('username', '').strip()

        try:
            shared_user = User.objects.get(
                Q(username__iexact=identifier) | Q(email__iexact=identifier)
            )

            if shared_user == request.user:
                messages.error(request, "You can't share a task with yourself.")
            else:
                task.shared_with.add(shared_user)
                messages.success(
                    request, f"Task shared with {shared_user.username}"
                )

        except User.DoesNotExist:
            messages.error(
                request,
                "User not found. Enter a valid username or email."
            )

    return redirect('home')

