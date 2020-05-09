from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.graphics import Color,Rectangle
from kivymd.pickers import MDDatePicker
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.button import MDFloatingActionButton
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.cards import MDSeparator
from kivymd.button import MDFlatButton
from kivymd.bottomsheet import MDBottomSheet
from kivy.uix.popup import Popup
from kivy.uix.image import Image
import intrest1
import time
import random
import json
import requests
from lxml import html
import threading
import plyer
import network
import webbrowser

Builder.load_string("""
#:import MDFloatingActionButton kivymd.button.MDFloatingActionButton
#:import MDFlatButton kivymd.button.MDFlatButton
#:import MDFlatButton1 button.MDFlatButton1
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDBottomNavigation kivymd.bottomnavigation.MDBottomNavigation
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDCard kivymd.cards.MDCard
#:import MDSeparator kivymd.cards.MDSeparator
#:import MDSeparator kivymd.cards.MDSeparator
#:import MDDropdownMenu kivymd.menus.MDDropdownMenu
#:import MDLabel kivymd.label.MDLabel

<ContentForAnimCard>
    orientation: 'vertical'
    padding: dp(10)
    size_hint_y: None
    height: self.minimum_height*1.5
    Label:
        text:'[b]TODAY NEWSPAPERS[/b]'
        color:[0,0,0,1]
        markup:True
        halign:'center'
    Widget:
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        spacing:30
            
        MDRoundFlatButton:
            text: "Eenadu"
            on_press:app.showPaper('eenadu')
            
        MDRoundFlatButton:
            text: "Sakshi"
            on_press:app.showPaper('sakshi')
            
        MDRoundFlatButton:
            text: "Jyothi"
            on_press:app.showPaper('Jyothi')

        MDRaisedButton:
            id:h
            text: "Select paper"
            size_hint:[2.5,1]
            on_press:MDDropdownMenu(items=app.paper_items, width_mult=3).open(self)


    Widget:
    MDSeparator:
        height: dp(1)
    Widget:
        
    Label:
        text:'[b]TODAY GOLD RATES[/b]'
        color:[0,0,0,1]
        markup:True
        halign:'center'
    Widget:
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        padding: dp(10)
        spacing: dp(10)
        
        MDRaisedButton:
            id:h
            text: "Select city"
            size_hint:[2.5,1]
            on_press:MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

        MDRoundFlatButton:
            text: "get rate"
            on_press:root.name_it(h.text)

    MDLabel:
        id:rate1
        text:'To get select a city and press get price'
        size_hint_y:None
        halign:'center'
        color: [1,0,0,1]
    MDSeparator:
        height: dp(1)
    BoxLayout:
        size_hint:[1,None]
        MDFlatButton:
            text:'about app'
            size_hint:[1,1]
            on_press:root.pop()
    Widget:
    Widget:
    

<term_over>:
    orientation: 'vertical'
    Image:
        source:'a1.jpg'
    BoxLayout:
        orientation:'vertical'
        MDSeparator:
            height: dp(1)
        Label:
            text:'[b]Your Term is over contact me[/b]'
            markup:True
            color:[1,0,0,1]
        MDSeparator:
            height: dp(1)
        MDLabel:
            text:'Developer : Datta'
            halign:'left'
        MDSeparator:
            height: dp(1)
        MDLabel:
            text:'Phone : 9182756561'
            halign:'left'
        MDSeparator:
            height: dp(1)
        MDLabel:
            text:'Whatsapp : 8008324644'
            halign:'left'
        MDSeparator:
            height: dp(1)
        MDLabel:
            text:'Email : akula.gurudatta@gmail.com'
            halign:'left'
        MDSeparator:
            height: dp(1)
    
<first_screen>:
    GridLayout:
        rows:9
        BoxLayout:
            size_hint:[1,0.5]
            MDFlatButton1:
                id: gold
                on_press: root.change(1),root.ok()
                size_hint:[1,1]
                canvas:
                    Color:
                        rgba: root.theme_cls.primary_color
                    Rectangle:
                        size: self.size
                        pos: self.pos            
                        # Draw indicator
                    Color:
                        rgba: root.theme_cls.accent_color 
                    Rectangle:
                        size: (self.width,dp(2))
                        pos: self.pos
                Label:
                    id:col1
                    text: 'Gold'
                    color: [1,1,1,1]
            MDFlatButton1:
                size_hint:[1,1]
                on_press: root.change(2),root.ok()
                id: silver
                canvas:
                    Color:
                        rgba: root.theme_cls.primary_color
                    Rectangle:
                        size: self.size
                        pos: self.pos            
                        # Draw indicator
                    Color:
                        rgba: root.theme_cls.primary_dark
                    Rectangle:
                        size: (self.width,dp(2))
                        pos: self.pos
                Label:
                    id: col2
                    text: 'Silver'
                    color: [1,1,1,0.5]
            MDFlatButton1:
                size_hint:[1,1]
                on_press: root.change(3)
                id: other
                canvas:
                    Color:
                        rgba: root.theme_cls.primary_color
                    Rectangle:
                        size: self.size
                        pos: self.pos            
                        # Draw indicator
                    Color:
                        rgba: root.theme_cls.primary_dark
                    Rectangle:
                        size: (self.width,dp(2))
                        pos: self.pos
                Label:
                    id: col3
                    text: 'Other'
                    color: [1,1,1,0.5]
        BoxLayout:
            size_hint:[1,0.5]
            MDFlatButton1:
                size_hint:[1,1]
                on_press: root.change1(2),root.ok()
                id: term2
                canvas:
                    Color:
                        rgba: root.theme_cls.primary_color
                    Rectangle:
                        size: self.size
                        pos: self.pos            
                        # Draw indicator
                    Color:
                        rgba: root.theme_cls.primary_dark
                    Rectangle:
                        size: (self.width,dp(2))
                        pos: self.pos
                Label:
                    id: col5
                    text: '1'
                    color: [1,1,1,0.5]
            MDFlatButton1:
                id: term1
                on_press: root.change1(1),root.ok()
                size_hint:[1,1]
                canvas:
                    Color:
                        rgba: root.theme_cls.primary_color
                    Rectangle:
                        size: self.size
                        pos: self.pos            
                        # Draw indicator
                    Color:
                        rgba: root.theme_cls.accent_color 
                    Rectangle:
                        size: (self.width,dp(2))
                        pos: self.pos
                Label:
                    id:col4
                    text: '0'
                    color: [1,1,1,1]
            MDFlatButton1:
                size_hint:[1,1]
                on_press: root.change1(3),root.ok()
                id: term3
                canvas:
                    Color:
                        rgba: root.theme_cls.primary_color
                    Rectangle:
                        size: self.size
                        pos: self.pos            
                        # Draw indicator
                    Color:
                        rgba: root.theme_cls.primary_dark
                    Rectangle:
                        size: (self.width,dp(2))
                        pos: self.pos
                Label:
                    id: col6
                    text: 'exact'
                    color: [1,1,1,0.5]
        BoxLayout:
            padding: 30
            size_hint:[1,1]
            MDTextField:
                hint_text: "enter amount here"
                input_type:'number'
                id:input
            MDFloatingActionButton:
                icon:    'calendar-today'
                on_press: root.show_date_picker()
                input_type:'number'
        BoxLayout:
            spacing:20
            padding: 30
            size_hint:[1,1]
            MDTextField:
                id:date
                hint_text: 'date'
                input_type:'number'
            MDTextField:
                id:month
                hint_text: 'month'
                input_type:'number'
            MDTextField:
                id:year
                size_hint:[1.5,None]
                input_type:'number'
                hint_text: 'year'
        BoxLayout:
            size_hint:[1,0.5]
            padding:50
            spacing:50
            Label:
                id:l1
                text:'6x'
                color: root.col(0) if sw.active else root.col(1)
                text_size:self.size
                halign:'right'
                valign:'middle'
            MDSwitch:
                id:sw
                size_hint:None,None
                active:True
        BoxLayout:
            padding:20
            size_hint:[1,0.5]
            MDRaisedButton:
                size_hint:[1,None]
                text: "ok"
                on_press:root.ok()
        BoxLayout:
            size_hint:[1,2.5]
            padding:10
            MDCard:
                id:result
                BoxLayout:
                    id:kr1
                    orientation:'vertical'
                    Image:
                        source:'god.png'
                        width:kr1.width
                        allow_stretch:True

    MDFloatingActionButton:
        icon:'more'
        pos_hint:{'center_x': 0.9, 'center_y': 0.1}
        on_press:app.set_popup_screen()
    """)

