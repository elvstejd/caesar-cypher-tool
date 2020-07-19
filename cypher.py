'''Esta clase se encarga de cifrar una oracion o palabra usando el metodo César. 
Mas informacion aqui https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar '''

class Caesar:

    def __init__(self, sentence, shift):
        self.sentence = sentence
        self.shift = shift

    def __gen_abc(self, n):
        self.abc = "abcdefghijklmnopqrstuvwxyz"
        self.new_abc = self.abc[n:] + self.abc[:n]
        return self.new_abc

    def __restore_case(self, og, coded):
        self.case_corrected = ""
        for i in range(len(og)):
            if og[i].isupper():
                self.case_corrected += coded[i].upper()
            else:
                self.case_corrected += coded[i]

        return self.case_corrected

    def encode(self):
        self.normal_abc = list('abcdefghijklmnopqrstuvwxyz')
        self.shifted_abc = list(self.__gen_abc(self.shift))

        self.coded_sentence = ''

        for i in self.sentence:
            letter = i.lower()
            if letter in self.normal_abc:
                self.coded_sentence += self.shifted_abc[self.normal_abc.index(letter)]
            else:
                self.coded_sentence += i

        self.coded_sentence = self.__restore_case(self.sentence, self.coded_sentence)

        return self.coded_sentence

    
    
# MODO DE USO:

# 1. Crear objeto Caesar con la oracion y el desplazaminento como argumentos. A continuacion llamar el metodo encode().

# resultado = Caesar("Nos vemos hoy a las ocho.", 12).encode() 

# 2. Imprime el resultado

# print("Codificado: ")
# print(resultado)




# (c) ElvsTejd