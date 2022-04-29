import justpy as jp

def my_click(self, msg):
    self.text = 'I was clicked!'

wp = jp.WebPage(delete_flag=False)
my_paragraph_design = "w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
p = jp.P(text='Hello World!', a=wp, classes=my_paragraph_design)
for i in range(1,11):
    jp.P(text=f'{i}) Hello World!', a=wp, style=f'color: blue; font-size: {10*i}px')
# d = jp.Div(text='Hello world!')
# d.on('click', my_click) 
# wp.add(d)

def hello_world():
    return wp

jp.justpy(hello_world)