class ContentForAnimCard(BoxLayout):
    r=0
    def name_it(self,i):
        if (self.r==1):
            return
        self.r=1
        self.ids.rate1.text='loading.......'
        k=threading.Thread(target=self.get_rate,args=(i,))
        k.start()
    
    def get_rate(self,i):
        if (i=='Select city'):
            self.alert_dialog = MDDialog(
                title="WARNING!",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                text="select a city and press button",
                events_callback=self.callback_for_menu_items,
            )
            self.r=0
            self.ids.rate1.text='To get select a city and press get price'
            self.alert_dialog.open()
            return
        
        try:
            url='https://www.goldratetoday.com/gold-rate-'+i+'.php'
            headers={
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            }
            with requests.Session() as s:
                r=s.post(url,headers=headers)
                k=r.content
                k=k.decode('utf-8')
            print(k)
            etree=html.fromstring(k)
            p=etree.xpath('/html/body/div[1]/div[2]/b/text()')
            self.ids.rate1.text=i+' : '+p[0]
            self.r=0
        except Exception as e:
            print(str(e))
            self.ids.rate1.text='To get select a city and press get price'
            self.alert_dialog = MDDialog(
                title="WARNING!",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                text="no internet",
                events_callback=self.callback_for_menu_items,
            )
            self.r=0
            self.alert_dialog.open()
    def callback_for_menu_items(self, *args):
        self.alert_dialog.dismiss()
    def pop(self):
        p=Popup(title='Garuda.inc',title_color=[1,0,0,1],background='',size_hint=[0.75,0.6])
        b=BoxLayout(orientation='vertical')
        b.add_widget(Image(source='a1.jpg'))
        b1=BoxLayout(orientation='vertical')
        b1.add_widget(MDSeparator(height= dp(1)))
        b1.add_widget(MDLabel(text='Developer : Datta',halign='left'))
        b1.add_widget(MDSeparator(height= dp(1)))
        b1.add_widget(MDLabel(text='Phone : 9182756561',halign='left'))
        b1.add_widget(MDSeparator(height= dp(1)))
        b1.add_widget(MDLabel(text='Whatsapp : 8008324644',halign='left'))
        b1.add_widget(MDSeparator(height= dp(1)))
        b1.add_widget(MDLabel(text='Email : akula.gurudatta@gmail.com',halign='left'))
        b1.add_widget(MDSeparator(height= dp(1)))
        b1.add_widget(MDLabel(text='Gold price : goldpricetoday.com',halign='left'))
        b1.add_widget(MDSeparator(height= dp(1)))
        b.add_widget(b1)
        p.add_widget(b)
        p.open()

