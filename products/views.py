from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Book,Review
from .forms import AddReviewForm,UpdateReviewForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
from django.contrib import messages
# Create your views here.

# class ListView(View):
#     def get(self,request):
#         book=Book.objects.all().order_by('-pk')
#         return render(request, 'book/book_list.html',{'book':book})

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        reviews = Review.objects.filter(book=pk)
        context = {
            'book': book,
            'reviews': reviews
        }

        return render(request, 'book/book_detail.html', context=context)


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_detail.html'
    success_url = reverse_lazy('products:book_list')

class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        books = Book.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'books': books,
            'add_review_form': add_review_form
        }
        return render(request, 'book/add_review.html', context=context)

    def post(self, request, pk):
        books = Book.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                book=books,
                user=request.user,
                rating=add_review_form.cleaned_data['rating']
            )

            review.save()
            messages.success(request, "Comment qo'shildi.")
            return redirect('products:book_detail', pk=pk)
        
class ReviewDeleteView(View):
    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        book_pk = review.book.pk
        review.delete()
        messages.success(request, "Comment o'chirildi.")
        # messages.error(request, "Comment o'chirilmadi")
        return HttpResponseRedirect(reverse_lazy('products:book_detail', kwargs={'pk': book_pk}))

class ReviewUpdateView(View):
    def get(self, request, pk):
        data = Review.objects.get(pk=pk)
        update_form=UpdateReviewForm(instance=data)
        return render(request, 'book/update_review.html', {'form': update_form})    
    def post(self, request, pk):
        update = Review.objects.get(pk=pk)
        update_form = UpdateReviewForm(request.POST, instance=update)
        if update_form.is_valid():
            update_review = update_form.save(commit=False)
            update_review.book_id = update.book_id
            update_review.save()
            messages.success(request, "Comment o'zgartirildi.")
            return redirect('products:book_detail', pk=update.book_id)  # Corrected redirect with the book's pk
        else:
            messages.error(request, "Comment o'zgartirilmadi.")
            return render(request, 'book/update_review.html', {'form': update_form})  # Corrected context dictionary


