import datetime

to_do_list = {}

def list_tasks(date):
		if d in to_do_list:
        print(f'Tasks for {date}:\n{"\n".join(to_do_list[date])}')
    else:
        print(f'There is no tasks as of {date}')
        
def add_task(date):
    task = input('Type new task here:\n')
    to_do_list.get(d, []).append(task)
    print(f'Tasks for {requested_date}:\n' + '\n'.join(to_do_list[date]))

def repeat():
    while True:
        rep = input('Repeat? (Y/N)\n').upper()
        if rep == 'Y':
            return False
        elif rep == 'N':
            exit()


def is_valid_operation(operation):
    if operation in ('1', '2'):
    		return True
    print('Operation type is incorrect')
    return repeat()

def input_date():
    requested_date = input('Date? (valid formats: ddmmyyyy, dd-mm-yyyy, dd/mm/yyyy, dd.mm.yyyy; if empty - than date is today)\n')
    return ''.join(e for e in requested_date.replace(' ', '') if e.isdigit())


def is_valid_date(date):
    if not date:
        return datetime.date.today().strftime("%d.%m.%Y")
    try:
        d = datetime.strptime(requested_date, "%d%m%Y").strftime("%d.%m.%Y")
        return date
    except ValueError:
        print('Input date is incorrect!')
        return repeat


def to_do():
    while True:
        
        oper_type = input(
        '''What do you want to do? ("1" - get tasks by date; "2" - post new task
        '''
        ).strip()
        
        if not is_valid_operation(oper_type):
        		continue
        
        requested_date = is_valid_date(input_date())
        if not requested_date:
        		continue
                
        if oper_type == '1':
            list_tasks(requested_date)
        elif oper_type == '2':
						add_task(requested_date)  
            
        repeat()
        