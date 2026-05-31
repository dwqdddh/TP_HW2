import pytest
from recipes import Ingredient, Recipe, ShoppingList

def test_create_Ingredient():
    x = Ingredient("Соль", 100, "мг")
    assert x.name == "Соль"
    assert x.quantity == 100.0
    assert x.unit == "мг"

def test_str_Ingredient():
    x = Ingredient("Соль", 100, "мг")
    assert str(x)=="Соль: 100.0 мг"

def test_eq_Ingredient():
    x = Ingredient("Соль", 100, "мг")
    y = Ingredient("Соль", 200, "мг")
    z = Ingredient("Сахар", 100, "мг")
    w = Ingredient("Соль", 100, "г")
    assert x==y
    assert x!=z
    assert x!=w



def test_create_Recipe():
    x = Recipe("Карамель")
    assert x.title == "Карамель"
    assert x.ingredients == []

    y = Recipe("Чай", [Ingredient("Кипяток",200 ,"мл")])
    assert y.title == "Чай"
    assert y.ingredients[0].name == "Кипяток"
    assert y.ingredients[0].quantity == 200.0
    assert y.ingredients[0].unit == "мл"

def test_add_Recipe():
    x = Recipe("Карамель")
    x.add_ingredient(Ingredient("Масло",100,"г"))
    assert x.ingredients[0].name == "Масло" 
    assert x.ingredients[0].quantity == 100.0 
    assert x.ingredients[0].unit == "г" 

    x.add_ingredient(Ingredient("Масло", 200, "г")) 
    assert x.ingredients[0].quantity == 300.0
    assert len(x.ingredients)==1

def test_scale_Recipe():
    x = Recipe("Карамель")
    x.add_ingredient(Ingredient("Масло", 100, "г"))
    x.add_ingredient(Ingredient("Сахар", 200, "г"))

    y = x.scale(3)
    assert type(y) == Recipe
    assert y is not x
    assert y.ingredients[0].quantity == 300.0
    assert y.ingredients[1].quantity == 600.0
    assert x.ingredients[0].quantity == 100.0
    assert x.ingredients[1].quantity == 200.0

    z = Recipe("Тартар")
    with pytest.raises(ValueError):
        z.scale(-10)
    with pytest.raises(ValueError):
        z.scale(0)

def test_len_Recipe():
    x = Recipe("Карамель")
    x.add_ingredient(Ingredient("Масло", 100, "г"))
    x.add_ingredient(Ingredient("Масло", 200, "г"))
    x.add_ingredient(Ingredient("Сахар", 200, "г"))
    assert len(x)==2