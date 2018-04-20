from transitions import Machine

class Auto(object):

    states = ['apagado', 'encendido', 'en movimiento']

    def __init__(self, name):

        self.name = name

        self.velocidad = 'nula'

        self.machine = Machine(model=self, states=self.states, initial='apagado')

        self.machine.add_transition(trigger='encender', source='apagado', dest='encendido')


        self.machine.add_transition('acelerar', 'encendido', 'en movimiento', after = 'aumentar_velocidad')
        self.machine.add_transition('acelerar', 'en movimiento', 'en movimiento', after = 'aumentar_velocidad')

        self.machine.add_transition('frenar', 'en movimiento', 'encendido', conditions=['va_despacio'], after = 'disminuir_velocidad')
        self.machine.add_transition('frenar', 'en movimiento', 'en movimiento', after = 'disminuir_velocidad')
        
        self.machine.add_transition('apagar','encendido','apagado')

    
    def va_despacio(self):
        return self.velocidad == 'despacio';

    def aumentar_velocidad(self):
        if self.velocidad == 'despacio':
            self.velocidad = 'rapido'
        if self.velocidad == 'nula':
            self.velocidad = 'despacio'    
        print 'velocidad: ' + self.velocidad
            
    def disminuir_velocidad(self):
        if self.velocidad == 'despacio':
            self.velocidad = 'nula'
        if self.velocidad == 'rapido':
            self.velocidad = 'despacio'    
        print 'velocidad: ' + self.velocidad

        
a = Auto("auto")
print a.state

a.encender()
print a.state

a.acelerar()
print a.state

a.frenar()
print a.state
