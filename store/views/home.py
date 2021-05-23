from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView
from customers.models import Customer
from store.forms import NewCommentForm
from store.models import Product, Comment
from store.models import Category




class Home(View):
    def get(self,request):
        customer = Customer.objects.get(customer=request.user)
        request.session["customer"] = customer.id
        cart = request.session.get('cart')
        categories = Category.getAllCategory()
        products = Product.getAllProduct().order_by('-id')

        if request.GET.get('id'):

            filterProductById = Product.objects.get(id=int(request.GET.get('id')))
            return render(request, 'productDetail.html',{"product":filterProductById,"categories":categories})

        if not cart:
            request.session['cart'] = {}

        if request.GET.get('category_id'):
            filterProduct = Product.getProductByFilter(request.GET['category_id'])
            return render(request, 'home.html',{"products":filterProduct,"categories":categories})

        return render(request, 'home.html',{"products":products,"categories":categories})

    def post(self,request):
        product = request.POST.get('product')

        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        print(cart)
        request.session['cart'] = cart
        return redirect('cart')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'productDetail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        #user = self.request.session.get('customer')
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(product_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        #customer = Customer.objects.get(id=user)
        data['form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        print(str(self.request.user) +"  posting a comment")
        customer = Customer.objects.get(customer=self.request.user)
        new_comment = Comment(text=request.POST.get('text'),
                              author=self.request.user,
                              product_connected=self.get_object(),
                              image=customer.image)

        new_comment.save()

        return self.get(self, request, *args, **kwargs)



class CommentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    success_url = '/'
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


