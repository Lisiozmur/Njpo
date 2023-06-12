class Exp:
    def interpret(self, cox):
        pass

class AdEx(Exp):
    def __init__(self, Left_o, right_o):
        self.left_o = Left_o
        self.right_o = right_o

    def interpret(self, cox):
        return self.left_o.interpret(cox) + self.right_o.interpret(cox)

class VaExp(Exp):
    def __init__(self, va):
        self.va = va

    def interpret(self, cox):
        return cox.get_value(self.va)

class EqExp(Exp):
    def __init__(self, left_exp, right_exp):
        self.left_exp = left_exp
        self.right_exp = right_exp

    def interpret(self, cox):
        return self.left_exp.interpret(cox) == self.right_exp.interpret(cox)

class Context:
    def __init__(self):
        self.var = {}

    def set_value(self, var, val):
        self.var[var] = val

    def get_value(self, var):
        return self.var.get(var)

context = Context()

variable_a = VaExp("a")
variable_b = VaExp("b")
variable_c = VaExp("c")

addition_expression = AdEx(variable_a, variable_b)
equality_expression = EqExp(addition_expression, variable_c)

context.set_value("a", 2), context.set_value("b", 3), context.set_value("c", 5)
result = equality_expression.interpret(context)

if result:
    print("Wyrażenie poprawne")
else:
    print("Wyrażenie nieporawne")
