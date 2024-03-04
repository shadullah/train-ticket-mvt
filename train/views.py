from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import AddTrainForm,TrainInfoUpdateForm
from django.urls import reverse_lazy
from .models import Train_list

# Create your views here.
class Add_trainView(FormView):
    template_name= 'train/add_train.html'
    form_class = AddTrainForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        add_train = form.save()
        print(add_train)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Add_trainView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the trains
        context['trains'] = Train_list.objects.all()
        return context

    
def train_list(req):
    data= Train_list.objects.all()
    return render(req, 'train/train_list.html', {'trains': data})

def editTrainInfo(req,id):
    train = Train_list.objects.get(pk=id)
    edit_form = TrainInfoUpdateForm(instance=train)

    if req.method=='POST':
        edit_form = TrainInfoUpdateForm(req.POST,instance=train)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
        else:
            print("error")
    return render(req, 'train/edit_train.html', {'form':edit_form})


def delete_train(req,id):
    data= Train_list.objects.get(pk=id)
    data.delete()
    return redirect('add_train')



