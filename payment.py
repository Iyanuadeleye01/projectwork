firstnames = ('pedro', 'toyin', 'dayo','iyanu')
lastnames = ('oye','ojo','bello','tosin')
ages = (34,43,34,23)
total_age =sum(ages)
average_age = total_age/len(ages)
for firstname, lastname, age in zip(firstnames,lastnames,ages):
    if age > average_age:
        print(f'{firstname} {lastname} is old')
    else:
        print(f' {firstname} {lastname} is young')
        
