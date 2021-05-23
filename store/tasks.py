
from celery import shared_task

from djcelery_email.tasks import send_email

from Sondo_shopping.settings import EMAIL_HOST_USER
from customers.models import Customer
from store.models import Order


@shared_task
def OrderEmail(order_id=None):
    order = Order.objects.get(id=order_id)
    customer = Customer.objects.get(id=order.customer.id)
    send_email(
        'Order on Sondo_shopping',
        'Thank You for placing Order, %s on its way.' % order.product.name,
        EMAIL_HOST_USER,
        [customer.customer.email],
        fail_silently=False,
    )



