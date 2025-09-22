#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    if lsyr[0]%2 == 0:
        n=int((lsyr[0]-1)/3)
    else:
        n=lsyr[0]*2
    title = "Syracuse" + " (n = " + str(n) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    # votre code ici 
    l = [n]
    i=0
    suite=[]
    while n!=1:
        if n%2 == 0:
            n = n//2
        else:
            n=(n*3)+1
        suite.append(n)
    return suite

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    TV=len(l)
    return TV
    # votre code ici

def temps_de_vol_en_altitude(l):
    if l[0]%2 == 0:
        n=int((l[0]-1)/3)
    else:
        n=lsyr[0]*2
    TVA=0
    i = 0
    while l[i] >= n:
        i +=1
    TVA = l[i]
    return TVA

    # votre code ici

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    am=max(l)
    return am


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(18)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()