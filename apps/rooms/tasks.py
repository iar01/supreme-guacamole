from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from datetime import datetime
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from apps.rooms.models import Booking
from datetime import datetime, timedelta


@shared_task(bind=True)
def automated(self):
    now = datetime.now()
    reminder_time_window = now + timedelta(minutes=15)  # Target 15 minutes in the future

    # Fetch relevant bookings
    upcoming_bookings = Booking.objects.filter(
        start_time__gte=now,
        start_time__lte=reminder_time_window
    )

    if not upcoming_bookings:
        return "No upcoming bookings found within the next 15 minutes"

    htmly = get_template('reminder.html')

    # Iterate and send emails
    for booking in upcoming_bookings:
        data = {
            'name': booking.name,
            'start_time': booking.start_time,
            'end_time': booking.end_time,
            'room_name': booking.room.room_name,
            'room_number': booking.room.room_number,
            'floor': booking.room.floor.floor_name,
            'building': booking.room.floor.building.name
        }

        subject = f"Greetings {booking.name} - Reminder of your today's booking"
        from_email = 'test@outlook.com'
        to = booking.Email

        html_content = htmly.render(data)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    return f"Reminder emails sent for {len(upcoming_bookings)} bookings"
