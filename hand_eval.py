from treys import Card, Evaluator
import random
    

table = [Card.new('Ah'), Card.new('Kd'), Card.new('7d'), Card.new("Ac"), Card.new("6h")]

jeff = [Card.new('Qs'), Card.new('Th')]

sam = [Card.new('As'), Card.new('Th')]

eval = Evaluator()

print(eval.evaluate(table, jeff))
print(eval.evaluate(table, sam))