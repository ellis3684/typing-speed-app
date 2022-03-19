from tkinter import Tk, ttk, Text, IntVar
from sampler import Sampler
from grader import Grader
from timer import Timer
import os


def start_typing():
    """Sets the time the user starts typing."""
    timer.set_start_time()
    input_entry.config(state='normal')
    start_button.config(state='disabled')
    global finish_button
    finish_button = ttk.Button(mainframe, text='Finish Typing', command=print_wpm)
    finish_button.grid(column=0, row=6, sticky='e')


def text_is_correct():
    """Compares the user's text with the sample text to check for correctness and completeness."""
    user_text = input_entry.get('1.0', 'end-1c')
    return grader.check_text(sampler.text, user_text)


def get_wpm():
    """Calculates the words per minute by dividing the text length by the time the user took to finish writing. The
    function loops until the user has successfully completed the test. Then, it destroys any widgets that were created
    to guide the user if the user previously made an error."""
    test_complete = False
    submit_test_widgets_exist = False
    while not test_complete:
        if text_is_correct():
            if submit_test_widgets_exist:
                error_frame.destroy()
                error_text.destroy()
                correct_text_button.destroy()
            timer.set_finish_time()
            total_time_in_seconds = timer.get_total_time()
            text_length = sampler.get_random_text_length()
            one_min_in_seconds = 60
            wpm = int(text_length // (total_time_in_seconds / one_min_in_seconds))
            return wpm
        else:
            finish_button.config(state='disabled')
            error_frame = ttk.Frame(mainframe)
            error_frame.grid(column=0, row=7, pady=20)
            error_frame.config(style='Card')
            error_text = ttk.Label(error_frame, text=f'Uh oh. Your text does not match the sample text. Your text must '
                                                     f'match the \nsample text perfectly before you can get your '
                                                     f'typing speed. \n\nHere\'s what the computer wrote:\n\n'
                                                     f'\"{grader.relevant_computer_section}\"\n\nAnd here\'s what you '
                                                     f'wrote:\n\n\"{grader.error_text}\"')
            error_text.grid(padx=10, pady=10)
            var = IntVar()
            correct_text_button = ttk.Button(
                mainframe,
                text='Submit Correction',
                style='Accent.TButton',
                command=lambda: var.set(1)
            )
            correct_text_button.grid(column=0, row=8)
            submit_test_widgets_exist = True
            correct_text_button.wait_variable(var)


def print_wpm():
    """Prints the words per minute in a label at the bottom of the window. Also creates a button that allows the user
    to restart the test if they'd like."""
    wpm = get_wpm()
    input_entry.config(state='disabled')
    finish_button.config(state='disabled')
    global wpm_frame
    wpm_frame = ttk.Frame(mainframe)
    wpm_frame.grid(column=0, row=7, pady=20)
    wpm_frame.config(style='Card')
    global wpm_text
    wpm_text = ttk.Label(wpm_frame, text=f'Your typing speed is {wpm} words per minute.')
    wpm_text.grid(padx=10, pady=10)
    create_restart_button()


def restart_test():
    """Resets class instances, resets widgets, and gets new sample text to copy."""
    sampler = Sampler()
    timer = Timer()
    guide_text.config(text=sampler.get_random_text())
    start_button.config(state='enabled')
    input_entry.config(state='normal')
    input_entry.delete('1.0', 'end-1c')
    input_entry.config(state='disabled')
    wpm_frame.destroy()
    wpm_text.destroy()
    restart_button.destroy()


def create_restart_button():
    """Creates a button that allows the user to restart the test."""
    global restart_button
    restart_button = ttk.Button(mainframe, text='Start Over', style='Accent.TButton', command=restart_test)
    restart_button.grid(column=0, row=8)



# Set up root window with Ttk theme.
current_directory = os.getcwd()
root = Tk()
root.title('Typing Speed Test App - by Corey Ellis')
style = ttk.Style(root)
root.tk.call('source', f'{current_directory}/Forest-ttk-theme-master/forest-light.tcl')
style.theme_use('forest-light')



# Create class instances.
sampler = Sampler()
timer = Timer()
grader = Grader()



# Setting main frame to hold widgets.
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, padx=40, pady=40)

header_label = ttk.Label(mainframe, text='Test Your Tempo', font=("Fixedsys", 40))
header_label.grid(column=0, row=0, pady=(10, 40))


# Setting the guide text label, frame, and label within the frame.
guide_label = ttk.Label(mainframe, text='Please type the text below as quickly and accurately as possible:')
guide_label.grid(column=0, row=1, sticky='w')

guide_frame = ttk.Frame(mainframe)
guide_frame.grid(column=0, row=2, pady=5, sticky='w')
guide_frame.config(style='Card')

guide_text = ttk.Label(guide_frame, text=sampler.get_random_text())
guide_text.grid(padx=10, pady=10)



# Setting a horizontal line separator.
separator = ttk.Separator(mainframe)
separator.grid(column=0, row=3, sticky='ew', pady=20)



# Setting the entry box for the user to type in.
input_label = ttk.Label(mainframe, text='Press \'Start Typing\' to begin, and then start typing in the box below:')
input_label.grid(column=0, row=4, sticky='w')

input_entry = Text(mainframe, width=68, height=7, state='disabled')
input_entry.grid(column=0, row=5, pady=5, sticky='w')



# Setting the buttons to start timer, stop timer, and restart with new text.
start_button = ttk.Button(mainframe, text='Start Typing', style='Accent.TButton', command=start_typing)
start_button.grid(column=0, row=6, sticky='w')





root.mainloop()
