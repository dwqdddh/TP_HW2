class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value<=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value
    
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        if type(other) != Ingredient:
            return False
        return self.name==other.name and self.unit==other.unit


class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        self.ingredients = []
        if ingredients is not None:
            for i in ingredients:
                self.add_ingredient(i)
                
    def add_ingredient(self, ingredient: Ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if (type(ratio)==int or type(ratio)==float) and ratio>0:
            return True
        return False
    
    def scale(self, ratio:float):
        if Recipe.is_valid_ratio(ratio)==False:
            raise ValueError("Не положительный коэффицент:", ratio)
        ratio_recipe = Recipe(self.title)
        for i in self.ingredients:
            ratio_recipe.add_ingredient(Ingredient(i.name, i.quantity*ratio, i.unit))
        return ratio_recipe
    
    def __str__(self):
        string = f"{self.title} (список ингредиентов):"
        for i in self.ingredients:
            string += f"\n{i}" 
        return string 

    def __len__(self):
        return len(self.ingredients)


class ShoppingList:
    def __init__(self):
        self._items = []
            
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        for i in recipe.scale(portions).ingredients:
            self._items.append((i, recipe.title))

    def remove_recipe(self, title: str):
        new = []
        for i in self._items:
            if i[1]!=title:
                new.append(i)
        self._items = new

    def get_list(self):
        dictionary = {}
        for i in self._items:
            ingredient = i[0]
            key = (ingredient.name, ingredient.unit)
            if key in dictionary:
                dictionary[key]+= ingredient.quantity
            else:
                dictionary[key] = ingredient.quantity
        
        mas = []
        for i in dictionary:
            mas.append(Ingredient(i[0], dictionary[i], i[1]))
        mas.sort(key=lambda i: i.name)
        return mas
    
    def __add__(self, other):
        new = ShoppingList()
        new._items = self._items + other._items
        return new