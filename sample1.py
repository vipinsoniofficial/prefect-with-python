from prefect import task, Task, Flow, Parameter
from prefect.tasks.control_flow.conditional import switch
from prefect.tasks.control_flow.case import case
"""
@task
def say_hello(name):
    print("hello, {}!".format(name))


with Flow("first") as flow:
    name = Parameter('name')
    say_hello(name)

flow.run(name='vipin')


class AddTask(Task):
    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, x: int, y: int=None) -> int:
        if y is None:
            y = self.default
        return x + y


add = AddTask(default=1)

with Flow("My first flow") as flow:
    first_result = add(1, y=2)
    seconf_result = add(x=first_result, y=100)


state = flow.run()
print(state)
"""

@task
def condition():
    return "b"    # returning 'b' will take the b_branch

@task
def a_branch():
    return "A Branch"

@task
def b_branch():
    return "B Branch"


"""with Flow("switch-flow") as flow:
    switch(condition, dict(a=a_branch, b=b_branch(a_branch)))
"""

with Flow("example") as flow:
    cond = condition()

    with case(cond, "a"):
        print('a')
        a_branch()
        print('aa')

    with case(cond, "b"):
        print('b')
        b_branch()

    with case(cond, "c"):
        print('c')
        a_branch()

flow.run()
