# Deck Creator for Anki
A web scraping script to create your Anki decs

### Summary
1. Description
2. What is Anki
3. Usage

##### Contact
E-mail: matt-gomes@live.com

LinkedIn: https://www.linkedin.com/in/mattnobre/

------------

### Description
Do you want to study a language? have you a word list to improve your vocabulary? You can use this project to create a Deck into Ankiweb to achieve your goals! Passing a csv file with two columns: 

1. Word -> the word you want to learn
2. Translation -> some translations of this word

You will get a complete translations and how many examples do you want *-*

##### Example

example.csv
```
card  carta, cartão
name  nome
money dinheiro
```

**Return:**
```
card;cartão, caixa, ficha;Create a new address book card entry. Create a new card. New Card. As already stated, this directive is based on the green card system.
name;nome, sinal, marca;If the name of the Constitution is an obstacle, then I am prepared to change the name./I advocate a transparent policy where brand name of origin is obligatory.
money;moeda, grana, dinheiro;It deals with money, in other words - and people know how to use money.
```

##### Contributions
It's just to languages study but fell free to implement others goals.


------------

### What is Anki?
Anki (based on the Japanese word 暗記 anki meaning memorization) is an open source program for memorization cards, originally designed for learning new languages.


You can read more about Anki in [Ankiweb](https://ankiweb.net/about "Ankiweb")

##### Portuguese-English
If you want to learn Portugues-English you can use my "The 1000 most used words in English" deck. Avaliable [here](https://ankiweb.net/shared/info/2116076806 "here")


------------

### Usage
1. Clone this repository
2. Open the terminal
3. run virtualenv env
4. exec env
5. run pip install -r requirements.txt
6. run python main.py

##### Details
1. There is a data examples to try in ./data and ./file
2. Your txt will be save in ./file

##### Requirements
* Python 3.x
* Pip
