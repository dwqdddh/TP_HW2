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
