import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from average import function

def test_moyenne_normale():
    assert function([10, 20, 30]) == 20

def test_moyenne_un_element():
    assert function([42]) == 42

def test_moyenne_vide():
    assert function([]) == 0

def test_moyenne_negatifs():
    assert function([-10, 10]) == 0