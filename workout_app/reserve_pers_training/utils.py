from .models import Reserve, Schedule


def get_schedule_events(trainer):
    reservations = Reserve.objects.filter(trainer=trainer)
    trainer_working_days = Schedule.objects.filter(trainer=trainer, is_working_day=True)

    events = [
        {
            "title": "Reserved",
            "start": f"{r.date}T{r.start_time}",
            "end": f"{r.date}T{r.end_time}",
            "color": "blue",
        }
        for r in reservations
    ] + [
        {
            "title": "Available",
            "start": f"{d.date}T08:00:00",
            "end": f"{d.date}T18:00:00",
            "color": "grey",
        }
        for d in trainer_working_days
    ]

    return events
