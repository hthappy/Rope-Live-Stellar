import os
import sys

def get_media_path(filename):
    """获取媒体文件的绝对路径"""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, 'rope', 'media', filename)

bg = 'black'
main = '#1A1A1A' #Not as Dark Grey '#1A1A1A'
main2 = '#151515' #Dark Grey '#151515'
main3 = '#28282E' #Light Grey '#28282E'

canvas_frame_label_1 = {
    'bg':                       main2,
    'bd':                       '0',
    'relief':                   'flat',
    'highlightthickness':       '0'
    }

canvas_frame_label_2 =      {
    'bg':                       main2,
    'bd':                       '0',
    'relief':                   'flat',
    'highlightthickness':       '0'
    }

canvas_frame_label_3 = {
    'bg':                       main,
    'bd':                       '0',
    'relief':                   'flat',
    'highlightthickness':       '0'
    }

info_label = {
    'bg':                       main2,
    'fg':                       '#BCBCBC',
    'bd':                        '5',
    'relief':                   'flat',
    'highlightthickness':       '0',
    'font':                     ("微软雅黑", 9),
    'anchor':                   'nw',
    'justify':                  'left',
    }

text_1 = {
    'bg':                       main2,
    'fg':                       'white',
    'activebackground':         main2,
    'activeforeground':         'white',
    'relief':                   'flat',
    'border':                   '0',
    'font':                     ("微软雅黑", 9)
    }
text_2 = {
    'bg':                       main2,
    'fg':                       '#D0D0D0',
    'activebackground':         main2,
    'activeforeground':         'white',
    'relief':                   'flat',
    'border':                   '0',
    'font':                     ("微软雅黑", 9)
    }
text_3 = {
    'bg':                       main,
    'fg':                       '#979797',
    'activebackground':         main,
    'activeforeground':         'white',
    'relief':                   'flat',
    'border':                   '0',
    'font':                     ("微软雅黑", 9)
    }

option_slider_style = {
    'bg':                       main,
    'activebackground':         main,
    'highlightcolor':           'white',
    'highlightthickness':       '0',
    'relief':                   'flat',
    'sliderrelief':             'flat',
    'border':                   '0',
    'width':                    '3',
    'troughcolor':              '#1F1F1F',
    }

entry_3 = {
    'bg':                       '#1F1F1F',
    'fg':                       '#FFFFFF',
    'relief':                   'flat',
    'border':                   '0',
    'width':                    '5',
    'justify':                  'c',
    'font':                     ("微软雅黑", 9),
    'highlightthickness':        '1',
    'highlightbackground':        '#17181A',
    }

entry_2 = {
    'bg':                       '#1F1F1F',
    'fg':                       '#FFFFFF',
    'relief':                   'flat',
    'border':                   '0',
    'highlightthickness':        '1',
    'highlightbackground':        '#17181A',
    'width':                    '5',
    'justify':                  'l',
    'font':                     ("微软雅黑", 9)
    }

text_selection_off_3 = {
    'bg':                       main,
    'fg':                       '#7A7A7A',
    'activebackground':         main,
    'activeforeground':         'white',
    'relief':                   'flat',
    'border':                   '0',
    'font':                     ("Segoe UI", 10)
    }
text_selection_on_3 = {
    'bg':                       main,
    'fg':                       '#FFFFFF',
    'activebackground':         main,
    'activeforeground':         'white',
    'relief':                   'flat',
    'border':                   '0',
    'font':                     ("Segoe UI", 10)
    }
text_selection_off_2 = {
    'bg':                       main2,
    'fg':                       '#7A7A7A',
    'activebackground':         main2,
    'activeforeground':         'white',
    'relief':                   'flat',
    'border':                   '0',
    'font':                     ("Segoe UI", 10)
    }
text_selection_on_2 = {
    'bg':                       main2,
    'fg':                       '#FFFFFF',
    'activebackground':         main2,
    'activeforeground':         'white',
    'relief':                   'flat',
    'border':                   '0',
    'font':                     ("Segoe UI", 10)
    }

parameter_switch_3 = {
    'bg':                       main,
    'fg':                       '#FFFFFF',
    'activebackground':         main,
    'activeforeground':         'white',
    'relief':                   'flat',
    'border':                   '0',
    'font':                     ("微软雅黑", 10)
    }

canvas_bg = {
    'bg':                       bg,
    'relief':                   'flat',
    'bd':                       '0',
    'highlightthickness':       '0'
    }

icon = {
    'IconOn':                   get_media_path('OnState.png'),
    'IconOff':                  get_media_path('OffState.png'),
    }

frame_style_bg =      {
    'bg':               bg,
    'relief':           'flat',
    'bd':               '0'
    }

button_3 =    {
    'bg':               main2,
    'fg':               '#FFFFFF',
    'activebackground': main2,
    'activeforeground': 'white',
    'relief':           'flat',
    'border':           '0',
    'font':             ("微软雅黑", 10)
    }
button_2 =    {
    'bg':               main2,
    'fg':               '#FFFFFF',
    'activebackground': main2,
    'activeforeground': 'white',
    'relief':           'flat',
    'border':           '0',
    'font':             ("微软雅黑", 10)
    }
button_1 =    {
    'bg':               main2,
    'fg':               '#FFFFFF',
    'activebackground': main2,
    'activeforeground': 'white',
    'relief':           'flat',
    'border':           '0',
    'font':             ("微软雅黑", 10)
    }

button_inactive =    {
    'bg':               main2,
    'fg':               '#FFFFFF',
    'activebackground': main2,
    'activeforeground': 'white',
    'relief':           'flat',
    'border':           '0',
    'font':             ("微软雅黑", 10)
    }

button_active =    {
    'bg':               main2,
    'fg':               '#FFFFFF',
    'activebackground': main2,
    'activeforeground': 'white',
    'relief':           'flat',
    'border':           '0',
    'font':             ("微软雅黑", 10)
    }

media_button_off_3= {
    'bg':               main2,
    'fg':               '#7A7A7A',
    'activebackground': main2,
    'activeforeground': 'white',
    'relief':           'flat',
    'border':           '0',
    'font':             ("Segoe UI", 8)
    }

media_button_on_3= {
    'bg':               '#4a57ee',
    'fg':               '#FFFFFF',
    'activebackground': '#4a57ee',
    'activeforeground': 'white',
    'relief':           'flat',
    'border':           '0',
    'font':             ("Segoe UI", 8)
    }

ui_text_na_2 =    {
    'bg':               main,
    'fg':               '#7A7A7A',
    'activebackground': main,
    'activeforeground': 'white',
    'relief':           'flat',
    'border':           '0',
    'font':             ("微软雅黑", 9)
    }

timeline_canvas = {
    'bg':                       main,
    'relief':                   'flat',
    'bd':                       '0',
    'highlightthickness':       '0'
    }

donate_1 = {
    'bg':               main,
    'fg':               '#7562ee',
    'relief':           'flat',
    'border':           '0',
    'font':             ("微软雅黑 Semibold", 10),
    'cursor':           "hand2",
    }

# Panes
# 3:#28282E
# 2:#212126
# 1:#17181A

# preview background: #1A1A1A

# Num Fields, slider bg: #1F1F1F
# slider ball: #919191
# Borders:#090909
# Text
# On/off:#FFFFFF
# labels: #D0D0D0
# notActive: #7A7A7A
# active:#FFFFFF

# highlighted button: #B1B1B2
# Button off: #828282

# on:     #FFFFFF
# hover:  #b1b1b2
# off:    #828282
