from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class IdadeApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding= 20, spacing= 10)

        self.nome_input = TextInput(
            hint_text="Digite seu nome",
            multiline = False,
            size_hint=(1, 0.2),
            
        )

        self.idade_input = TextInput(
            hint_text="Digite sua idade",
            multiline = False,
            input_filter='int',
            size_hint=(1, 0.2)
        )

        botao = Button(
            text="Enviar",
            size_hint= (1, 0.2)
        )

        botao.bind(on_press=self.mostrar_mensagem)

        self.resultado = Label(
            text="",
            size_hint=(1, 0.4)
        )
        
        layout.add_widget(self.nome_input)
        layout.add_widget(self.idade_input)
        layout.add_widget(botao)
        layout.add_widget(self.resultado)
    

        return layout
        
    def mostrar_mensagem(self, instance):
        nome = self.nome_input.text.strip()
        

        try:

          idade = int(self.idade_input.text)
          if idade < 18:
            mensagem = f"Olá, {nome} Você é menor de idade."
          elif idade >= 60:
            mensagem = f"PARÁBENS {nome} VOCÊ TA NA MELHOR IDADE !!!!"
          else:
            mensagem = f" Olá {nome} você é IDOSO <3"
        
        except ValueError:
            mensagem = "Por favor, digite uma idade válida. "

        self.resultado.text= mensagem

if __name__ == "__main__":
    IdadeApp().run()                