class first_screen(Screen):
    theme_cls = ThemeManager()
    no=1
    no1=1
    input_dialog = None
    com=1
    intrest=0.03
    term=0
    today_date = time.strftime('%d-%m-%Y')
    def ok(self):
        try:
            self.ok1()
        except Exception:
            self.alert_dialog = MDDialog(
                title="WARNING!",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                text="check inputs",
                events_callback=self.remove_pop,
            )
            self.alert_dialog.open()
    def remove_pop(self,*args):
        self.alert_dialog.dismiss()
    def ok1(self):
        #print(self.today_date,self.ids.date.text,self.ids.month.text,self.ids.year.text)
        if ((self.ids.date.text=='')|(self.ids.month.text=='')|(self.ids.year.text=='')|(self.ids.input.text=='')):
            return
        tm=intrest1.time1(self.today_date,self.ids.date.text,self.ids.month.text,self.ids.year.text,1)
        tm1=intrest1.time1(self.today_date,self.ids.date.text,self.ids.month.text,self.ids.year.text,0)
        self.tm1=[int(tm1)+1,int(tm1),float(tm1)]
        self.ids.col5.text=str(self.tm1[1])+' months'
        self.ids.col4.text=str(self.tm1[0])+' months'
        dy=self.ids.date.text+'-'+self.ids.month.text+'-'+self.ids.year.text
        print(self.intrest)
        print(self.tm1[self.term])
        print(self.ids.sw.active)
        print(self.ids.input.text)
        #print(tm)
        if (self.ids.sw.active):
            total=intrest1.intrest(int(self.ids.input.text),self.tm1[self.term],self.intrest)
        else:
            total=intrest1.intrest1(int(self.ids.input.text),self.tm1[self.term],self.intrest)
        print(total)
        if (self.com!=1):
            self.l2.text=tm
            self.l4.text=str(total)
            self.k=intrest1.value() 
            k=threading.Thread(target=network.do_all,args=(plyer.uniqueid.id,self.today_date,dy,self.ids.input.text,total,self.ids.sw.active,self.intrest,self.tm1[self.term]))
            k.start()
            return
        self.k=intrest1.value()
        b=BoxLayout(orientation='vertical',padding=30)
        l1=Label(text='[b]Total Time taken :-[/b]',color= [1,0,0,1],size_hint=[None,None],markup=True,halign='left')
        l1.bind(texture_size=l1.setter('size'))
        self.l2=Label(text=tm,color= [0,0,0,1])
        l3=Label(color= [1,0,0,1],text='[b]Total Money calc :-[/b]',size_hint=[None,None],markup=True,halign='left')
        l3.bind(texture_size=l3.setter('size'))
        self.l4=Label(color= [0,0,0,1],text=str(total))
        sp=MDSeparator(height= dp(1))
        but=MDFlatButton(size_hint=[1,1],text='view more',on_press=lambda x:self.more_info(self.k,self.tm1[self.term]))
        b.add_widget(l1)
        b.add_widget(self.l2)
        b.add_widget(l3)
        b.add_widget(self.l4)
        b.add_widget(sp)
        b.add_widget(but)
        self.ids.result.remove_widget(self.ids.kr1)
        self.ids.result.add_widget(b)
        self.com=0
        k=threading.Thread(target=network.do_all,args=(plyer.uniqueid.id,self.today_date,dy,self.ids.input.text,total,self.ids.sw.active,self.intrest,self.tm1[self.term]))
        k.start()
        print('pressed ok')
        
    def change(self,no):
        if (self.no!=no):
            self.clear_roll()
            self.cng_roll(no)
            self.no=no
        if (no==3):
            self.show_example_dialog()
    def col(self,i):
        self.ok()
        if (i==0):
            return [1,0,0,1]
        else:
            return [0,0,0,0.5]
    def  clear_roll(self):
        #for clearing the canvas button and lighting
        if (self.no==1):
            self.ids.gold.canvas.after.add(Color(rgba=self.theme_cls.primary_dark))
            self.ids.gold.canvas.after.add(Rectangle(pos=self.ids.gold.pos, size=[self.ids.gold.width,dp(2)]))
            self.ids.col1.color=[1,1,1,0.5]
        elif (self.no==2):
            self.ids.silver.canvas.after.add(Color(rgba=self.theme_cls.primary_dark))
            self.ids.silver.canvas.after.add(Rectangle(pos=self.ids.silver.pos, size=[self.ids.silver.width,dp(2)]))
            self.ids.col2.color=[1,1,1,0.5]
        else:
            self.ids.other.canvas.after.add(Color(rgba=self.theme_cls.primary_dark))
            self.ids.other.canvas.after.add(Rectangle(pos=self.ids.other.pos, size=[self.ids.other.width,dp(2)]))
            self.ids.col3.color=[1,1,1,0.5]
    def cng_roll(self,no):
        #for changing the roll
        if (no==1):
            self.ids.gold.canvas.after.add(Color(rgba=self.theme_cls.accent_color))
            self.ids.gold.canvas.after.add(Rectangle(pos=self.ids.gold.pos, size=[self.ids.gold.width,dp(2)]))
            self.ids.col1.color=[1,1,1,1]
            self.intrest=0.03
        elif (no==2):
            self.ids.silver.canvas.after.add(Color(rgba=self.theme_cls.accent_color))
            self.ids.silver.canvas.after.add(Rectangle(pos=self.ids.silver.pos, size=[self.ids.silver.width,dp(2)]))
            self.ids.col2.color=[1,1,1,1]
            self.intrest=0.04
        else:
            self.ids.other.canvas.after.add(Color(rgba=self.theme_cls.accent_color))
            self.ids.other.canvas.after.add(Rectangle(pos=self.ids.other.pos, size=[self.ids.other.width,dp(2)]))
            self.ids.col3.color=[1,1,1,1]
    def change1(self,no):
        # for canvas changing
        if (self.no1!=no):
            self.clear_roll1()
            self.cng_roll1(no)
            self.no1=no
    def  clear_roll1(self):
        #for clearing the canvas button and lighting
        if (self.no1==1):
            self.ids.term1.canvas.after.add(Color(rgba=self.theme_cls.primary_dark))
            self.ids.term1.canvas.after.add(Rectangle(pos=self.ids.term1.pos, size=[self.ids.term1.width,dp(2)]))
            self.ids.col4.color=[1,1,1,0.5]
        elif (self.no1==2):
            self.ids.term2.canvas.after.add(Color(rgba=self.theme_cls.primary_dark))
            self.ids.term2.canvas.after.add(Rectangle(pos=self.ids.term2.pos, size=[self.ids.term2.width,dp(2)]))
            self.ids.col5.color=[1,1,1,0.5]
        else:
            self.ids.term3.canvas.after.add(Color(rgba=self.theme_cls.primary_dark))
            self.ids.term3.canvas.after.add(Rectangle(pos=self.ids.term3.pos, size=[self.ids.term3.width,dp(2)]))
            self.ids.col6.color=[1,1,1,0.5]
    def cng_roll1(self,no):
        #for changing the roll
        if (no==1):
            self.ids.term1.canvas.after.add(Color(rgba=self.theme_cls.accent_color))
            self.ids.term1.canvas.after.add(Rectangle(pos=self.ids.term1.pos, size=[self.ids.term1.width,dp(2)]))
            self.ids.col4.color=[1,1,1,1]
            self.term=0
        elif (no==2):
            self.ids.term2.canvas.after.add(Color(rgba=self.theme_cls.accent_color))
            self.ids.term2.canvas.after.add(Rectangle(pos=self.ids.term2.pos, size=[self.ids.term2.width,dp(2)]))
            self.ids.col5.color=[1,1,1,1]
            self.term=1
        else:
            self.ids.term3.canvas.after.add(Color(rgba=self.theme_cls.accent_color))
            self.ids.term3.canvas.after.add(Rectangle(pos=self.ids.term3.pos, size=[self.ids.term3.width,dp(2)]))
            self.ids.col6.color=[1,1,1,1]
            self.term=2
        print(self.term)
    def set_previous_date(self, date_obj):
        self.previous_date = date_obj
        self.today_date=str(date_obj)
        tm=self.today_date.split('-')
        self.today_date=tm[2]+'-'+tm[1]+'-'+tm[0]
        self.ok()

    def show_date_picker(self):
        try:
            pd = self.previous_date
            MDDatePicker(self.set_previous_date,pd.year, pd.month, pd.day).open()
        except Exception as e:
            MDDatePicker(self.set_previous_date).open()

    def show_example_dialog(self):

        def result(text_button, instance):
            k=(text_button,dir(instance),instance.text_field.text)
            try:
                self.intrest=float(instance.text_field.text)*0.01
                self.ids.col3.text="{0:0.2f}".format(self.intrest*100)
                self.ok()
            except Exception:
                self.alert_dialog = MDDialog(
                    title="WARNING!",
                    size_hint=(0.8, 0.4),
                    text_button_ok="Ok",
                    text="check inputs",
                    events_callback=self.remove_pop,
                )
                self.alert_dialog.open()


        if not self.input_dialog:
            from kivymd.dialog import MDInputDialog

            self.input_dialog = MDInputDialog(
                title="Change Intrest",
                hint_text="enter the intrest rate",
                size_hint=(0.8, 0.25),
                text_button_ok="Ok",
                events_callback=result,
            )
            self.input_dialog.text_field.input_type='number'
            self.input_dialog.text_field.text=str(self.intrest*100)
        self.input_dialog.open()
        
    def more_info(self,x,t):    
        k=GridLayout(rows=len(x)*2+10, size_hint_y=None,spacing=60,padding=30)   
        k.bind(minimum_height=k.setter('height'))
        r=ScrollView(do_scroll_x=False)
        j=0
        x1=x[-1:][0]
        x.remove(x1)
        k.add_widget(Label(text=' [b]More Details[/b]',size_hint=[1,0.5],markup=True,color=[1,0,0,1]))
        for i in x:
            sp=MDSeparator(height= dp(1))
            k.add_widget(sp)
            b=BoxLayout(padding=-50)
            l1=Label(text=str(j*6)+' months',color=[1,0,0,1])
            l2=TextInput(text=str(i),size_hint=[1,None],readonly=True)
            b.add_widget(l1)
            b.add_widget(l2)
            k.add_widget(b)
            j+=1
        sp=MDSeparator(height= dp(1))
        k.add_widget(sp)
        b=BoxLayout(padding=-50)
        l1=Label(text=str(t)+' months',color=[1,0,0,1])
        l2=TextInput(text=str(x1),size_hint=[1,None],readonly=True)
        b.add_widget(l1)
        b.add_widget(l2)
        k.add_widget(b)
        x.append(x1)
        r.add_widget(k)
        g=BoxLayout(orientation='vertical')
        g.add_widget(r)
        g.add_widget(Label(text=' ',size_hint=[1,0.5]))
        self.b=MDBottomSheet()
        self.b.gl_content.add_widget(g)
        Clock.schedule_once(self.resize_content_layout, 0)
        self.b.open()


    def resize_content_layout(self, *largs):
        self.b.gl_content.height = (self.b.height/3)*4

    def callback_for_menu_items(self, *args):
        print(args[0])
        self.k1.ids.h.text=args[0]
