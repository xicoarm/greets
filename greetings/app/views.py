import requests
from django.shortcuts import redirect, render
from .models import PreOrder, Order
import datetime
import openai
import stripe
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.conf import settings  # new
from django.http.response import JsonResponse  # new
from django.views.decorators.csrf import csrf_exempt  # new
from django.views.generic.base import TemplateView




def index(request):
    template = "home.html"

    return render(request, template)


def pre_order(request):

    if request.method == 'POST':
        if 'session_id' not in request.session:
            unique_id = get_random_string(length=32)
            my_session = request.session['session_id'] = unique_id
        else:
            unique_id = request.session['session_id']

        template = "order.html"

        # check provided values

        if 'Recipient_Check' in request.POST:
            recipient = request.POST['Recipient_Check']
        else:
            recipient = "none"

        if 'Category_Check' in request.POST:
            category = request.POST.getlist('Category_Check')
        else:
            category = "none"

        created_at = datetime.datetime.now()

        if 'Text_Length' in request.POST:
            text_length = request.POST['Text_Length']
        else:
            text_length = "none"

        if 'Unique_Term' in request.POST and request.POST['Unique_Term'] != "":
            unique_term = request.POST['Unique_Term']
        else:
            unique_term = "none"

        if 'Email' in request.POST:
            email = request.POST['Email']
        else:
            email = "none"

        if 'Name' in request.POST:
            name = request.POST['Name']
        else:
            name = "none"

        PreOrder.objects.filter(unique_id=request.session['session_id']).delete()

        pre_order = PreOrder(email=email, name=name, created_at=created_at, recipient=recipient, category=category,
                             text_length=text_length, unique_term=unique_term, unique_id=unique_id)
        pre_order.save()

        context = {
            'email': email,
            'name': name,
            'created_at': created_at,
            'recipient': recipient,
            'category': category,
            'text_length': text_length,
            'unique_term': unique_term,
            'unique_id': unique_id
        }

    else:
        params_for_question = PreOrder.objects.filter(unique_id=request.session['session_id']).first()
        context = {
            'email': getattr(params_for_question, "email"),
            'name': getattr(params_for_question, "name"),
            'created_at': getattr(params_for_question, "created_at"),
            'recipient': getattr(params_for_question, "recipient"),
            'category': getattr(params_for_question, "category"),
            'text_length': getattr(params_for_question, "text_length"),
            'unique_term': getattr(params_for_question, "unique_term"),
            'unique_id': getattr(params_for_question, "unique_id")
        }

    template = "checkout.html"

    return render(request, template, context)





