class CalculatorException(Exception):
    """Eroare de calcul."""
    pass


class Calculator(object):
    def __init__(self):
        # Definim operatorii și prioritățile lor
        self.operatori = {
            '+': {'precedenta': 1, 'asociativitate': 'left'},
            '-': {'precedenta': 1, 'asociativitate': 'left'},
            '*': {'precedenta': 2, 'asociativitate': 'left'},
            '/': {'precedenta': 2, 'asociativitate': 'left'}
        }

    def read(self):
        '''read input from stdin'''
        return input('> ')

    def _este_operator(self, input):
        return input in self.operatori

    def _este_numar(self, input):
        try:
            float(input)
            return True
        except ValueError:
            return False

    def _tokenizeaza(self, expresie):
        tokens = []
        numar_curent = ""

        i = 0
        while i < len(expresie):
            char = expresie[i]

            if char.isspace():
                if numar_curent:
                    tokens.append(numar_curent)
                    numar_curent = ""
                i += 1
                continue

            if char.isdigit() or char == '.':
                numar_curent += char

            elif char in self.operatori:
                if numar_curent:
                    tokens.append(numar_curent)
                    numar_curent = ""

                if char == '-':
                    if not tokens or tokens[-1] in self.operatori or tokens[-1] == '(':
                        numar_curent = '-'
                        i += 1
                        continue

                tokens.append(char)

            elif char == '(' or char == ')':
                if numar_curent:
                    tokens.append(numar_curent)
                    numar_curent = ""
                tokens.append(char)

            else:
                raise CalculatorException(f"Caracter invalid în expresie: '{char}'")

            i += 1

        if numar_curent:
            tokens.append(numar_curent)

        return tokens

    def _conversie(self, tokens):
        output = []
        stiva_operatori = []

        for token in tokens:
            if self._este_numar(token):
                output.append(token)

            elif self._este_operator(token):
                while (stiva_operatori and
                       stiva_operatori[-1] != '(' and
                       stiva_operatori[-1] in self.operatori and
                       self.operatori[stiva_operatori[-1]]['precedenta'] >= self.operatori[token]['precedenta']):
                    output.append(stiva_operatori.pop())
                stiva_operatori.append(token)

            elif token == '(':
                stiva_operatori.append(token)

            elif token == ')':
                while stiva_operatori and stiva_operatori[-1] != '(':
                    output.append(stiva_operatori.pop())

                if not stiva_operatori:
                    raise CalculatorException("Paranteze nepotrivite în expresie")

                stiva_operatori.pop()

        while stiva_operatori:
            op = stiva_operatori.pop()
            if op == '(' or op == ')':
                raise CalculatorException("Paranteze nepotrivite în expresie")
            output.append(op)

        return output

    def _evalueaza(self, rpn):
        stiva = []

        for token in rpn:
            if self._este_numar(token):
                stiva.append(float(token))

            elif self._este_operator(token):
                if len(stiva) < 2:
                    raise CalculatorException("Expresie invalida: operatori insuficienți")

                operand2 = stiva.pop()
                operand1 = stiva.pop()

                if token == '+':
                    rezultat = operand1 + operand2
                elif token == '-':
                    rezultat = operand1 - operand2
                elif token == '*':
                    rezultat = operand1 * operand2
                elif token == '/':
                    if operand2 == 0:
                        raise CalculatorException("Impărțire la zero")
                    rezultat = operand1 / operand2

                stiva.append(rezultat)

        if len(stiva) != 1:
            raise CalculatorException("Expresie invalidă")

        return stiva[0]

    def eval(self, string):
        '''evaluates an infix arithmetic expression '''
        if not string or string.strip() == "":
            raise CalculatorException("Expresie vidă")

        try:
            tokens = self._tokenizeaza(string)

            if not tokens:
                raise CalculatorException("Expresie vidă")

            operatie = self._conversie(tokens)

            rezultat = self._evalueaza(operatie)

            return rezultat

        except CalculatorException:
            raise
        except Exception as e:
            raise CalculatorException(f"Eroare la evaluarea expresiei: {str(e)}")

    def loop(self):
        """read a line of input, evaluate and print it
        repeat the above until the user types 'quit'. """
        while True:
            try:
                line = self.read()

                if line.strip().lower() == 'quit':
                    break

                rezultat = self.eval(line)

                print(rezultat)

            except CalculatorException as e:
                print(f"Eroare: {e}")
            except EOFError:
                break
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    calc = Calculator()
    calc.loop()