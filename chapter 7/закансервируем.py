# Законсервируем
# Демонстрирует консервацию даных и доступ к ним через интерфейс полки

import pickle
import shelve

print('Консервация списков')
variety = ['огурцы', 'помидор', 'капуста']
shape = ['целые', 'кубиками', 'соломкой']
brand = ['Главпродукт', 'Чумак', 'Бондюэль']
f = open('pickles1.dat', 'wb')

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print('\nРасконсервация списков.')
f = open('pickles1.dat', 'rb')
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print('\nПомещаем списков на полку')
s = shelve.open('pickles2.dat')
s['variety'] = ['огурцы', 'помидор', 'капуста']
s['shape'] = ['целые', 'кубиками', 'соломкой']
s['brand'] = ['Главпродукт', 'Чумак', 'Бондюэль']
s.sync()  # убедимся, что данные записаны

print('\nИзвлечения списков из файла:')
print('торговые марки -', s['brand'])
print('формы - ', s['shape'])
print('вид овощей -', s['variety'])
s.close

input('\nНажмите Enter, что бы выйти.\n')
