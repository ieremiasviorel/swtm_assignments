import sys
from pprint import pprint
from PyInquirer import prompt
from cli.menu import get_start_question, get_event_selection_question, \
    get_event_operation_selection_question, extract_event_name, get_event_edit_form, get_event_name_form, \
    get_event_description_form, get_event_creation_form
from proxy.proxy import Proxy


def handle_cli_start():
    menu_selection_answer = prompt(get_start_question())['menu_selection']
    handle_menu_selection(menu_selection_answer)


def handle_menu_selection(menu_selection_answer):
    if menu_selection_answer == 'List all events':
        events = proxy.events_list()
        handle_show_list_of_events(events)
    if menu_selection_answer == 'Search event by name':
        event_name_answer = handle_event_name_input()
        event_name = event_name_answer['name']
        events = proxy.events_list_by_name(event_name)
        handle_show_list_of_events(events)
    if menu_selection_answer == 'Search events by description':
        event_description_answer = handle_event_description_input()
        event_description = event_description_answer['description']
        events = proxy.events_list_by_description(event_description)
        handle_show_list_of_events(events)
    elif menu_selection_answer == 'Create event':
        handle_event_creation()
    elif menu_selection_answer == 'Quit':
        exit(0)


def handle_show_list_of_events(events):
    event_selection_answer = prompt(get_event_selection_question(events))[
        'event_selection']
    handle_event_selection_answer(events, event_selection_answer)


def handle_event_creation():
    answers = prompt(get_event_creation_form())
    proxy.event_add(answers['name'],
                    answers['description'], answers['scheduled_time'])
    handle_menu_selection('List all events')


def handle_event_selection_answer(events, event_selection_answer):
    if event_selection_answer == 'Back':
        handle_cli_start()

    selected_event_name = extract_event_name(event_selection_answer)
    selected_event = next(
        event for event in events if event.name == selected_event_name)
    pprint(selected_event.description)

    event_operation_selection_answer = prompt(
        get_event_operation_selection_question())['event_operation_selection']

    if event_operation_selection_answer == 'Edit':
        handle_event_edit(selected_event)
    elif event_operation_selection_answer == 'Delete':
        handle_event_delete(selected_event)
    elif event_operation_selection_answer == 'Back':
        handle_menu_selection('List all events')


def handle_event_edit(event):
    original_event_name = event.name
    answers = prompt(get_event_edit_form(event))
    proxy.event_edit(original_event_name,
                     answers['name'], answers['description'], answers['scheduled_time'])
    handle_menu_selection('List all events')


def handle_event_delete(event):
    proxy.event_delete(event.name)
    handle_menu_selection('List all events')


def handle_event_name_input():
    return prompt(get_event_name_form())


def handle_event_description_input():
    return prompt(get_event_description_form())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urlServ = sys.argv[1]
    else:
        urlServ = "http://localhost/Xh1Serv.php"

    proxy = Proxy(urlServ)

    print("**********************************************")
    print("***  Welcome to Events Agenda Application  ***")
    print("**********************************************")

    handle_cli_start()
