import tkinter as tk
from tkinter import font

import pronk_sheet

error_message = None
def button_click_command():
    stock_tickers_input = stock_tickers.get()
    print('stock_tickers_input: {}'.format(stock_tickers_input))
    api_key_input = api_key.get()
    print('api_key_input: {}'.format(api_key_input))

    if not stock_tickers_input or not api_key_input:
        error_message['bg'] = 'red'
        error_message['text'] = 'Both inputs must be filled!'
    else:
        error_message['bg'] = 'lime'
        error_message['text'] = 'Program has finished running'
        pronk_sheet.execute(stock_tickers_input, api_key_input)

window = tk.Tk()
frame = tk.Frame(master=window)

greeting = tk.Label(
    master=frame,
    text="Hey there! This is fun, I've never written a GUI in python before\n",
)

label_font = font.Font(name='appHighlightFont', size=8)
api_key_label = tk.Label(
    master=frame,
    font=label_font,
    text='''
Enter any string here for api key.
I.e. 'fdfd' will work.
***CHANGE THIS EVERY TIME YOU RUN THE PROGRAM***.
This will fail without error if you use the same key too much due to api restriction for stock data.
'''
)
api_key = tk.Entry(master=frame, width=50)
stock_tickers_label = tk.Label(
    master=frame,
    font=label_font,
    text='''
Enter comma separate, no spaces, stock tickers. Every stock you type will add
1 minute to program execution, since this 'free' stock api only allows 5 calls
per minute. I.e. 'APHA,CGC,ACB', which would take ~3 minutes to run
'''
)
stock_tickers = tk.Entry(master=frame, width=50)

button = tk.Button(
    command=button_click_command,
    master=frame,
    text="Start Program",
    width=25,
    height=1,
    bg="black",
    fg="white",
)

button_subtext_font = font.Font(name='buttonSubtextFont', size=12)
button_subtext = tk.Label(
    master=frame,
    font=label_font,
    text='''
**Make sure excel file from last run is closed before re-running or this will fail**
***When program is running, please be patient.  There is no feedback, excel will open when it's ready***
''',
    bg="pink",
    fg="black",
)

error_message_font = font.Font(name='errorFont', size=8)
error_message = tk.Label(
    master=frame,
    font=label_font,
    text=''
)

disclaimer_font = font.Font(name='disclaimerFont', size=11, weight='bold')
disclaimer_label = tk.Label(
    master=frame,
    font=disclaimer_font,
    text='''
Disclaimer/Warning.  This underlying API supplying this data is good,
but I have found examples of the following:
- missing quarterly report for Corsair, causes computation errors
- Some 'smaller' stocks don't seem to exist.

I need to do more data digging but this doesn't concern me much overall
it performs very well/saves tons of time/and is very accurate and more
accurate than yahoo finance
'''
)

greeting.pack()
api_key_label.pack()
api_key.pack()
stock_tickers_label.pack()
stock_tickers.pack()
api_key_label.pack()
button.pack()
button_subtext.pack()
error_message.pack()
disclaimer_label.pack()
frame.pack()
window.mainloop()
