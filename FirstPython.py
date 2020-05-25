print('hello python from IntelliJ')

# here, you can add a new repo for new project, if you add a repo in github first,
# then you import this project to github by a command git remote set-url <new repo
# name> then git remote -v to check, then git pull origin master --allowed-unrelated-histories
# also, git clone new ssh, if you want to set up different repo for different projects

x=2
x=x+2
print(x)
if x > 3:
  print('x is bigger than 3.')
print('x is smaller.')
if x > 8:
  print('it is a lie.')
print('ok, now it is working')
if x<2:
  print('x<2')
elif x<3:
  print('x<3')
else:
  print('x is 4')
print('all done')
# here, attention, if, elif and else, you can treat them as a big box, with many statement, if a statement is true, then
# no matter how many more true statement down below the first true statement, only the first statement would be executed.


person = input('Enter a number')
try:
  person2=int(person)
  print('it is a number')
except:
  person2=-1
  print('it is not a number')
print('all done 1')
