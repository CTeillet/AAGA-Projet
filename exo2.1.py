import random
import ternary_trie


def gen_arbre_tern(titre, nb_words):
    with open('Shakespeare/' + titre + '.txt', 'r') as f:
        lines = f.readlines()
        res_words = []
        for _ in range(nb_words):
            res_words.append(random.choice(lines).strip())

        arbre = ternary_trie.gener_feuille()
        for word in res_words:
            print(word)
            arbre = ternary_trie.insert(arbre, word)
    return arbre


def fusion(titre1, titre2, nb_words):
    arbre1 = gen_arbre_tern(titre1, nb_words)
    print(find_words(arbre1))
    # print(arbre1.affiche())
    arbre2 = gen_arbre_tern(titre2, nb_words)
    arbre3 = ternary_trie.fusion(arbre1, arbre2)
    return arbre3


def find_words(arbre):
    return find_words_aux(arbre, "", [])


def find_words_aux(arbre, s_temp, res):
    if arbre.is_feuille():
        return res
    else:
        if arbre.val == 0:
            s_temp2 = s_temp + arbre.cle
            res.append(s_temp2)
        for i in range(len(arbre.fils)):
            fils = arbre.fils[i]
            if i == 1:
                s_temp2 = s_temp + arbre.cle
                res = find_words_aux(fils, s_temp2, res)
            else:
                res = find_words_aux(fils, s_temp, res)
        return res


def is_sorted(liste):
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
    return True


abr = find_words(fusion('romeo_juliet', '1henryiv', 15))
print(abr)
print(is_sorted(abr))
