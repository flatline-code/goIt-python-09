contacts = {}

def input_error(handler):
    def wrapper(*args):
        try:
            return handler(*args)
        except Exception as e:
            error_string = e.args[0]
            if "phone()" in error_string: 
                print('enter name')
            else:
                print('enter name and phone')
    return wrapper

def stop():
    print('Good bye!')

def greeting():
    print('How can I help you?')

@input_error
def add(name, phone):
    contacts[name] = phone
    print('new contact added')

@input_error
def change(name, phone):
    if contacts.get(name):
        contacts[name] = phone
        print('contact changed')
    else:
        print('no such contact')

@input_error
def phone(name):
    if contacts.get(name):
        print(f'phone: {contacts[name]}')
    else:
        print('no such name')

def show_all():
    if not contacts:
        print('nothing to show')

    for name, phone in contacts.items():
        print(f'name: {name} | phone: {phone}')

def main():  
    commands_without_input = {
      'hello': greeting,
      'exit': stop,
      'close': stop,
      'good bye': stop,
      'show all': show_all,
    }

    commands_with_input = {
        'add': add,
        'change': change,
        'phone': phone,
    }
    
    while True:
        user_command = input('...').lower()
        user_command_with_inputs = user_command.split(' ')
        command = user_command_with_inputs[0]
        user_inputs = user_command_with_inputs[1:]

        if user_command in ['exit', 'close', 'good bye']:
            stop()
            break
        
        if commands_without_input.get(user_command):
            commands_without_input[user_command]()
            continue
        elif commands_with_input.get(command):
            commands_with_input[command](*user_inputs)
            continue
        else:
            print('unknown command')
            continue

if __name__ == '__main__':
    main()