recipients = ["john@test.com", "james@test.com", "adam@test.com", "loen@test.com"]

print(recipients)

expected = "john@test.com;james@test.com;adam@test.com;loen@test.com"

to = ";".join(recipients)

print(to)
print(expected)

print(to == expected)
print("#" * 100)
# how-to-join-list-in-python-but-make-the-last-separator-different

langs = ["Python", "PHP", "Ruby", "Go"]

expected = "I Love langs Python, PHP, Ruby and Go"

joining_lags = ", ".join(langs[:-1])
last_lang = langs[-1]

print(joining_lags)
print(last_lang)

actual = "I Love langs " + joining_lags + " and " + last_lang

print(expected)
print(actual)
print(expected == actual)

# split

domain = "www.test.com/images/dogs/germanshepherd.png"

img_name = domain.split("/")[-1]

print(img_name)
