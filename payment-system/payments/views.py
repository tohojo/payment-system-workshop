from django.shortcuts import render, redirect, get_object_or_404

from .models import Customer, Transaction

def index(request):
    return render(request, "payments/index.html")

def customer_list(request):
    # TODO: Add the list of customers as the 'customer_list' key in the context
    # dictionary
    #
    # Hint: The Customer object has a lookup function in Customer.objects.all()

    context = {"customer_list": Customer.objects.all()}
    return render(request, "payments/customer_list.html", context)

def lookup_customer(request):
    # TODO: Replace the customer_id with a lookup in the database by the card
    # number submitted by the user
    #
    # Hint: The card number is in request.POST['card_number'], and the
    # get_object_or_404() function can be used to do the lookup

    c = get_object_or_404(Customer, card_number=request.POST['card_number'])
    customer_id = c.id
    return redirect('payments:transaction_list', customer_id)

def add_customer(request):
    # TODO: Create a new Customer object based on the name and card number
    # submitted by the user
    #
    # Hint: The name is in request.POST['name'] and the card number in
    # request.POST['card_number']
    #
    # Don't forget to call the .save() method on the Customer object after it is
    # created

    c = Customer(name=request.POST['name'],
                 card_number=request.POST['card_number'])
    c.save()
    new_customer_id = c.id
    return redirect('payments:transaction_list', new_customer_id)

def transaction_list(request, customer_id):
    # TODO: Populate the context object with the customer information in the
    # 'customer' key, and the list of transactions in the 'transaction_list' key
    #
    # Hint: The get_object_or_404() function can lookup the customer based on
    # the customer_id passed to the function (using the 'pk' lookup key), and
    # the list of transactions for a customer 'c' can be accessed as
    # c.transaction_set.all()

    c = get_object_or_404(Customer, pk=customer_id)
    context = {"customer": c, "transaction_list": c.transaction_set.all()}
    return render(request, "payments/transaction_list.html", context)

def add_transaction(request, customer_id):
    # TODO: Create a new transaction for the customer based on the values
    # submitted by the user.
    #
    # Hint: The transaction description and amount are in
    # request.POST['description'] and request.POST['amount'], respectively, and
    # a customer object can add a new transaction using the
    # c.transaction_set.create() function.

    c = get_object_or_404(Customer, pk=customer_id)

    c.transaction_set.create(description=request.POST['description'],
                             amount=request.POST['amount'])
    return redirect('payments:transaction_list', customer_id)
