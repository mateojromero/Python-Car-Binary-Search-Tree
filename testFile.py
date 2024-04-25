from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

class Test_Car:
    
    def test_init(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        assert str(c1) == 'Make: DODGE, Model: CRV, Year: 2007, Price: $8000'

    def test_gt(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('honda', 'odyssey', 2009, 9000)
        assert c2 > c1
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('dodge', 'charger', 2009, 9000)
        assert c1 > c2
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('dodge', 'CRV', 2009, 9000)
        assert c2 > c1
        c1 = Car('dodge', 'CRV', 2009, 8000)
        c2 = Car('dodge', 'CRV', 2009, 9000)
        assert c2 > c1

    def test_lt(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('honda', 'odyssey', 2009, 9000)
        assert c1 < c2
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('dodge', 'charger', 2009, 9000)
        assert c2 < c1
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('dodge', 'CRV', 2009, 9000)
        assert c1 < c2
        c1 = Car('dodge', 'CRV', 2009, 8000)
        c2 = Car('dodge', 'CRV', 2009, 9000)
        assert c1 < c2

    def test_eq(self):
        c1 = Car('Toyota', 'Camry', 2009, 5000)
        assert not (c1 == None)
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('dOdGe', 'CrV', 2007, 8000)
        assert c1 == c2

    def test_str(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        assert str(c1) == 'Make: DODGE, Model: CRV, Year: 2007, Price: $8000'

class Test_CarInventoryNode:

    def test_init(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        node = CarInventoryNode(c1)
        assert node.get_make() == 'DODGE'
        assert node.get_model() == 'CRV'
        assert len(node.cars) == 1
        assert node.parent is None
        assert node.left is None
        assert node.right is None

    def test_get_make(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        node = CarInventoryNode(c1)
        assert node.get_make() == 'DODGE'

    def test_get_model(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        node = CarInventoryNode(c1)
        assert node.get_model() == 'CRV'

    def test_get_parent(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('honda', 'odyssey', 2009, 9000)
        parent_node = CarInventoryNode(c1)
        child_node = CarInventoryNode(c2)
        child_node.set_parent(parent_node)
        assert child_node.get_parent() == parent_node

    def test_set_parent(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('honda', 'odyssey', 2009, 9000)
        parent_node = CarInventoryNode(c1)
        child_node = CarInventoryNode(c2)
        child_node.set_parent(parent_node)
        assert child_node.parent == parent_node

    def test_get_left(self):
        parent_car = Car('dodge', 'CRV', 2007, 8000)
        left_car = Car('honda', 'odyssey', 2009, 9000)
        parent_node = CarInventoryNode(parent_car)
        left_node = CarInventoryNode(left_car)
        parent_node.set_left(left_node)
        assert parent_node.get_left() == left_node
    
    def test_set_left(self):
        parent_car = Car('dodge', 'CRV', 2007, 8000)
        left_car = Car('honda', 'odyssey', 2009, 9000)
        parent_node = CarInventoryNode(parent_car)
        left_node = CarInventoryNode(left_car)
        parent_node.set_left(left_node)
        assert parent_node.get_left() == left_node

    def test_get_right(self):
        parent_car = Car('dodge', 'CRV', 2007, 8000)
        right_car = Car('honda', 'odyssey', 2009, 9000)
        parent_node = CarInventoryNode(parent_car)
        right_node = CarInventoryNode(right_car)
        parent_node.set_right(right_node)
        assert parent_node.get_right() == right_node
    
    def set_right(self):
        parent_car = Car('dodge', 'CRV', 2007, 8000)
        right_car = Car('honda', 'odyssey', 2009, 9000)
        parent_node = CarInventoryNode(parent_car)
        right_node = CarInventoryNode(right_car)
        parent_node.set_right(right_node)
        assert parent_node.get_right() == right_node

    def test_str(self):
        c1 = Car('dodge', 'CRV', 2007, 8000)
        c2 = Car('dodge', 'CRV', 2009, 9000)
        node = CarInventoryNode(c1)
        node.cars.append(c2) 
        result = 'Make: DODGE, Model: CRV, Year: 2007, Price: $8000\nMake: DODGE, Model: CRV, Year: 2009, Price: $9000\n'
        assert str(node) == result
        

class Test_CarInventory:

    def test_init(self):
        inventory = CarInventory()
        assert inventory.root is None

    def test_add_car_and_insert(self):
        inventory = CarInventory()
        car = Car('Tesla', 'Model S', 2020, 70000)
        inserted_node = inventory.insert(None, car)
        assert inserted_node is not None
        assert inserted_node.get_make() == 'TESLA'
        assert inserted_node.get_model() == 'MODEL S'
        assert len(inserted_node.cars) == 1

    def test_does_car_exist(self):
        inventory = CarInventory()
        assert not inventory.does_car_exist(Car('dodge', 'CRV', 2007, 8000))
        inventory = CarInventory()
        inventory.add_car(Car('dodge', 'CRV', 2007, 8000))
        inventory.add_car(Car('honda', 'odyssey', 2009, 10000))
        assert inventory.does_car_exist(Car('dodge', 'CRV', 2007, 8000))
        assert not inventory.does_car_exist(Car('ford', 'mustang', 2010, 12000))
        assert not inventory.does_car_exist(Car('dodge', 'CRV', 2009, 9000))
        assert not inventory.does_car_exist(Car('dodge', 'CRA', 2007, 8000))
        assert not inventory.does_car_exist(Car('dodge', 'CRW', 2007, 8000))

    def test_inorder(self):
        inventory = CarInventory()
        inventory.add_car(Car('dodge', 'CRV', 2007, 8000))
        inventory.add_car(Car('dodge', 'charger', 2009, 9000))
        inventory.add_car(Car('honda', 'odyssey', 2009, 9000))
        assert inventory.inorder() == 'Make: DODGE, Model: CHARGER, Year: 2009, Price: $9000\nMake: DODGE, Model: CRV, Year: 2007, Price: $8000\nMake: HONDA, Model: ODYSSEY, Year: 2009, Price: $9000\n'

    def test_preorder(self):
        inventory = CarInventory()
        inventory.add_car(Car('dodge', 'CRV', 2007, 8000))
        inventory.add_car(Car('honda', 'odyssey', 2009, 9000))
        inventory.add_car(Car('dodge', 'charger', 2009, 9000))
        assert inventory.preorder() == 'Make: DODGE, Model: CRV, Year: 2007, Price: $8000\nMake: DODGE, Model: CHARGER, Year: 2009, Price: $9000\nMake: HONDA, Model: ODYSSEY, Year: 2009, Price: $9000\n'

    def test_postorder(self):
        inventory = CarInventory()
        inventory.add_car(Car('dodge', 'CRV', 2007, 8000))
        inventory.add_car(Car('honda', 'odyssey', 2009, 9000))
        inventory.add_car(Car('dodge', 'charger', 2009, 9000))
        assert inventory.postorder() == 'Make: DODGE, Model: CHARGER, Year: 2009, Price: $9000\nMake: HONDA, Model: ODYSSEY, Year: 2009, Price: $9000\nMake: DODGE, Model: CRV, Year: 2007, Price: $8000\n'

    def test_get_best_car(self):
        inventory = CarInventory()
        inventory.add_car(Car('Honda', 'Odyssey', 2010, 15000))
        inventory.add_car(Car('Honda', 'Odyssey', 2009, 14000))
        inventory.add_car(Car('Honda', 'Civic', 2011, 12000))
        inventory.add_car(Car('Dodge', 'Charger', 2012, 16000))
        inventory.add_car(Car('Honda', 'Odyssey', 2010, 14500))
        inventory.add_car(Car('Honda', 'Odyssey', 2008, 13000))
        inventory.add_car(Car('Honda', 'Civic', 2011, 11500))
        inventory.add_car(Car('Honda', 'Odyssey', 2008, 13500))
        inventory.add_car(Car('Honda', 'Pilot', 2012, 18000))
        inventory.add_car(Car('Honda', 'Pilot', 2013, 19000))       
        b1 = inventory.get_best_car('Honda', 'Odyssey')
        assert str(b1) == 'Make: HONDA, Model: ODYSSEY, Year: 2010, Price: $15000'
        b2 = inventory.get_best_car('Honda', 'Civic')
        assert str(b2) == 'Make: HONDA, Model: CIVIC, Year: 2011, Price: $12000'
        none_car = inventory.get_best_car('Ford', 'Focus')
        assert none_car is None
        b3 = inventory.get_best_car('HONDA', 'ODYSSEY')
        assert str(b3) == 'Make: HONDA, Model: ODYSSEY, Year: 2010, Price: $15000'
        b4 = inventory.get_best_car('HoNdA', 'OdYsSeY')
        assert str(b4) == 'Make: HONDA, Model: ODYSSEY, Year: 2010, Price: $15000'
        b5 = inventory.get_best_car('Honda', 'Pilot')
        assert str(b5) == 'Make: HONDA, Model: PILOT, Year: 2013, Price: $19000'

    def test_get_worst_car(self):
        inventory = CarInventory()
        inventory.add_car(Car('Honda', 'Odyssey', 2010, 15000))
        inventory.add_car(Car('Honda', 'Odyssey', 2009, 14000))
        inventory.add_car(Car('Honda', 'Civic', 2011, 12000))
        inventory.add_car(Car('Dodge', 'Charger', 2012, 16000))
        inventory.add_car(Car('Honda', 'Odyssey', 2010, 14500))
        inventory.add_car(Car('Honda', 'Odyssey', 2008, 13000))
        inventory.add_car(Car('Honda', 'Civic', 2011, 11500))
        inventory.add_car(Car('Honda', 'Odyssey', 2008, 13500))
        inventory.add_car(Car('Honda', 'Pilot', 2012, 18000))
        inventory.add_car(Car('Honda', 'Pilot', 2013, 19000))
        w1 = inventory.get_worst_car('Honda', 'Odyssey')
        assert str(w1) == 'Make: HONDA, Model: ODYSSEY, Year: 2008, Price: $13000'
        w2 = inventory.get_worst_car('Honda', 'Civic')
        assert str(w2) == 'Make: HONDA, Model: CIVIC, Year: 2011, Price: $11500'
        none_car = inventory.get_worst_car('Ford', 'Focus')
        assert none_car is None
        w3 = inventory.get_worst_car('HONDA', 'ODYSSEY')
        assert str(w3) == 'Make: HONDA, Model: ODYSSEY, Year: 2008, Price: $13000'
        w4 = inventory.get_worst_car('HoNdA', 'OdYsSeY')
        assert str(w4) == 'Make: HONDA, Model: ODYSSEY, Year: 2008, Price: $13000'
        w5 = inventory.get_worst_car('Honda', 'Pilot')
        assert str(w5) == 'Make: HONDA, Model: PILOT, Year: 2012, Price: $18000'

    def test_get_total_inventory_price(self):
        inventory = CarInventory()
        inventory.add_car(Car('dodge', 'CRV', 2007, 8000))
        inventory.add_car(Car('honda', 'odyssey', 2009, 9000))
        inventory.add_car(Car('dodge', 'charger', 2009, 9000))
        total_price = inventory.get_total_inventory_price()
        assert total_price == 26000

    def test_get_successor(self):
        inventory = CarInventory()
        inventory.add_car(Car('Honda', 'Odyssey', 2010, 15000))
        inventory.add_car(Car('Honda', 'Civic', 2011, 12000))
        inventory.add_car(Car('Dodge', 'Charger', 2012, 16000))
        inventory.add_car(Car('Tesla', 'Model S', 2020, 70000))
        successor = inventory.get_successor('Dodge', 'Charger')
        assert successor is not None
        assert successor.make == 'HONDA' and successor.model == 'CIVIC'
        successor = inventory.get_successor('Honda', 'Civic')
        assert successor is not None
        assert successor.make == 'HONDA' and successor.model == 'ODYSSEY'
        successor = inventory.get_successor('Honda', 'Odyssey')
        assert successor is not None
        assert successor.make == 'TESLA' and successor.model == 'MODEL S'
        successor = inventory.get_successor('Tesla', 'Model S')
        assert successor is None

    def test_remove_car(self):
        inventory = CarInventory()
        c1 = Car('Honda', 'Odyssey', 2010, 15000)
        c2 = Car('Honda', 'Odyssey', 2009, 14000)
        c3 = Car('Honda', 'Civic', 2011, 12000)
        c4 = Car('Dodge', 'Charger', 2012, 16000)
        c5 = Car('Honda', 'Odyssey', 2013, 19000)
        inventory.add_car(c1)
        inventory.add_car(c2)
        inventory.add_car(c3)
        inventory.add_car(c4)
        inventory.add_car(c5)
        assert inventory.remove_car('Honda', 'Odyssey', 2010, 15000) == True
        assert inventory.does_car_exist(Car('Honda', 'Odyssey', 2009, 14000))
        assert inventory.does_car_exist(Car('Honda', 'Civic', 2011, 12000))
        assert inventory.does_car_exist(Car('Dodge', 'Charger', 2012, 16000))
        assert inventory.does_car_exist(Car('Honda', 'Odyssey', 2013, 19000))
        assert inventory.remove_car('Honda', 'Civic', 2011, 12000) == True
        assert inventory.remove_car('Honda', 'Odyssey', 2009, 14000) == True
        assert inventory.remove_car('Dodge', 'Charger', 2012, 16000) == True
        assert inventory.remove_car('Honda', 'Odyssey', 2013, 19000) == True
        assert inventory.root is None
