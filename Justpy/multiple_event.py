import justpy as jp

def my_click(self, msg):
    self.text = 'I was clicked'
    self.set_class('bg-blue-500')

def my_mouseenter(self, msg):
    self.text = 'Mouse entered'
    self.set_class('bg-red-500')

def my_mouseleave(self, msg):
    self.text = 'Mouse left'
    self.set_class('bg-teal-500')


def event_demo():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-64 text-2xl m-2 p-2 bg-blue-500 text-white',
             click=my_click, mouseenter=my_mouseenter, mouseleave=my_mouseleave)
    return wp

jp.justpy(event_demo)