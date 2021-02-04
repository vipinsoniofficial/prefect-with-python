from prefect import Flow, task
from prefect.engine import signals
"""
@task
def signal_task(msg):
    if msg == 'go':
        print(msg)
        raise signals.SUCCESS(message='going!')
    elif msg == 'stop!':
        raise signals.FAIL(message='stopping!')
    elif msg == 'skip!':
        raise signals.SKIP(message='skipping!')


with Flow("My first flow") as flow:
    first_result = signal_task('go!')
    seconf_result = signal_task('stop!')

state = flow.run()
"""


@task
def number_task():
    print('42')
    return 42


f = Flow("example")
f.add_task(number_task)

print(f.tasks)
state = f.run()
