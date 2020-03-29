from model.validators import EventNameValidator, EventDateValidator

MENU_OPTIONS = [
    'List all events',
    'Search event by name',
    'Search events by description',
    'Create event',
    'Quit',
]

EVENT_OPERATION_OPTIONS = [
    'Edit',
    'Delete',
    'Back',
]

MENU_SELECTION_QUESTION = {
    'type': 'list',
    'message': '',
    'name': 'menu_selection',
    'choices': list(map(lambda menu_option: {'name': menu_option}, MENU_OPTIONS)),
}

EVENT_SELECTION_QUESTION = {
    'type': 'list',
    'message': '',
    'name': 'event_selection',
    'choices': [],
}

EVENT_OPERATION_SELECTION_QUESTION = {
    'type': 'list',
    'message': '',
    'name': 'event_operation_selection',
    'choices': list(map(lambda event_operation_option: {'name': event_operation_option}, EVENT_OPERATION_OPTIONS)),
}

EVENT_FORM = [
    {
        'type': 'input',
        'message': 'Name',
        'name': 'name',
        'default': '',
        'validate': EventNameValidator,
    },
    {
        'type': 'input',
        'message': 'Description',
        'name': 'description',
        'default': ''
    },
    {
        'type': 'input',
        'message': 'Date and time (YYYY-MM-ZZ HH:MM:SS)',
        'name': 'scheduled_time',
        'default': '',
        'validate': EventDateValidator,
    },
]

SIMPLE_INPUT_FORM = {
    'type': 'input',
    'message': '',
    'name': '',
    'default': '',
    'validate': ''
}
