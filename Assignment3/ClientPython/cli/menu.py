import copy

from cli.options import MENU_SELECTION_QUESTION, EVENT_SELECTION_QUESTION, \
    EVENT_OPERATION_SELECTION_QUESTION, EVENT_FORM, SIMPLE_INPUT_FORM
from model.validators import EventNameValidator, EventDescriptionValidator


def get_start_question():
    return MENU_SELECTION_QUESTION


def get_event_selection_question(events):
    events_selection_list = [{'name': stringify_event(index, event)} for index, event in enumerate(events, start=1)]
    events_selection_list.append({'name': 'Back'})

    event_selection_question = copy.deepcopy(EVENT_SELECTION_QUESTION)
    event_selection_question['choices'] = events_selection_list

    return event_selection_question


def get_event_operation_selection_question():
    return EVENT_OPERATION_SELECTION_QUESTION


def get_event_creation_form():
    return EVENT_FORM


def get_event_edit_form(event):
    event_form = copy.deepcopy(EVENT_FORM)
    event_form[0]['default'] = event.name
    event_form[1]['default'] = event.description
    event_form[2]['default'] = event.scheduled_time

    return event_form


def get_event_name_form():
    event_name_form = copy.deepcopy(SIMPLE_INPUT_FORM)
    event_name_form['name'] = 'name'
    event_name_form['message'] = 'Name'
    event_name_form['validate'] = EventNameValidator

    return event_name_form


def get_event_description_form():
    event_name_form = copy.deepcopy(SIMPLE_INPUT_FORM)
    event_name_form['name'] = 'description'
    event_name_form['message'] = 'Description'
    event_name_form['validate'] = EventDescriptionValidator

    return event_name_form


def stringify_event(index, event):
    return str(index) + '. ' + event.name + ' | Date: ' + str(event.scheduled_time)


def extract_event_name(event_selection_answer):
    name_start_index = event_selection_answer.find('.') + 2
    name_end_index = event_selection_answer.find(' | ')
    return event_selection_answer[name_start_index:name_end_index]