@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):

    params_for_question = PreOrder.objects.filter(unique_id=request.session['session_id']).first()

    email = getattr(params_for_question, "email")
    name = getattr(params_for_question, "name")
    created_at = getattr(params_for_question, "created_at")
    recipient = getattr(params_for_question, "recipient")
    category = getattr(params_for_question, "category")
    text_length = getattr(params_for_question, "text_length")
    unique_term = getattr(params_for_question, "unique_term")
    unique_id = getattr(params_for_question, "unique_id")

    count = 1
    print(category)
    print(text_length)
    print("unique")
    print(unique_term)

    if category != 'none':
        count = count + 1

    if text_length != 'none':
        if text_length == "Text_Length400":
            count = count + 2
        if text_length == "Text_Length200":
            count = count + 1
        if text_length == "Text_Length800":
            count = count + 3

    if unique_term != "none":
       count = count + 2


    if count == 1:
        if request.method == 'GET':
            domain_url = 'http://localhost:8000/'
            stripe.api_key = settings.STRIPE_SECRET_KEY

            try:

                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}/&' + 'sp=' + request.session[
                        'session_id'],
                    cancel_url=domain_url + 'cancelled/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'name': 'Greets',
                            'quantity': 1,
                            'currency': 'chf',
                            'amount': '190',
                        }
                    ]
                )



                return JsonResponse({'sessionId': checkout_session['id'], 'request': request.session['session_id']})

            except Exception as e:
                return JsonResponse({'error': str(e)})


    if count == 2:

        if request.method == 'GET':
            domain_url = 'http://localhost:8000/'
            stripe.api_key = settings.STRIPE_SECRET_KEY

            try:

                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}/&' + 'sp=' + request.session[
                        'session_id'],
                    cancel_url=domain_url + 'cancelled/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'name': 'Greets',
                            'quantity': 1,
                            'currency': 'chf',
                            'amount': '290',
                        }
                    ]
                )

                return JsonResponse({'sessionId': checkout_session['id'], 'request': request.session['session_id']})

            except Exception as e:
                return JsonResponse({'error': str(e)})


    if count == 3:

        if request.method == 'GET':
            domain_url = 'http://localhost:8000/'
            stripe.api_key = settings.STRIPE_SECRET_KEY

            try:

                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}/&' + 'sp=' + request.session[
                        'session_id'],
                    cancel_url=domain_url + 'cancelled/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'name': 'Greets',
                            'quantity': 1,
                            'currency': 'chf',
                            'amount': '390',
                        }
                    ]
                )

                return JsonResponse({'sessionId': checkout_session['id'], 'request': request.session['session_id']})

            except Exception as e:
                return JsonResponse({'error': str(e)})



    if count == 4:

        if request.method == 'GET':
            domain_url = 'http://localhost:8000/'
            stripe.api_key = settings.STRIPE_SECRET_KEY

            try:

                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}/&' + 'sp=' + request.session[
                        'session_id'],
                    cancel_url=domain_url + 'cancelled/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'name': 'Greets',
                            'quantity': 1,
                            'currency': 'chf',
                            'amount': '490',
                        }
                    ]
                )

                return JsonResponse({'sessionId': checkout_session['id'], 'request': request.session['session_id']})

            except Exception as e:
                return JsonResponse({'error': str(e)})




    if count == 5:

        if request.method == 'GET':
            domain_url = 'http://localhost:8000/'
            stripe.api_key = settings.STRIPE_SECRET_KEY

            try:

                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}/&' + 'sp=' + request.session[
                        'session_id'],
                    cancel_url=domain_url + 'cancelled/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'name': 'Greets',
                            'quantity': 1,
                            'currency': 'chf',
                            'amount': '590',
                        }
                    ]
                )

                return JsonResponse({'sessionId': checkout_session['id'], 'request': request.session['session_id']})

            except Exception as e:
                return JsonResponse({'error': str(e)})


    if count == 6:

        if request.method == 'GET':
            domain_url = 'http://localhost:8000/'
            stripe.api_key = settings.STRIPE_SECRET_KEY

            try:

                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}/&' + 'sp=' + request.session[
                        'session_id'],
                    cancel_url=domain_url + 'cancelled/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'name': 'Greets',
                            'quantity': 1,
                            'currency': 'chf',
                            'amount': '690',
                        }
                    ]
                )

                return JsonResponse({'sessionId': checkout_session['id'], 'request': request.session['session_id']})

            except Exception as e:
                return JsonResponse({'error': str(e)})


class SuccessView(TemplateView):

    def get(self, request):
        session_key = request.GET['sp']
        print(request.GET['sp'])


        ##### create question

        params_for_question = PreOrder.objects.filter(unique_id=session_key).first()

        #if getattr(params_for_question, "already_sent") != 1:


        print(params_for_question)

        email = getattr(params_for_question, "email")
        name = getattr(params_for_question, "name")
        created_at = getattr(params_for_question, "created_at")
        recipient = getattr(params_for_question, "recipient")
        category = getattr(params_for_question, "category")
        text_length = getattr(params_for_question, "text_length")
        unique_term = getattr(params_for_question, "unique_term")
        unique_id = getattr(params_for_question, "unique_id")

        print(text_length)
        print(recipient)
        print(unique_term)

        if category != "none":
            print(category)

        if text_length != "none":
            text_length = 350

        if recipient == "none" and unique_term == "none":
            type1 = "I want a message in german that contains at least" + str(text_length) + "characters to felicitate the new year of someone."
            user_input = type1

        if recipient == "none" and unique_term != "none":
            type2 = "I want a message in german that contains at least" + str(text_length) + "characters to felicitate the new year of someone. The message must be related to the term " + unique_term + "."
            user_input = type2

        if recipient != "none" and unique_term != "none":
            type3 = "I want a message in german that contains at least" + str(text_length) + "characters to felicitate the new year of my " + recipient + " . The message must be related to the term " + unique_term + "."
            user_input = type3

        if recipient != "none" and unique_term == "none":
            type4 = "I want a message in german that contains at least" + str(text_length) + "characters to felicitate the new year of my " + recipient + "."
            user_input = type4

        user_input = "I want a long message in german that contains at least characters to felicitate the new year of someone."


        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            temperature=0.1,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response = (response["choices"][0]["text"])
        dict = {'response': response}


        #create order and save

        order = Order(email=email, name=name, created_at=created_at, recipient=recipient, category=category,
                             text_length=text_length, unique_term=unique_term, unique_id=unique_id)
        order.save()

        pre_order = PreOrder.objects.get(unique_id=session_key)
        pre_order.already_sent = 1
        pre_order.save()

        return render(request, 'success.html', dict)

        #else:
            #return render(request, 'home.html')


