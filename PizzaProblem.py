class PizzaProblem(object):
    #Returns a ratio of Luis' pizza consumption
    def getLuis(self):
        luis_ratio = 5/6
        return luis_ratio

    #Returns a ratio of Marty's pizza consumption
    def getMarty(self):
        marty_ratio = 2/3
        return marty_ratio

    #Calculates the amount of pizza consumed based on Marty/Luis' eating habits, and the size of the pizza 
    def the_problem_with_pizza(self, marty, luis, pizza_size_Marty, pizza_size_Luis):
        M = marty
        L = luis
        x = pizza_size_Marty
        y = pizza_size_Luis

        marty_ate = M*x
        print("Marty ate: " + str(format(marty_ate, '.2f')) + " pizza units")
        luis_ate = L*y
        print("Luis ate: " + str(format(luis_ate, '.2f')) + " pizza units")

        if marty_ate > luis_ate:
            print("Marty ate : " + str(format(marty_ate - luis_ate, '.2f')) + " more pizza units. The teacher is wrong.\n")
        else:
            print("Luis ate: " + str(format(luis_ate - marty_ate, '.2f'))+ 
                  " more pizza units. We can deduce that they ate the same "+"size pizza or Luis' pizza was larger\n")

#Main
if __name__ == '__main__':
    pizza = PizzaProblem()
    Marty = pizza.getMarty()
    Luis = pizza.getLuis()
    print("2:1 ratio pizza sizes in Marty's favor")
    pizza.the_problem_with_pizza(Marty,Luis,2,1)
    print("1:2 ratio pizza sizes in Luis' favor")
    pizza.the_problem_with_pizza(Marty,Luis,1,2)
    print("1:1 ratio of pizza sizes")
    pizza.the_problem_with_pizza(Marty,Luis,1,1)
