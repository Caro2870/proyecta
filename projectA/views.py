from django.http import HttpResponse
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from django.conf import settings

def send_message(request):
    servicebus_client = ServiceBusClient.from_connection_string(settings.SERVICE_BUS_CONNECTION_STRING)
    sender = servicebus_client.get_queue_sender(settings.SERVICE_BUS_QUEUE_NAME)

    message = ServiceBusMessage("Carolina")
    sender.send_messages(message)

    return HttpResponse("Mensaje enviado.")
