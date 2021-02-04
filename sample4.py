from prefect import task, Flow

dict = {'fullname': ''}


@task
def users_name(name):
    print("hello, {}!".format(name))
    return name


@task
def user_fullname(name, lname):
    fullname = name + " " + lname
    print("fullname:", fullname)
    dict['fullname'] = fullname
    return fullname


@task
def user_age(name, age):
    print('Name:', name)
    print('Your age:', age)
    return age


@task
def user_city(city):
    print('Your city:', city)
    return city


@task
def user_country(country):
    print('Your country:', country)
    return country


def task_to_run():
    print("t1: name \nt2: fullname \nt3: age \nt4: city \nt5: country")

    print("which tasks you want to run?")
    access = True
    value = []
    while access:
        input1 = input("enter task name:")
        value.append(input1)

        exit = input("are you done?(y/n)")
        if exit.lower() == 'y':
            break
        else:
            continue

    return value


def main(fname, lname, age, city, country):
    if fname and lname and age and city and country:
        with Flow("first") as flow:

            tasks = task_to_run()
            task_list = []

            if tasks:
                for value in tasks:
                    if value == 't1':
                        task_list.append(users_name(fname))

                    elif value == 't2':
                        task_list.append(user_fullname(fname, lname))

                    elif value == 't3':
                        task_list.append(user_age(dict['fullname'], age))

                    elif value == 't4':
                        task_list.append(user_city(city))

                    elif value == 't5':
                        task_list.append(user_country(country))

                    else:
                        print('task not found')

            else:
                print('enter value')

            flow.chain(task_list)

        #flow.run()
        task_ref = flow.get_tasks()[0]
        print('task_ref', task_ref)
        state = flow.run()
        print('state',state)
        result = state.result[task_ref]._result
        print(result)


if __name__ == "__main__":
    main("vipin", "soni", "24", "jaipur", "India")
    print(dict['fullname'])

    
    """
    print('enter value:')
    name = input("enter firstname:")
    lastname = input("enter lastname:")
    age = input("enter age:")
    city = input("enter city:")
    country = input("enter country:")
    print(name, lastname, age, city, country)
    """
