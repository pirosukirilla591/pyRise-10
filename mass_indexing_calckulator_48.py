
# Калькулятор ИМТ ( Индекс Массы Тела)
print("Здравствуйте! Меня зовут Pie-Rise The Sound, я бот. Давайте посчитаем вам ИМТ...")

weight = float(input("Какой у вас вес(кг)?: "))
height = float(input("Какой у вас рост(см)?: "))

print("Отлично, делаем вычисления...")
print("Звуки работающего механизма*")

bmi = weight / ((height / 100) * (height / 100))
print("Ваш ИМТ равен ", bmi)

print("Подсчёт нормы ИМТ ...")
print("* звуки калькулятора тыц-тыц-тыц*")
print("")


if bmi >= 18.5: 
    print("Походу вы стали есть много булочек! Это очень плохо, запишитесь в тренажёрный зал...")