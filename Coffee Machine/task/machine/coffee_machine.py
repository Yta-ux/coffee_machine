class MachineCoffee:
    def __init__(self):
        self.agua = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.dinero = 550

    def Iniciar(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            self.action_ = input('>>').lower().strip()
            print()
            if self.action_ == 'buy':
                self.Buy()

            elif self.action_== 'fill':
                self.Fill()

            elif self.action_ == 'take':
                self.Take()

            elif self.action_ == 'remaining':
                self.Remaining()

            elif self.action_ == 'exit':
                break

            else:
                print('Codigo Invalido')

    def Buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        coffee = input('>>')
        if coffee == '1':
            if  self.agua >= 250 and self.beans >= 16 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.agua = self.agua - 250
                self.beans = self.beans - 16
                self.dinero = self.dinero + 4
                self.cups = self.cups - 1
            else:
                if self.agua < 250:
                    print('Sorry, not enough water!')
                elif self.beans < 16:
                    print('Sorry, not enough coffee beans!')
                elif self.cups < 1:
                    print('Sorry, not enough cups!')
            print()
        elif coffee == '2':
            if self.agua >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.agua = self.agua - 350
                self.milk = self.milk - 75
                self.beans = self.beans - 20
                self.dinero = self.dinero + 7
                self.cups = self.cups - 1
            else:
                if self.agua < 350:
                    print('Sorry, not enough water!')
                elif self.milk < 75:
                    print('Sorry, not enough milk!')
                elif self.beans < 20:
                    print('Sorry, not enough coffee beans!')
                elif self.cups < 1:
                    print('Sorry, not enough cups!')
            print()
        elif coffee == '3':
            if self.agua >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.agua = self.agua - 200
                self.milk = self.milk - 100
                self.beans = self.beans - 12
                self.dinero = self.dinero + 6
                self.cups = self.cups - 1
            else:
                if self.agua < 200:
                    print('Sorry, not enough water!')
                elif self.milk < 100:
                    print('Sorry, not enough milk!')
                elif self.beans < 12:
                    print('Sorry, not enough coffee beans!')
                elif self.cups < 1:
                    print('Sorry, not enough cups!')
            print()

    def Fill(self):
        print('Write how many ml of water do you want to add:')
        self.agua_ = int(input('>>'))
        self.agua = self.agua + self.agua_

        print('Write how many ml of milk do you want to add:')
        self.milk_ = int(input('>>'))
        self.milk = self.milk_ + self.milk

        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_ = int(input('>>'))
        self.beans = self.coffee_ + self.beans

        print('Write how many disposable cups of coffee do you want to add:')
        self.cups_ = int(input('>>'))
        self.cups = self.cups_ + self.cups
        print()

    def Take(self):
        print(f'I gave you ${self.dinero}')
        self.dinero = self.dinero - self.dinero
        print()

    def Remaining(self):
        print(f'The coffee machine has:')
        print(f'{self.agua} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.dinero} of money')
        print()

coffee_test = MachineCoffee()
coffee_test.Iniciar()