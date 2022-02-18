# Qu'est-ce qu'une _API_ ?

API signifie *`Application Programming Interface` ou `Interface de Programmation Applicative`*.
C'est une sorte d'Interface qui permet d'interagir avec un système d'information au travers de ce qu'on
appelle des __`endpoints`__.

Chaque *`endpoint`* permet d’exécuter différentes actions dans le système d’information,
sans avoir à en comprendre le fonctionnement.


# Qu'est-ce qu'un _endpoint_ ?

Un endpoint est une *URL sur laquelle on réalise différents appels*.
Selon la méthode HTTP utilisée *__(GET, POST, PATCH, DELETE)__*, une partie de code va
être exécutée et retourner un résultat.

Ce résultat est constitué:
    - D'un __status code__ (200, 201, 400, etc.) qui indique le succès ou non de l'appel;
    - D’un contenu qui est en JSON dans la majorité des cas (peut également être du XML dans certains cas),
    et qui va contenir des informations soit de succès soit d’erreur.
