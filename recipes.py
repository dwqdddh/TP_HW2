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
        if ingredients!=None:
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
    