people = [
  {
    'name': 'Мария',
    'interests': ['пътуване', 'танци', 'плуване', 'кино'],
    'gender': 'female'
  },
  {
    'name': 'Диана',
    'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
    'gender': 'female'
  },
  {
    'name': 'Дарина',
    'interests': ['покер', 'автомобили', 'танци', 'кино'],
    'gender': 'female'
  },
  {
    'name': 'Галя',
    'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
    'gender': 'female'
  },
  {
    'name': 'Валерия',
    'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
    'gender': 'female'
  },
  {
    'name': 'Ина',
    'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
    'gender': 'female'
  },
  {
    'name': 'Кирил',
    'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
    'gender': 'male'
  },
  {
    'name': 'Георги',
    'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
    'gender': 'male'
  },
  {
    'name': 'Андрей',
    'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
    'gender': 'male'
  },
  {
    'name': 'Емил',
    'interests': ['летене', 'баскетбол', 'софтуер', 'баскетбол'],
    'gender': 'male'
  },
  {
    'name': 'Димитър',
    'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
    'gender': 'male'
  },
  {
    'name': 'Петър',
    'interests': ['плуване', 'покер', 'баскетбол', 'лов със соколи'],
    'gender': 'male'
  },
  {
    'name': 'Калоян',
    'interests': ['история', 'покер', 'пътуване', 'автомобили'],
    'gender': 'male'
  }
]

females = []
males = []

for person in people:
    person['interests'] = set(person['interests'])

    if person['gender'] == 'female':
        females.append(person)
    else:
        males.append(person)

couples = []

for female in females:
    for male in males:
        if 'coupled' not in male and len(female['interests'].intersection(male['interests'])) > 0:
            couples.append([female, male])
            female['coupled'] = True
            male['coupled'] = True
            break

for male in males:
    male['interests'] = list(male['interests'])
    female['interests'] = list(female['interests'])

left_over_females = list(filter(lambda f: 'coupled' not in f, females))
left_over_males = list(filter(lambda m: 'coupled' not in m, males))

print('''
  couples: {}

  left over females: {}
  
  left over males: {}
'''.format(couples, left_over_females, left_over_males))