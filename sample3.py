from prefect import task, Flow, Parameter
import datetime


@task
def extract_reference_data():
    print("extract_reference_data invoked... extracting the data")
    return 1


@task
def extract_live_data(a, b, c):
    print("extract_live_data invoked with A,B,C: ", a, b, c)
    return 2


@task
def transform(d):
    print("transform invoked with D: ", d)
    return 3


@task
def load_reference_data(e):
    print("load_reference_data invoked with E: ", e)
    return 4


@task
def load_live_data(f):
    print("load_live_data invoked with F: ", f)


@task(max_retries=3, retry_delay=datetime.timedelta(seconds=10))
def run_independent_task():
    x = 1
    x = x + 1
    print("***Executing Independent Task***", x)


def main():
    with Flow("etl") as flow:
        a = Parameter("a", default="[A]")
        b = Parameter("b", default="[B]")
        reference_data = extract_reference_data()
        live_data = extract_live_data(a, b, reference_data)

        #flow.add_task(extract_reference_data)
        #flow.add_task(extract_live_data(a, b, extract_reference_data))
        list = [extract_reference_data,extract_live_data(a, b, extract_reference_data)]

        flow.chain(list)


        #transformed_live_data = transform(live_data)
        #run_independent_task()
        #updated_reference_data = load_reference_data(transformed_live_data)
        #updated_live_data = load_live_data(updated_reference_data)

    flow.run()
"""
flow = Flow('etl')
a = Parameter("a", default="[A]")
b = Parameter("b", default="[B]")
reference_data = extract_reference_data()
live_data = extract_live_data(a, b, reference_data)


flow.chain(extract_reference_data,extract_live_data)
flow.run()
"""
#flow.visualize()


if __name__ == "__main__":
    main()

    """flow = Flow("test")
    flow.add_task(extract_reference_data)
    flow.add_task(extract_live_data)
    flow.run()"""



