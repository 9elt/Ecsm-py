import time

from ecsm import ECSMParser

import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def compile():
    ecsm = ECSMParser()

    # remove output files
    for file in os.listdir(".output"):
        if file.endswith(".html"):
            os.remove(os.path.join(".output", file))

    for file in os.listdir(".output/css"):
        if file.endswith(".css"):
            os.remove(os.path.join(".output/css", file))

    html_files = []
    css_files = []

    # get filenames to compile
    for file in os.listdir("src"):
        if file.endswith(".html"):
            html_files.append(file)

    for file in os.listdir("src/css"):
        if file.endswith(".css"):
            css_files.append(file)

    for filename in html_files:
        with open(f"src/{filename}", 'r') as html:

            with open(f".output/{filename}", 'w') as output:
                output.write(ecsm.html_parser(html.read()))

        for css_filename in css_files:

            with open(f"src/css/{css_filename}", 'r') as css:

                with open(f".output/css/{css_filename}", 'w') as output:
                    output.write(ecsm.css_parser(css.read()))

        ecsm.clear_states()

    print("\nsuccessfully\x1b[1m\x1b[32m compiled\x1b[0m\n---------------------")
    print("\x1b[33m\x1b[1mhtml\x1b[0m -> ", "\x1b[34m\x1b[1m"+ ", ".join(html_files) + "\x1b[0m")
    print("\x1b[33m\x1b[1mcss\x1b[0m -> ", "\x1b[34m\x1b[1m"+ ", ".join(css_files) + "\x1b[0m")

# live compiler

def compiler_error():
    print("\nunknown compiler\x1b[1m\x1b[31m error\x1b[0m")

class LiveCompiler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        try: compile()
        except: compiler_error()

    def on_created(self, event):
        if event.is_directory:
            return

        try: compile()
        except: compiler_error()

def live_compiler():
    event_handler = LiveCompiler()
    observer = Observer()

    observer.schedule(
        event_handler, 
        "src",
        recursive=True
    )

    observer.start()

    try: compile()
    except: compiler_error()

    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()