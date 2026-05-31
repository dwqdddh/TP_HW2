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



def test_add_recipe_ShoppingList():
    x = Recipe("Карамель") 
    x.add_ingredient(Ingredient("Сахар", 200, "г")) 
    shop = ShoppingList()
    shop.add_recipe(x,1.5) 
    
    assert shop._items[0][1] == "Карамель" 
    assert shop._items[0][0].name == "Сахар" 
    assert shop._items[0][0].quantity == 300.0 
    with pytest.raises(ValueError): 
        shop.add_recipe(x, 0) 
    with pytest.raises(ValueError): 
        shop.add_recipe(x, -1)

def test_remove_ShoppingList():
    shop = ShoppingList()
    shop._items = [(Ingredient("Сахар", 200, "г"), "Карамель"),
        (Ingredient("Масло", 100, "г"), "Карамель"),
        (Ingredient("Мука", 300, "г"), "Печенье")]

    shop.remove_recipe("Карамель")

    assert len(shop._items) == 1
    assert shop._items[0][0].name == "Мука"
    assert shop._items[0][1] == "Печенье"

    shop.remove_recipe("Торт")

    assert len(shop._items) == 1
    assert shop._items[0][0].name == "Мука"

def test_get_list_ShoppingList():
    shop = ShoppingList() 
    shop._items = [ (Ingredient("Сахар", 200, "г"), "Карамель"), 
                   (Ingredient("Масло", 100, "г"), "Карамель"), 
                   (Ingredient("Сахар", 300, "г"), "Печенье"), 
                   (Ingredient("Яйцо", 2, "шт"), "Печенье") ]
    mas = shop.get_list()

    assert len(mas) == 3 
    assert mas[0].name == "Масло" 
    assert mas[0].quantity == 100.0 
    assert mas[1].name == "Сахар" 
    assert mas[1].quantity == 500.0 
    assert mas[2].name == "Яйцо" 
    assert mas[2].quantity == 2.0

def test_add_ShoppingList():
    x = ShoppingList()
    x._items = [(Ingredient("Сахар", 200, "г"), "Карамель")]
    y = ShoppingList()
    y._items = [(Ingredient("Масло", 100, "г"), "Печенье")]
    new = x + y

    assert len(x._items) == 1
    assert x._items[0][0].name == "Сахар"
    assert len(y._items) == 1
    assert y._items[0][0].name == "Масло"
    assert new is not x
    assert new is not y
    assert len(new._items) == 2
    assert new._items[0][0].name == "Сахар"
    assert new._items[1][0].name == "Масло"