name = "CHARLES DICKENS"
dob = "February 7, 1812"
birthplace = "portsmouth, England"
famous_for = "A writer of the Victorian era"
married_to = "Catherine Hogarth"
year_of_marriage = "1836"
number_of_children = "ten"
famous_works = '"A Christmas Carol", "Oliver Twist", "David Copperfield", and "Great Expectations"'
other_talent = "doing DRAMATIC public readings of my work"
death_date = "June 9, 1870"
place_of_death = "Gad's Hill Place, Kent, England"


output_text = f'''Hello. My name is {name.title()}.
I am an English novelist. I was born on {dob}, in {birthplace.title()}.
I am most famous as {famous_for[0].lower()+famous_for[1:]}.
I married {married_to} in {year_of_marriage}. We have {number_of_children} children.
Some of my most famous works include {famous_works}.
Besides being a writer, my other talent was {other_talent.replace("DRAMATIC","dramatic")}.
I died on {death_date}, at my home in {place_of_death}.'''

title =f'''A Brief Profile of {name[0].upper() + '. ' + name.split()[-1].title()} in {len(output_text)} characters.

'''
output_text=title+output_text

print(output_text)

test_text = f'''A Brief Profile of C. Dickens in 505 characters.

Hello. My name is Charles Dickens.
I am an English novelist. I was born on February 7, 1812, in Portsmouth, England.
I am most famous as a writer of the Victorian era.
I married Catherine Hogarth in 1836. We have ten children.
Some of my most famous works include "A Christmas Carol", "Oliver Twist", "David Copperfield", and "Great Expectations".
Besides being a writer, my other talent was doing dramatic public readings of my work.
I died on June 9, 1870, at my home in Gad's Hill Place, Kent, England.'''

if output_text == test_text:
    print("SUCCESS! Yes, your output text matches the test text.")
else:
    print("OOPS!!! Sorry, your output text does not match the test text.")