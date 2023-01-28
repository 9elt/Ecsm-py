def config_template(name):
    return f'''\
{{
    "name": "{name}"
}}
'''

def html_template(name):
    return f'''\
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
    <link rel="stylesheet" href="css/main.css">
</head>

<body>

</body>

</html>
'''

def css_template(name):
    return f'''\
/*
ECSM | Easy Css State Manager

usage:

boolean_state_name:active .targeted_class {{
    ...css style
}}

option_state_name:active_option_name .targeted_class {{
    ...css style
}}

*/
'''