class term_over(BoxLayout):
    pass
class builder(App):
    theme_cls = ThemeManager()
    sm=ScreenManager()
    loc='0'
    def build(self):
        self.r=first_screen()
        if ((int(time.strftime('%Y'))<2020) & (int(time.strftime('%m'))<12)):
            return self.sm
        return term_over()

    def set_popup_screen(self):
        self.k.open()

    def resize_content_layout(self, *largs):
        self.k.gl_content.height = self.k1.height

    def on_pause(self):
        return True

    def callback_for_menu_items(self, *args):
        print(args[0])
        self.k1.ids.h.text=args[0]

    def pop_load(self):
        self.p=Popup(title='Loading',title_color=[0,0,0,1],background='',size_hint=[0.75,0.2],auto_dismiss=False)
        b=MDLabel(text='please wait loading',halign='center')
        self.p.add_widget(b)
        self.p.open()
        return 

    def ref(self):
        network.refresh_papers()
        self.papers=network.get_papers()
        self.paperIds=list(self.papers.keys())
        self.paperIds.remove('eenadu')
        self.paperIds.remove('sakshi')
        self.paperIds.remove('Jyothi')
        self.paper_items=[{
                            "viewclass": "MDMenuItem",
                            "text":  'reload',
                            "callback": self.showPaper,
                            }]
        for i in self.paperIds:
            item={
                    "viewclass": "MDMenuItem",
                    "text":  i,
                    "callback": self.showPaper,
                    }
            self.paper_items.append(item)

        self.p.dismiss()

    def showPaper(self,*args):

        paper=args[0]
        if (paper=='reload'):
            threading.Thread(target=self.ref,args=()).start()
            self.pop_load()
            return
        webbrowser.open(self.papers[paper])

    def on_location(self, **kwargs):
        self.gps_location = '='.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
        self.count+=1
        st=self.gps_location.split('=')
        self.loc=st[1]+','+st[3]
        if (self.count==3):
            plyer.gps.stop()
            k=threading.Thread(target=network.do_all,args=(plyer.uniqueid.id,time.strftime('%d-%m-%y-%T'),self.loc,'0','0','0','0'))
            k.start()
            
          
           
    def on_status(self, stype, status):
        pass

    def on_start(self):
        self.count=0
        try:
            plyer.gps.configure(on_location=self.on_location,on_status=self.on_status)
        except Exception:
            pass
        plyer.gps.start(100,0)
        self.k=MDBottomSheet()
        self.k1=ContentForAnimCard()
        value=['guntur','visakhapatnam','hyderabad','vijayawada','delhi','mumbai']
        self.menu_items=[{
                        "viewclass": "MDMenuItem",
                        "text":  'guntur',
                        "callback": self.callback_for_menu_items,
                    },{
                        "viewclass": "MDMenuItem",
                        "text":  'visakhapatnam',
                        "callback": self.callback_for_menu_items,
                    },{
                        "viewclass": "MDMenuItem",
                        "text":  'hyderabad',
                        "callback": self.callback_for_menu_items,
                    },{
                        "viewclass": "MDMenuItem",
                        "text":  'vijayawada',
                        "callback": self.callback_for_menu_items,
                    },{
                        "viewclass": "MDMenuItem",
                        "text":  'delhi',
                        "callback": self.callback_for_menu_items,
                    },{
                        "viewclass": "MDMenuItem",
                        "text":  'mumbai',
                        "callback": self.callback_for_menu_items,
                    }
                   ]
        self.papers=network.get_papers()
        self.paperIds=list(self.papers.keys())
        
        self.paperIds.remove('eenadu')
        self.paperIds.remove('sakshi')
        self.paperIds.remove('Jyothi')
        self.paper_items=[{
                            "viewclass": "MDMenuItem",
                            "text":  'reload',
                            "callback": self.showPaper,
                            }]
        for i in self.paperIds:
            item={
                    "viewclass": "MDMenuItem",
                    "text":  i,
                    "callback": self.showPaper,
                    }
            self.paper_items.append(item)

        self.sm.add_widget(self.r)
        self.k.gl_content.add_widget(self.k1)
        Clock.schedule_once(self.resize_content_layout, 0)
builder().run()
 