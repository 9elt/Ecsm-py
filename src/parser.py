from bs4 import BeautifulSoup

def str_to_html(string):
    return BeautifulSoup(string, 'html.parser')

class ECSMParser:

    def __init__(self):
        self.default_css = '.ECSM-state { display: none !important }\n\n'
        self.BOOL_states = []
        self.OPT_states = {}

    def state_ID(self, state_type, state_name):
        return f'ECSM-{state_type}-ID_{state_name}'

    def state_KEY(self, state_type, key_name):
        return f'ECSM-{state_type}-KEY_{key_name}'

    def BOOL_input(self, ID):
        return str_to_html(f'<input class="ECSM-state" type="checkbox" id="{ID}"/>')

    def OPT_input(self, ID,  KEY):
        return str_to_html(f'<input class="ECSM-state" type="radio" name={ID} id="{KEY}"/>')

    def clear_states(self):
        self.BOOL_states = []
        self.OPT_states = {}

    def html_parser(self, html):

        document = BeautifulSoup(html, 'html.parser')
        state_handlers = document(handle_state=True)

        # state handlers parser
        for handler in state_handlers:

            if handler["handle_state"] == "":
                continue
    
            state = handler["handle_state"].split(":")

            ID = state[0]
            KEY = state[1] if len(state) > 1 else None

            state_type = "bool" if len(state) == 1 else "opt"

            ECSM_id = ""

            if state_type == "bool":

                ECSM_id = self.state_ID(state_type, ID)

                if ID not in self.BOOL_states:
                    self.BOOL_states.append(ID)

            elif state_type == "opt":

                ECSM_id = self.state_KEY(state_type, KEY)

                if ID in self.OPT_states:
                    self.OPT_states[ID].append(KEY)
                else:
                    self.OPT_states[ID] = [KEY]

            del handler["handle_state"]

            label = f'<label for="{ECSM_id}">{handler}</label>'

            handler.replace_with(str_to_html(label))

        # create <inputs/> for boolean states
        for state in self.BOOL_states:

            ECSM_id = self.state_ID("bool", state)

            document.body.insert(0, self.BOOL_input(ECSM_id))

        # create <inputs/> for option states
        for name in self.OPT_states:

            ECSM_id = self.state_ID("opt", name)

            for key in self.OPT_states[name]:

                ECSM_key = self.state_KEY("opt", key)

                document.body.insert(0, self.OPT_input(ECSM_id, ECSM_key))

        # stringify
        return str(document)

    def css_parser(self, css):

        # boolean states
        for state in self.BOOL_states:

            ECSM_id = self.state_ID("bool", state)

            css = css.replace(f'{state}:active ', f'#{ECSM_id}:checked~* ')
            css = css.replace(f'{state}:active', f'#{ECSM_id}:checked~')

        # option states
        for name in self.OPT_states:
            for key in self.OPT_states[name]:

                ECSM_key = self.state_KEY("opt", key)

                css = css.replace(f'{name}:{key} ', f'#{ECSM_key}:checked~* ')
                css = css.replace(f'{name}:{key}', f'#{ECSM_key}:checked~')

        return self.default_css + css
