import random

import time as tm
from kivy.clock import Clock
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
class layout(BoxLayout):
    a = 0
    chosen_text = ""
    count = 0
    countend = 0
    flag = 0
    text_list = [
        'Career goals can be focused on productivity, which means a person can produce or meet the desired ends',
        ' Efficiency could also be a goal that includes speed, accuracy, and consistency for producing the desired results',
        ' Having a career goal within academics always helps one\'s self-development within the chosen career',
        ' Improving skills and looking for opportunities help to keep a person relevant in a particular field',
        ' In the long run, having a personal development goal is equally important as one\'s educational qualifications',
        ' Personal skills like communication, teamwork, leadership qualities, etc. help in the long and short-run processes',
        'Travelling may be an expensive hobby but it compensates for the financial loss',
        ' If a traveller has interest in life and its manifestations, he can explore a lot to keep himself absorbed and happy',
        ' A student of sociology can gather much from the customs and rituals of life of the people living in different regions of the world',
        ' A student of history can discover a vivid account of history in the historical monuments',
        ' An engineer can enrich his knowledge by looking at the engineering feats at different places',
        ' In fact, one can find everything that satisfies one\'s intellectual and adventurous cravings',
        'The \"Just Say No\" campaign was founded by Nancy Reagen and soon became the centrepiece of the Reagen Administration\'s anti-drug campaign',
        ' The campaign mainly focused on TV commercials and public advertisements',
        ' In the initial stages, the government wanted to know the source of the illicit substances',
        ' The answer was simply Mexico; it was the greatest exporter of marijuana in the sixties',
        ' Though in the mid-seventies, the Mexican smugglers were subdued due to stricter customs and border patrol',
        ' The lack of income is the reason that the choice of America changed to cocaine',
        'A German neurologist named Alois Alzheimer discovered Alzheimer\'s disease in 1906 after studying the case of a middle-aged woman named Auguste D',
        ' After her death he found senile plaques and neurofibrillary tangles as he did an autopsy',
        ' Alzheimer\'s disease or AD is a form of dementia which leads to the loss of a person\'s ability to think and reason',
        ' It destroys the memory as neurons are injured and die throughout the brain resulting in a break down in the connections between networks of neurons',
        ' Major brain regions begin to shrink',
        ' By the final stages of Alzheimer\'s significant loss of brain volume is seen, which is called brain atrophy',
        'Taking care of mental health not only is getting help from professionals when needed but also connecting with other, getting involved in physical activities, helping others, getting enough sleep and staying positive that there is a way out',
        ' Positive mental health allows people to realize their full potential, cope with stress in life, work productively and make meaningful contributions to the community',
        ' Various factors in people\'s lives such as intrapersonal relations, physical factors, childhood trauma and many other conditions can disrupt mental health conditions',
        ' Taking care and looking after one\'s mental health preserves an individual\'s ability to enjoy life']
    label_text = StringProperty("Click button to generate text!!!!")
    def choose(self):
        self.wordlist = []
        if self.flag == 0:
            abc = len(self.text_list)
            abc -= 1
            num = random.randint(0, abc)
            random_text = self.text_list[num]
            self.chosen_text = random_text
            self.label_text = self.chosen_text
            self.ids.clicked.disabled = True
            self.ids.textinput.readonly = False
            self.count = 0
            self.countend = 0
            self.random_text_list = self.chosen_text.split()
        else:
            self.ids.textinput.readonly = True
            self.label_text = "Click button to generate text!!!!"
            self.ids.clicked.text = "Generate!"
            self.flag = 0
            self.ids.textinput.text = ""
            self.ids.textinput.readhint = "Click the button and enter the generated text!"
            self.count = 0
            self.countend = 0
            self.random_text_list = self.chosen_text.split()
    mytime = 0
    mins = 0
    def increment(self,interval):
        if self.ids.clicked.disabled == True:
            self.mytime += 1
            if self.mytime == 60:
                self.mins += 1
                self.mytime = 0
            self.ids.foralltime.text = str(self.mins) + ":" + str(self.mytime)
    newvar = ""
    wordlist = []
    def start(self):
        self.t1 = tm.time()
        Clock.schedule_interval(self.increment, 1)
        self.newvar = ""
    inputtext = ""
    # def lst_join(self, lst):
    #     lst

    def textchange(self):
        abc = self.count
        if " " in self.ids.textinput.text:
            self.wordlist.append(self.ids.textinput.text.strip())
            self.inputtext += self.ids.textinput.text.strip()
            self.newvar += self.inputtext
            print(self.random_text_list)

            if self.inputtext == self.random_text_list[self.count*3]:
                self.random_text_list.insert(self.count*3, "[color=00FF00]")
                self.random_text_list.insert(self.count*3+2, "[/color]")
                self.ids.my_label.text = ""
                # self.ids.my_label.text = " ".join(self.random_text_list)
                for i in self.random_text_list:
                    if i == "[color=00FF00]" or i == "[/color]":
                        self.ids.my_label.text += i
                    else:
                        self.ids.my_label.text += f" {i}"
                # self.countend = self.count + 2
                # self.count += 3
                self.count +=1
            else:
                self.random_text_list.insert(self.count*3, "[color=FF0000]")
                self.random_text_list.insert(self.count*3+2, "[/color]")
                self.ids.my_label.text = ""
                # self.ids.my_label.text = " ".join(self.random_text_list)
                for i in self.random_text_list:
                    if i == "[color=FF0000]" or i == "[/color]":
                        self.ids.my_label.text += i
                    else:
                        self.ids.my_label.text += f" {i}"
                self.count += 1
            self.ids.textinput.text = ""
            self.inputtext = ""
            if len(self.wordlist) == len(self.chosen_text.split()):
                self.finish()
    def finish(self):
        self.mytime = 0
        self.mins = 0
        if self.ids.textinput.text != " ":
             self.wordlist.append(self.ids.textinput.text)
        t2 = tm.time()
        self.ids.textinput.readonly = True
        split_text = self.chosen_text.split()
        correct_count = 0
        for i in split_text:
            try:
                if i == self.wordlist[split_text.index(i)].strip():

                    correct_count += 1
                else:

                    continue
            except:

                continue
        time = t2 - self.t1
        self.label_text = f"\nTime Taken: {round(time)}\nTotal Count of Words: {len(self.label_text.split())}\nCorrect Count of Words: {correct_count}\nWords Per Minute: {round((correct_count / time) * 60)}"
        self.ids.clicked.disabled = False
        self.ids.clicked.text = "Restart?"
        self.flag = 1
        Clock.unschedule(self.increment)
        self.ids.foralltime.text = "0:0"
class typetestApp(App):
    pass
typetestApp().run()
