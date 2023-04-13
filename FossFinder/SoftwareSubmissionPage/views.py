from django.shortcuts import render
from .models import SubmittedSoftware
from .forms import SubmitSoftwareForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django import forms
from .models import SubmittedSoftware

# Create your views here.
def software_submit(request):
    form = SubmitSoftwareForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = SubmitSoftwareForm()

    return render(request, 'software_submit.html', {'form':form})

def software_submit_detail(request, pk):
    software = SubmittedSoftware.objects.get(pk=pk)
    context = {
        'SubmittedSoftware': software
    }
    return render(request, 'software_submit_detail.html', context)

class MyForm(forms.Form):
    def define_form():
        CHOICES = [(i, str(i)) for i in range(6)]
        dropdown = forms.ChoiceField(choices=CHOICES)

    def test_dropdown_menu_is_zero(self):
        data = {'my_dropdown': 0}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.cleaned_data['my_dropdown'], 0)
        
        # Set the value to a non-zero value and verify it's no longer 0
        data = {'my_dropdown': 3}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertNotEqual(form.cleaned_data['my_dropdown'], 0)

    def test_dropdown_menu_is_one(self):
        data = {'my_dropdown': 1}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.cleaned_data['my_dropdown'], 1)
        
        # Set the value to a non-one value and verify it's no longer 1
        data = {'my_dropdown': 3}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertNotEqual(form.cleaned_data['my_dropdown'], 1)

    def test_dropdown_menu_is_two(self):
        data = {'my_dropdown': 2}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.cleaned_data['my_dropdown'], 2)
        
        # Set the value to a non-two value and verify it's no longer 2
        data = {'my_dropdown': 3}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertNotEqual(form.cleaned_data['my_dropdown'], 2)

    def test_dropdown_menu_is_three(self):
        data = {'my_dropdown': 3}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.cleaned_data['my_dropdown'], 3)
        
        # Set the value to a non-three value and verify it's no longer 3
        data = {'my_dropdown': 2}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertNotEqual(form.cleaned_data['my_dropdown'], 3)

    def test_dropdown_menu_is_four(self):
        data = {'my_dropdown': 4}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.cleaned_data['my_dropdown'], 4)
        
        # Set the value to a non-four value and verify it's no longer 4
        data = {'my_dropdown': 3}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertNotEqual(form.cleaned_data['my_dropdown'], 4)

    def test_dropdown_menu_is_five(self):
        data = {'my_dropdown': 5}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.cleaned_data['my_dropdown'], 5)
        
        # Set the value to a non-five value and verify it's no longer 5
        data = {'my_dropdown': 4}
        form = MyForm(data=data)
        self.assertEqual(form.is_valid(), True)
        self.assertNotEqual(form.cleaned_data['my_dropdown'], 5)

class MyView(FormView):
    form_class = MyForm
    template_name = 'my_template.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Do something with the form data
        return super().form_valid(form)
    
    def my_function(self):
        # Function code here
        pass

view = MyView()
view.my_function()