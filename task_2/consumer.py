import pika
import json
from models import Contact


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue', durable=True)

    def send_email(email):
        print(f'Sending email to {email}...')

    def callback(ch, method, properties, body):
        data = json.loads(body)
        contact_id = data['contact_id']

        contact = Contact.objects.get(id=contact_id)

        if contact and not contact.message_sent:
            send_email(contact.email)
            contact.message_sent = True
            contact.save()
            print(f"Email sent to {contact.fullname} ({contact.email})")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='email_queue', on_message_callback=callback)

    print("Consumer is waiting for messages... Press CTRL+C to exit.")

    channel.start_consuming()


if __name__ == '__main__':
    main()
