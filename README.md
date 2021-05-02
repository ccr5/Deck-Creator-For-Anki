[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<p align="center">
  <a href="https://github.com/ccr5/Deck-Creator-For-Anki">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Deck Creator for Anki</h3>

  <p align="center">
    A way to create your Anki decs
    <br />
    <a href="https://github.com/ccr5/Deck-Creator-For-Anki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ccr5/Deck-Creator-For-Anki/issues">Report Bug</a>
    ·
    <a href="https://github.com/ccr5/Deck-Creator-For-Anki/issues">Request Feature</a>
  </p>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
        <a href="#what-is-anki">What is Anki?</a>
        <ul>
            <li><a href="#portuguese-english">Portuguese-English</a></li>
        </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
        <ul>
            <li><a href="#details">Details</a></li>
        </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

Do you want to study a language? have you a word list to improve your vocabulary? You can use this project to create a Deck into Ankiweb to achieve your goals! Passing a csv file with two columns: 

1. Word -> the word you want to learn
2. Translation -> some translations of this word

You will get a complete translations and how many examples do you want *-*

## What is Anki?
Anki (based on the Japanese word 暗記 anki meaning memorization) is an open source program for memorization cards, originally designed for learning new languages.


You can read more about Anki in [Ankiweb](https://ankiweb.net/about "Ankiweb")

### Portuguese-English
If you want to learn Portugues-English you can use my "The 1000 most used words in English" deck. Avaliable [here](https://ankiweb.net/shared/info/2116076806 "here")

## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone this repository
```sh
git clone "https://github.com/ccr5/Deck-Creator-For-Anki.git"
```
2. Open the terminal
3. create a virtual environment 
```sh
virtualenv venv
```
4. exec env
**Linux**
```sh
source venv/bin/activate
```
5. install all dependencies
```sh
pip install -r requirements.txt
```
6. run main.py
```sh
python main.py
```

## Usage

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

### Details
1. There is a data examples to try in ./data and ./file
2. Your txt will be save in ./file

## Roadmap

See the [open issues](https://github.com/ccr5/Deck-Creator-For-Anki/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Matheus Nobre Gomes - matt-gomes@live.com

Project Link: [https://github.com/ccr5/Deck-Creator-For-Anki](https://github.com/ccr5/Deck-Creator-For-Anki)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ccr5/Deck-Creator-For-Anki.svg?style=for-the-badge
[contributors-url]: https://github.com/ccr5/Deck-Creator-For-Anki/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ccr5/Deck-Creator-For-Anki.svg?style=for-the-badge
[forks-url]: https://github.com/ccr5/Deck-Creator-For-Anki/network/members
[stars-shield]: https://img.shields.io/github/stars/ccr5/Deck-Creator-For-Anki.svg?style=for-the-badge
[stars-url]: https://github.com/ccr5/Deck-Creator-For-Anki/stargazers
[issues-shield]: https://img.shields.io/github/issues/ccr5/Deck-Creator-For-Anki.svg?style=for-the-badge
[issues-url]: https://github.com/ccr5/Deck-Creator-For-Anki/issues
[license-shield]: https://img.shields.io/github/license/ccr5/Deck-Creator-For-Anki.svg?style=for-the-badge
[license-url]: https://github.com/ccr5/Deck-Creator-For-Anki/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mattnobre
[product-screenshot]: images/screenshot.png
