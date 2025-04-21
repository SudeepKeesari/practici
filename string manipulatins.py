#slicing
str= "python programming"
substring=str[7:19]
print(substring)

#striding
text="hello world"
rev=text[::-1]
wish=text[::2] #prints character at desired place
print(rev, wish)

#concatenate
fst="sai"
sec="sudeep"
#out=fst + sec
print(fst+ " "+sec)

#finding characters
tex="python is programming language"
position=tex.find("is")
print(position)

#replacing chars and substrings
word="c is a programmable language"
updated_word=word.replace("c","python")
print(updated_word)

#splitting strings
input="hi hello world!"
oup=input.split()
print(oup)

#join words
ip=["a","e","i","o","u"]
op="".join(ip)


#formatting
name="sai"
age="19"
msg= "my name is {} of age {}".format(name,age)
print(msg)