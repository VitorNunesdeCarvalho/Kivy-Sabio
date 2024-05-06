# widgets são empilhados uns sobre os outros na ordem em que são adicionados

from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

layout_stack = StackLayout()

# O primeiro widget adicionado será o mais abaixo na pilha
# e o último widget adicionado será o mais acima.

botao1 = Button(text='Botão 1')
botao2 = Button(text='Botão 2')
layout_stack.add_widget(botao1)
layout_stack.add_widget(botao2)