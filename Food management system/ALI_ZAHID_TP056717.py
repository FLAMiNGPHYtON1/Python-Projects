#TP056717
#ALI ZAHID





# this function, when called, will reduce the quantity of a food item by the value of FoodQuantityBuy
# if the value of FoodQuantityBuy was greater or equal to the current quantity of the food item,
# the function will print a 'Purchase Successful' message along with returning 'Yes
# if the value of FoodQuantityBuy was lesser than the current quantity of the food item,
# the function will print a error message along with returning 'No'
def purchasing(FoodItemBuy, FoodQuantityBuy):
    with open("Food Item Supply.txt") as Food_Items_Supply_Modify_Txt:
        Food_Item_Supply_List = Food_Items_Supply_Modify_Txt.read().splitlines()
        for Food_Item in Food_Item_Supply_List:
            if FoodItemBuy in Food_Item:
                Position = Food_Item_Supply_List.index(Food_Item)
                Food_Item_Supply_ListModified = Food_Item_Supply_List[Position].split(",")
                if FoodItemBuy in Food_Item_Supply_ListModified:
                    break
        PreviousQuantity = int(Food_Item_Supply_ListModified[1])
        NewQuantity = PreviousQuantity - int(FoodQuantityBuy)
        if NewQuantity < 0:
            print("""The current stock of this food item is lesser than the amount you wish to buy, please enter a lower number, the current stock of this food item is:-""", Food_Item_Supply_ListModified[1])
            return "No"
        else:
            Food_Item_Supply_ListModified[1] = str(NewQuantity)
            print("------------------------------------")
            print(Food_Item_Supply_ListModified[0], ":-", Food_Item_Supply_ListModified[1])
            print("------------------------------------")
            Food_Item_Supply_ListModified = (",".join(Food_Item_Supply_ListModified))
            Food_Item_Supply_List[Position] = str(Food_Item_Supply_ListModified)
            print("======================================================================")
            print("Purchase successful!")
            print("======================================================================")
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))
            return "Yes"

# this function when called will search for a food item which is equal to the value of Food_Item_Search and print a 'Found' message if a match was found
# if nothing was found, this function returns a 'not found' message
def search_function(Food_Item_Search):
    with open("Food Item Supply.txt") as Food_Item_Supply_txt:
        Food_Item_Supply_list_Items = []
        Food_Item_Supply_list_Quantity = []
        Food_Item_Supply_list = Food_Item_Supply_txt.read().splitlines()
        for x in Food_Item_Supply_list:
            Position = Food_Item_Supply_list.index(x)
            Food_Item = Food_Item_Supply_list[Position].split(",")
            Food_Item_Supply_list_Items.append(Food_Item[0])
            Food_Item_Supply_list_Quantity.append(Food_Item[1])
        if Food_Item_Search in Food_Item_Supply_list_Items:
            Position = Food_Item_Supply_list_Items.index(Food_Item_Search)
            print("======================================================================")
            print("Item found!")
            print(Food_Item_Supply_list_Items[Position], ":-", Food_Item_Supply_list_Quantity[Position])
            print("======================================================================")
            return Food_Item_Search
        else:
            print("---------------------------------------------------------------------")
            print("Item not found!")
            print("---------------------------------------------------------------------")
            return "No"

# this function,when called ,will perform one of two actions depending on the value of Option parameter
# if Option is equal to 1, this function will then increase the quantity of a food item by the value of UserQuantity in Food Item Supply.txt
# if Option is equal to 2, this function will then decrease the quantity of a food item by the value of UserQuantity in Food Item Supply.txt
def modify_quantity(FoodItemModify, Option, UserQuantity):
    with open("Food Item Supply.txt") as Food_Items_Supply_Modify_Txt:
        Food_Item_Supply_List = Food_Items_Supply_Modify_Txt.read().splitlines()
        for Food_Item in Food_Item_Supply_List:
            if FoodItemModify in Food_Item:
                Position = Food_Item_Supply_List.index(Food_Item)
                Food_Item_Supply_ListModified = Food_Item_Supply_List[Position].split(",")
                if FoodItemModify in Food_Item_Supply_ListModified:
                    break
        if Option == "1":
            PreviousQuantity = int(Food_Item_Supply_ListModified[1])
            NewQuantity = PreviousQuantity + int(UserQuantity)
            Food_Item_Supply_ListModified[1] = str(NewQuantity)
            print("------------------------------------")
            print(Food_Item_Supply_ListModified[0], ":-", Food_Item_Supply_ListModified[1])
            print("------------------------------------")
            Food_Item_Supply_ListModified = (",".join(Food_Item_Supply_ListModified))
            Food_Item_Supply_List[Position] = str(Food_Item_Supply_ListModified)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))
                Food_Item_Supply_List_Txt.write('\n')
        else:
            PreviousQuantity = int(Food_Item_Supply_ListModified[1])
            NewQuantity = PreviousQuantity - int(UserQuantity)
            if NewQuantity < 0:
                print("""The quantity of this food item is lesser than the amount you wish to decrease it by, please try a lower number, the current quantity of this food item is:-""", Food_Item_Supply_ListModified[1])
            else:
                Food_Item_Supply_ListModified[1] = str(NewQuantity)
                print("------------------------------------")
                print(Food_Item_Supply_ListModified[0], ":-", Food_Item_Supply_ListModified[1])
                print("------------------------------------")
                Food_Item_Supply_ListModified = (",".join(Food_Item_Supply_ListModified))
                Food_Item_Supply_List[Position] = str(Food_Item_Supply_ListModified)
                with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                    Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))
                    Food_Item_Supply_List_Txt.write('\n')

# this function, when called, will carry out a specific action depending on the value of the Option parameter for the fruits category
# if the value of Option is 1, this function will rename a food item which is equal to the value of FoodItemModify parameter
# from the grains category to whatever the value of NewFoodName parameter is in Food Items.txt
# if the value of Option is 2, this function will remove a food item which is equal to the value of FoodItemModify parameter in Food Item.txt
# these actions are then repeated for the file Food Item Supply.txt
def modify_grains_rename_remove(FoodItemModify, Option, NewFoodName):

    with open("Food Items.txt") as Food_Items_Modifytxt:
        Food_Items_List = Food_Items_Modifytxt.read().splitlines()
        Food_Items_Grain_Modified = Food_Items_List[0].split(",")
        if Option == "1":
            Position = Food_Items_Grain_Modified.index(FoodItemModify)
            Food_Items_Grain_Modified[Position] = NewFoodName
            Food_Items_Grain_Modified = [",".join(Food_Items_Grain_Modified)]
            Food_Items_List[0:1] = Food_Items_Grain_Modified
            print("")
            print("------------------------------------")
            print(Food_Items_List[0])
            print("------------------------------------")
            with open("Food Items.txt", "w+") as FoodItems_txtGrains:
                FoodItems_txtGrains.write('\n'.join(Food_Items_List))
                FoodItems_txtGrains.write('\n')
        else:
            Food_Items_Grain_Modified.remove(FoodItemModify)
            Food_Items_Grain_Modified = [",".join(Food_Items_Grain_Modified)]
            Food_Items_List[0:1] = Food_Items_Grain_Modified
            with open("Food Items.txt", "w+") as FoodItems_txtGrains:
                FoodItems_txtGrains.write('\n'.join(Food_Items_List))
                FoodItems_txtGrains.write('\n')
    with open("Food Item Supply.txt") as Food_Item_Supply_Txt:
        Food_Item_Supply_List = Food_Item_Supply_Txt.read().splitlines()
        for Food_Item in Food_Item_Supply_List:
            if FoodItemModify in Food_Item:
                Position = Food_Item_Supply_List.index(Food_Item)
                Food_Item_Supply_ListModified = Food_Item_Supply_List[Position].split(",")
                if FoodItemModify in Food_Item_Supply_ListModified:
                    break
        if Option == "1":
            Food_Item_Supply_ListModified[0] = NewFoodName
            print("------------------------------------")
            print(Food_Item_Supply_ListModified[0], ":-", Food_Item_Supply_ListModified[1])
            print("------------------------------------")
            Food_Item_Supply_ListModified = (",".join(Food_Item_Supply_ListModified))
            Food_Item_Supply_List[Position] = str(Food_Item_Supply_ListModified)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))
        else:
            Food_Item_Supply_List.pop(Position)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))

# this function, when called, will carry out a specific action depending on the value of the Option parameter for the fruits category
# if the value of Option is 1, this function will rename a food item which is equal to the value of FoodItemModify parameter
# from the rawmeats category to whatever the value of NewFoodName parameter is in Food Items.txt
# if the value of Option is 2, this function will remove a food item which is equal to the value of FoodItemModify parameter in Food Item.txt
# these actions are then repeated for the file Food Item Supply.txt
def modify_rawmeats_rename_remove(FoodItemModify, Option, NewFoodName):

    with open("Food Items.txt") as Food_Items_Modifytxt:
        Food_Items_List = Food_Items_Modifytxt.read().splitlines()
        Food_Items_RawMeats_Modified = Food_Items_List[1].split(",")
        if Option == "1":
            Position = Food_Items_RawMeats_Modified.index(FoodItemModify)
            Food_Items_RawMeats_Modified[Position] = NewFoodName
            Food_Items_RawMeats_Modified = [",".join(Food_Items_RawMeats_Modified)]
            Food_Items_List[1:2] = Food_Items_RawMeats_Modified
            print("")
            print("------------------------------------")
            print(Food_Items_List[1])
            print("------------------------------------")
            with open("Food Items.txt", "w+") as FoodItems_txtRawMeats:
                FoodItems_txtRawMeats.write('\n'.join(Food_Items_List))
                FoodItems_txtRawMeats.write('\n')
        else:
            Food_Items_RawMeats_Modified.remove(FoodItemModify)
            Food_Items_RawMeats_Modified = [",".join(Food_Items_RawMeats_Modified)]
            Food_Items_List[1:2] = Food_Items_RawMeats_Modified
            with open("Food Items.txt", "w+") as FoodItems_txtRawMeats:
                FoodItems_txtRawMeats.write('\n'.join(Food_Items_List))
                FoodItems_txtRawMeats.write('\n')
    with open("Food Item Supply.txt") as Food_Item_Supply_Txt:
        Food_Item_Supply_List = Food_Item_Supply_Txt.read().splitlines()
        for Food_Item in Food_Item_Supply_List:
            if FoodItemModify in Food_Item:
                Position = Food_Item_Supply_List.index(Food_Item)
                Food_Item_Supply_ListModified = Food_Item_Supply_List[Position].split(",")
                if FoodItemModify in Food_Item_Supply_ListModified:
                    break
        if Option == "1":
            Food_Item_Supply_ListModified[0] = NewFoodName
            print("------------------------------------")
            print(Food_Item_Supply_ListModified[0], ":-", Food_Item_Supply_ListModified[1])
            print("------------------------------------")
            Food_Item_Supply_ListModified = (",".join(Food_Item_Supply_ListModified))
            Food_Item_Supply_List[Position] = str(Food_Item_Supply_ListModified)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))

        else:
            Food_Item_Supply_List.pop(Position)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))

# this function, when called, will carry out a specific action depending on the value of the Option parameter for the fruits category
# if the value of Option is 1, this function will rename a food item which is equal to the value of FoodItemModify parameter
# from the dairy category to whatever the value of NewFoodName parameter is in Food Items.txt
# if the value of Option is 2, this function will remove a food item which is equal to the value of FoodItemModify parameter in Food Item.txt
# these actions are then repeated for the file Food Item Supply.txt
def modify_dairy_rename_remove(FoodItemModify, Option, NewFoodName):

    with open("Food Items.txt") as Food_Items_Modifytxt:
        Food_Items_List = Food_Items_Modifytxt.read().splitlines()
        Food_Items_Dairy_Modified = Food_Items_List[2].split(",")
        if Option == "1":
            Position = Food_Items_Dairy_Modified.index(FoodItemModify)
            Food_Items_Dairy_Modified[Position] = NewFoodName
            Food_Items_Dairy_Modified = [",".join(Food_Items_Dairy_Modified)]
            Food_Items_List[2:3] = Food_Items_Dairy_Modified
            print("")
            print("------------------------------------")
            print(Food_Items_List[2])
            print("------------------------------------")
            with open("Food Items.txt", "w+") as FoodItems_txtDairy:
                FoodItems_txtDairy.write('\n'.join(Food_Items_List))
                FoodItems_txtDairy.write('\n')
        else:
            Food_Items_Dairy_Modified.remove(FoodItemModify)
            Food_Items_Dairy_Modified = [",".join(Food_Items_Dairy_Modified)]
            Food_Items_List[2:3] = Food_Items_Dairy_Modified
            with open("Food Items.txt", "w+") as FoodItems_txtDairy:
                FoodItems_txtDairy.write('\n'.join(Food_Items_List))
                FoodItems_txtDairy.write('\n')
    with open("Food Item Supply.txt") as Food_Item_Supply_Txt:
        Food_Item_Supply_List = Food_Item_Supply_Txt.read().splitlines()
        for Food_Item in Food_Item_Supply_List:
            if FoodItemModify in Food_Item:
                Position = Food_Item_Supply_List.index(Food_Item)
                Food_Item_Supply_ListModified = Food_Item_Supply_List[Position].split(",")
                if FoodItemModify in Food_Item_Supply_ListModified:
                    break
        if Option == "1":
            Food_Item_Supply_ListModified[0] = NewFoodName
            print("------------------------------------")
            print(Food_Item_Supply_ListModified[0], ":-", Food_Item_Supply_ListModified[1])
            print("------------------------------------")
            Food_Item_Supply_ListModified = (",".join(Food_Item_Supply_ListModified))
            Food_Item_Supply_List[Position] = str(Food_Item_Supply_ListModified)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))
        else:
            Food_Item_Supply_List.pop(Position)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))

# this function, when called, will carry out a specific action depending on the value of the Option parameter for the fruits category
# if the value of Option is 1, this function will rename a food item which is equal to the value of FoodItemModify parameter
# from the vegetables category to whatever the value of NewFoodName parameter is in Food Items.txt
# if the value of Option is 2, this function will remove a food item which is equal to the value of FoodItemModify parameter in Food Item.txt
# these actions are then repeated for the file Food Item Supply.txt
def modify_vegetables_rename_remove(FoodItemModify, Option, NewFoodName):

    with open("Food Items.txt") as Food_Items_Modifytxt:
        Food_Items_List = Food_Items_Modifytxt.read().splitlines()
        Food_Items_Vegetables_Modified = Food_Items_List[3].split(",")
        if Option == "1":
            Position = Food_Items_Vegetables_Modified.index(FoodItemModify)
            Food_Items_Vegetables_Modified[Position] = NewFoodName
            Food_Items_Vegetables_Modified = [",".join(Food_Items_Vegetables_Modified)]
            Food_Items_List[3:4] = Food_Items_Vegetables_Modified
            print("")
            print("------------------------------------")
            print(Food_Items_List[3])
            print("------------------------------------")
            with open("Food Items.txt", "w+") as FoodItems_txtVegetables:
                FoodItems_txtVegetables.write('\n'.join(Food_Items_List))
                FoodItems_txtVegetables.write('\n')
        else:
            Food_Items_Vegetables_Modified.remove(FoodItemModify)
            Food_Items_Vegetables_Modified = [",".join(Food_Items_Vegetables_Modified)]
            Food_Items_List[3:4] = Food_Items_Vegetables_Modified
            with open("Food Items.txt", "w+") as FoodItems_txtVegetables:
                FoodItems_txtVegetables.write('\n'.join(Food_Items_List))
                FoodItems_txtVegetables.write('\n')
    with open("Food Item Supply.txt") as Food_Item_Supply_Txt:
        Food_Item_Supply_List = Food_Item_Supply_Txt.read().splitlines()
        for Food_Item in Food_Item_Supply_List:
            if FoodItemModify in Food_Item:
                Position = Food_Item_Supply_List.index(Food_Item)
                Food_Item_Supply_ListModified = Food_Item_Supply_List[Position].split(",")
                if FoodItemModify in Food_Item_Supply_ListModified:
                    break
        if Option == "1":
            Food_Item_Supply_ListModified[0] = NewFoodName
            print("------------------------------------")
            print(Food_Item_Supply_ListModified[0], ":-", Food_Item_Supply_ListModified[1])
            print("------------------------------------")
            Food_Item_Supply_ListModified = (",".join(Food_Item_Supply_ListModified))
            Food_Item_Supply_List[Position] = str(Food_Item_Supply_ListModified)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))
        else:
            Food_Item_Supply_List.pop(Position)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))

# this function, when called, will carry out a specific action depending on the value of the Option parameter for the fruits category
# if the value of Option is 1, this function will rename a food item which is equal to the value of FoodItemModify parameter
# from the fruits category to whatever the value of NewFoodName parameter is in Food Items.txt
# if the value of Option is 2, this function will remove a food item which is equal to the value of FoodItemModify parameter in Food Item.txt
# these actions are then repeated for the file Food Item Supply.txt
def modify_fruits_rename_remove(FoodItemModify, Option, NewFoodName):

    with open("Food Items.txt") as Food_Items_Modifytxt:
        Food_Items_List = Food_Items_Modifytxt.read().splitlines()
        Food_Items_Fruits_Modified = Food_Items_List[4].split(",")
        if Option == "1":
            Position = Food_Items_Fruits_Modified.index(FoodItemModify)
            Food_Items_Fruits_Modified[Position] = NewFoodName
            Food_Items_Fruits_Modified = [",".join(Food_Items_Fruits_Modified)]
            Food_Items_List[4:5] = Food_Items_Fruits_Modified
            print("")
            print("------------------------------------")
            print(Food_Items_List[4])
            print("------------------------------------")
            with open("Food Items.txt", "w+") as FoodItems_txtFruits:
                FoodItems_txtFruits.write('\n'.join(Food_Items_List))
                FoodItems_txtFruits.write('\n')
        else:
            Food_Items_Fruits_Modified.remove(FoodItemModify)
            Food_Items_Fruits_Modified = [",".join(Food_Items_Fruits_Modified)]
            Food_Items_List[4:5] = Food_Items_Fruits_Modified
            with open("Food Items.txt", "w+") as FoodItems_txtFruits:
                FoodItems_txtFruits.write('\n'.join(Food_Items_List))
                FoodItems_txtFruits.write('\n')
    with open("Food Item Supply.txt") as Food_Item_Supply_Txt:
        Food_Item_Supply_List = Food_Item_Supply_Txt.read().splitlines()
        for Food_Item in Food_Item_Supply_List:
            if FoodItemModify in Food_Item:
                Position = Food_Item_Supply_List.index(Food_Item)
                Food_Item_Supply_ListModified = Food_Item_Supply_List[Position].split(",")
                if FoodItemModify in Food_Item_Supply_ListModified:
                    break
        if Option == "1":
            Food_Item_Supply_ListModified[0] = NewFoodName
            print("------------------------------------")
            print(Food_Item_Supply_ListModified[0], ":-", Food_Item_Supply_ListModified[1])
            print("------------------------------------")
            Food_Item_Supply_ListModified = (",".join(Food_Item_Supply_ListModified))
            Food_Item_Supply_List[Position] = str(Food_Item_Supply_ListModified)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))
        else:
            Food_Item_Supply_List.pop(Position)
            with open("Food Item Supply.txt", "w+") as Food_Item_Supply_List_Txt:
                Food_Item_Supply_List_Txt.write('\n'.join(Food_Item_Supply_List))

# this function, when called, will add a food item with a certain value of quantity using data entered by user
# the food item is entered into the grains category in Food Items.txt.
# this food item is then added again into Food Item Supply.txt with what ever Quantity value was entered
def grains(grain_item, Quantity):

    with open("Food Items.txt", "r") as FoodItems_txtGrains:
        Food_List_Grains = FoodItems_txtGrains.read().splitlines()
        Food_List_Grains1 = Food_List_Grains[0].split(",")
        Food_List_Grains1.append(grain_item)
        Food_List_Grains1 = [",".join(Food_List_Grains1)]
        Food_List_Grains[0:1] = Food_List_Grains1
        print("")
        print("======================================================================")
        print(Food_List_Grains[0])
        print("======================================================================")
        print("")
    with open("Food Items.txt", "w+") as FoodItems_txtGrains:
        FoodItems_txtGrains.write('\n'.join(Food_List_Grains))
        FoodItems_txtGrains.write('\n')
    with open("Food Item Supply.txt", "a") as FoodItemsSupply_txtGrains:
        FoodItemsSupply_txtGrains.write('\n' + str(grain_item) + "," + str(Quantity))

# this function, when called, will add a food item with a certain value of quantity using data entered by user
# the food item is entered into the raw_meats category in Food Items.txt.
# this food item is then added again into Food Item Supply.txt with what ever Quantity value was entered
def raw_meats(rawmeat_item, Quantity):
    with open("Food Items.txt", "r") as FoodItems_txtRawMeats:
        Food_List_RawMeats = FoodItems_txtRawMeats.read().splitlines()
        Food_List_RawMeats1 = Food_List_RawMeats[1].split(",")
        Food_List_RawMeats1.append(rawmeat_item)
        Food_List_RawMeats1 = [",".join(Food_List_RawMeats1)]
        Food_List_RawMeats[1:2] = Food_List_RawMeats1
        print("")
        print("======================================================================")
        print(Food_List_RawMeats[1])
        print("======================================================================")
        print("")
    with open("Food Items.txt", "w+") as FoodItems_txtRawMeats:
        FoodItems_txtRawMeats.write('\n'.join(Food_List_RawMeats))
        FoodItems_txtRawMeats.write('\n')
    with open("Food Item Supply.txt", "a") as FoodItemsSupply_txtRawMeats:
        FoodItemsSupply_txtRawMeats.write('\n' + str(rawmeat_item) + "," + str(Quantity))

# this function, when called, will add a food item with a certain value of quantity using data entered by user
# the food item is entered into the dairy category in Food Items.txt.
# this food item is then added again into Food Item Supply.txt with what ever Quantity value was entered
def dairy(dairy_item, Quantity):
    with open("Food Items.txt", "r") as FoodItems_txtDairy:
        Food_List_Dairy = FoodItems_txtDairy.read().splitlines()
        Food_List_Dairy1 = Food_List_Dairy[2].split(",")
        Food_List_Dairy1.append(dairy_item)
        Food_List_Dairy1 = [",".join(Food_List_Dairy1)]
        Food_List_Dairy[2:3] = Food_List_Dairy1
        print("")
        print("======================================================================")
        print(Food_List_Dairy[2])
        print("======================================================================")
        print("")
    with open("Food Items.txt", "w+") as FoodItems_txtDairy:
        FoodItems_txtDairy.write('\n'.join(Food_List_Dairy))
        FoodItems_txtDairy.write('\n')
    with open("Food Item Supply.txt", "a") as FoodItemsSupply_txtDairy:
        FoodItemsSupply_txtDairy.write('\n' + str(dairy_item) + "," + str(Quantity))

# this function, when called, will add a food item with a certain value of quantity using data entered by user
# the food item is entered into the vegetables category in Food Items.txt.
# this food item is then added again into Food Item Supply.txt with what ever Quantity value was entered
def vegetables(vegetable_item, Quantity):
    with open("Food Items.txt", "r") as FoodItems_txtVegetables:
        Food_List_Vegetables = FoodItems_txtVegetables.read().splitlines()
        Food_List_Vegetables1 = Food_List_Vegetables[3].split(",")
        Food_List_Vegetables1.append(vegetable_item)
        Food_List_Vegetables1 = [",".join(Food_List_Vegetables1)]
        Food_List_Vegetables[3:4] = Food_List_Vegetables1
        print("")
        print("======================================================================")
        print(Food_List_Vegetables[3])
        print("======================================================================")
        print("")
    with open("Food Items.txt", "w+") as FoodItems_txtVegetables:
        FoodItems_txtVegetables.write('\n'.join(Food_List_Vegetables))
        FoodItems_txtVegetables.write('\n')
    with open("Food Item Supply.txt", "a") as FoodItemsSupply_txtVegetables:
        FoodItemsSupply_txtVegetables.write('\n' + str(vegetable_item) + "," + str(Quantity))

# this function, when called, will add a food item with a certain value of quantity using data entered by user
# the food item is entered into the fruits category in Food Items.txt.
# this food item is then added again into Food Item Supply.txt with what ever Quantity value was entered
def fruits(fruit_item, Quantity):
    with open("Food Items.txt", "r") as Food_Items_txtFruits:
        Food_List_Fruits = Food_Items_txtFruits.read().splitlines()
        Food_List_Fruits1 = Food_List_Fruits[4].split(",")
        Food_List_Fruits1.append(fruit_item)
        Food_List_Fruits1 = [",".join(Food_List_Fruits1)]
        Food_List_Fruits[4:5] = Food_List_Fruits1
        print("")
        print("======================================================================")
        print(Food_List_Fruits[4])
        print("======================================================================")
        print("")
    with open("Food Items.txt", "w+") as Food_Items_txtFruits:
        Food_Items_txtFruits.write('\n'.join(Food_List_Fruits))
        Food_Items_txtFruits.write('\n')
    with open("Food Item Supply.txt", "a") as FoodItemsSupply_txtFruits:
        FoodItemsSupply_txtFruits.write('\n' + str(fruit_item) + "," + str(Quantity))

# this function, when called,will append to the User Details.txt text file with data entered in this order (username, account_password) and add "Registered Cus" to the end of every line
def registration(Account_Details):
    with open("User Details.txt", "a") as User_Details_Txt:
        User_Details_Txt.write(str(Account_Details))
    print("")
    print("You are now registered!")

# this function, when called, will, using data entered, open a text file, find a line which matches data,
# and checks if that lines contains Administrator or Registered Customer, which is then returned
def get_user_type(user_name, account_password):
    with open("User Details.txt", "r") as User_Details:
        for line in User_Details:
            User_Data_List = line.split(",")
            if user_name == User_Data_List[0] and account_password == User_Data_List[1]:
                if "Administrator" in line:
                    return "Administrator"
                else:
                    return "Registered_Cus"
        else:
            print("")
            print("----------------------------------------------------------------------")
            print("You have entered an incorrect username or password, please try again")
            print("----------------------------------------------------------------------")
            print("")


# the regcus_menu is the function which creates a menu which users can access after logging in into the program after registering themselves. users are given 4 options
# the first option allows user to view all food categories present in system
# the second option allows user to view all individual food items present in system along with how much stock is currently available for ordering
# the third option allows user to search for a specific food item present in system along with amount of stock available for ordering
# the fourth option returns user back to login screen
def regcus_menu(username, account_password):
    while True:
        BreakCondition = False
        print("")
        print("")
        print("======================================================================")
        print("User type:-", get_user_type(username, account_password))
        print("======================================================================")
        print("Welcome back", username, ", please select what would you like to do")
        print("")
        print("1. View all food categories")
        print("2. View all individual food items available for order")
        print("3. Search for a specific food item to order")
        print("4. Return to login screen")
        print("")
        print("======================================================================")
        Answer = str(input("Enter menu number here:- "))
        print("======================================================================")
        if Answer == "1":
            with open("Food Items.txt") as Food_Items_Txt:
                print("======================================================================")
                for line in Food_Items_Txt:
                    print(line.split(",", 1)[0])
                print("======================================================================")
        elif Answer == "2":
            while True:
                if BreakCondition == True:
                    break
                else:
                    print("======================================================================")
                    with open("Food Item Supply.txt") as Food_Item_Supply_txt:
                        Food_Item_Supply_list_Items = []
                        Food_Item_Supply_list = Food_Item_Supply_txt.read().splitlines()
                        for x in Food_Item_Supply_list:
                            Position = Food_Item_Supply_list.index(x)
                            Food_Item = Food_Item_Supply_list[Position].split(",")
                            Food_Item_Supply_list_Items.append(Food_Item[0])
                    with open("Food Item Supply.txt") as Food_Items_Supply_Txt:
                        Food_Items_Supply_List = Food_Items_Supply_Txt.read().splitlines()
                        for FoodItem in Food_Items_Supply_List:
                            print(FoodItem.split(",")[0], ":-", FoodItem.split(",")[1], "units")
                    while True:
                        print("======================================================================")
                        FoodItemBuy = input("Which food item do you wish to purchase?:- ")
                        print("======================================================================")
                        if FoodItemBuy not in Food_Item_Supply_list_Items:
                            print("---------------------------------------------------------------------")
                            print("Unknown Item!")
                            print("---------------------------------------------------------------------")
                        else:
                            break
                    while True:
                        print("======================================================================")
                        FoodQuantityBuy = str(input("How much of this food item do you wish to buy?:- "))
                        print("======================================================================")
                        if not FoodQuantityBuy.isnumeric():
                            print("---------------------------------------------------------------------")
                            print("Invalid Number!")
                            print("---------------------------------------------------------------------")
                        else:
                            break
                    while True:
                        print("======================================================================")
                        print("Your order is:- ", FoodItemBuy, FoodQuantityBuy, "units")
                        print("Do you wish to confirm your order?")
                        print("1. Yes")
                        print("2. No")
                        print("======================================================================")
                        MenuNumber = str(input("Enter menu number here:- "))
                        print("======================================================================")
                        if MenuNumber == "1":
                            confirmation = purchasing(FoodItemBuy, FoodQuantityBuy)
                            if confirmation == "Yes":
                                with open("Payment confirmation.txt", "a+") as Payment_confirmation_txt:
                                    Payment_Proof = username + "," + FoodItemBuy + "," + FoodQuantityBuy + '\n'
                                    Payment_confirmation_txt.write(str(Payment_Proof))
                                print("======================================================================")
                                print("Do you want to buy another food item?")
                                print("1. Yes")
                                print("2. No")
                                print("======================================================================")
                                MenuNumber = str(input("Enter menu number here:- "))
                                print("======================================================================")
                                if MenuNumber == "1":
                                    break
                                elif MenuNumber == "2":
                                    BreakCondition = True
                                    break
                                else:
                                    print("---------------------------------------------------------------------")
                                    print("You have entered an invalid number")
                                    print("---------------------------------------------------------------------")
                            else:
                                print("======================================================================")
                                print("Do you want to buy another food item?")
                                print("1. Yes")
                                print("2. No")
                                print("======================================================================")
                                MenuNumber = str(input("Enter menu number here:- "))
                                print("======================================================================")
                                if MenuNumber == "1":
                                    break
                                elif MenuNumber == "2":
                                    BreakCondition = True
                                    break
                                else:
                                    print("---------------------------------------------------------------------")
                                    print("You have entered an invalid number, please enter 1 or 2")
                                    print("---------------------------------------------------------------------")
                        elif MenuNumber == "2":
                            BreakCondition = True
                            break
                        else:
                            print("---------------------------------------------------------------------")
                            print("You have entered an invalid answer, please enter 1 or 2")
                            print("---------------------------------------------------------------------")
        elif Answer == "3":
            while True:
                BreakCondition1 = False
                if BreakCondition == True:
                    break
                else:
                    print("======================================================================")
                    Food_Item_Search = input("Enter food item you wish to search for, enter 'None' to return to the previous menu:- ")
                    print("======================================================================")
                    if Food_Item_Search == "None":
                        break
                    else:
                        FoodItemBuy = search_function(Food_Item_Search)
                        if FoodItemBuy == "No":
                            pass
                        else:
                            while True:
                                if BreakCondition1 == True:
                                    break
                                else:
                                    with open("Food Item Supply.txt") as Food_Item_Supply_txt:
                                        Food_Item_Supply_list_Items = []
                                        Food_Item_Supply_list = Food_Item_Supply_txt.read().splitlines()
                                        for x in Food_Item_Supply_list:
                                            Position = Food_Item_Supply_list.index(x)
                                            Food_Item = Food_Item_Supply_list[Position].split(",")
                                            Food_Item_Supply_list_Items.append(Food_Item[0])
                                    print("======================================================================")
                                    print("Do you wish to buy this food item?")
                                    print("1. Yes")
                                    print("2. No")
                                    print("======================================================================")
                                    Answer = str(input("Enter menu number here:- "))
                                    print("======================================================================")
                                    if Answer == "1":
                                        while True:
                                            print("======================================================================")
                                            FoodQuantityBuy = str(input("How much of this food item do you wish to buy?:- "))
                                            print("======================================================================")
                                            if not FoodQuantityBuy.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("Invalid Number!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        while True:
                                            print("======================================================================")
                                            print("Your order is:- ", FoodItemBuy, FoodQuantityBuy, "units")
                                            print("Do you wish to confirm your order?")
                                            print("1. Yes")
                                            print("2. No")
                                            print("======================================================================")
                                            MenuNumber = str(input("Enter menu number here:- "))
                                            print("======================================================================")
                                            if MenuNumber == "1":
                                                confirmation = purchasing(FoodItemBuy, FoodQuantityBuy)
                                                if confirmation == "Yes":
                                                    with open("Payment confirmation.txt", "a+") as Payment_confirmation_txt:
                                                        Payment_Proof = username + "," + FoodItemBuy + "," + FoodQuantityBuy + '\n'
                                                        Payment_confirmation_txt.write(str(Payment_Proof))
                                                    print("======================================================================")
                                                    print("Do you want to buy another food item?")
                                                    print("1. Yes")
                                                    print("2. No")
                                                    print("======================================================================")
                                                    MenuNumber = str(input("Enter menu number here:- "))
                                                    print("======================================================================")
                                                    if MenuNumber == "1":
                                                        BreakCondition1 = True
                                                        break
                                                    elif MenuNumber == "2":
                                                        BreakCondition = True
                                                        BreakCondition1 = True
                                                        break
                                                    else:
                                                        print("---------------------------------------------------------------------")
                                                        print("You have entered an invalid number, please enter 1 or 2")
                                                        print("---------------------------------------------------------------------")
                                                else:
                                                    print("======================================================================")
                                                    print("Do you want to buy another food item?")
                                                    print("1. Yes")
                                                    print("2. No")
                                                    print("======================================================================")
                                                    MenuNumber = str(input("Enter menu number here:- "))
                                                    print("======================================================================")
                                                    if MenuNumber == "1":
                                                        BreakCondition1 = True
                                                        break
                                                    elif MenuNumber == "2":
                                                        BreakCondition = True
                                                        BreakCondition1 = True
                                                        break
                                                    else:
                                                        print("---------------------------------------------------------------------")
                                                        print("You have entered an invalid number, please enter 1 or 2")
                                                        print("---------------------------------------------------------------------")
                                            elif MenuNumber == "2":
                                                BreakCondition = True
                                                BreakCondition1 = True
                                                break
                                            else:
                                                print("---------------------------------------------------------------------")
                                                print("You have entered an invalid answer, please enter 1 or 2")
                                                print("---------------------------------------------------------------------")
                                    elif Answer == "2":
                                        BreakCondition = True
                                        break
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("You have entered an invalid answer, please enter 1 or 2")
                                        print("---------------------------------------------------------------------")


        elif Answer == "4":
            break
        else:
            print("---------------------------------------------------------------------")
            print("You have entered an incorrect answer, please enter a number from 1 to 4")
            print("---------------------------------------------------------------------")


# the cus_menu function is the first menu which users see when this program is initialized, 4 options are given which are selected by entering number 1 to 4 in given prompt.
# the first option allows user to see all food items present in system according to category
# the second option allows user to register themselves to the program, which allows them to login into the program and be allowed access more details/functionalities of the program
# the third option takes user to the login menu
# the fourth option stops the program with an exit message
def cus_menu():

    with open("Food Item Supply Template.txt") as Food_Items_Supply_Template_Txt:
        Food_Items_Supply_Template_Txt = Food_Items_Supply_Template_Txt.read().splitlines()
    with open("Food Item Supply.txt", "w+") as Food_Item_Supply_Txt:
        Food_Item_Supply_Txt.write('\n'.join(Food_Items_Supply_Template_Txt))
    with open("User Details Template.txt") as User_Details_Template_Txt:
        User_Details_Template = User_Details_Template_Txt.read().splitlines()
    with open("User Details.txt", "w+") as User_Details_Txt:
        User_Details_Txt.write('\n'.join(User_Details_Template))
    with open("Food Items Template.txt") as Food_Items_Template_Txt:
        Food_Item_Template = Food_Items_Template_Txt.read().splitlines()
    with open("Food Items.txt", "w+") as Food_Items_Txt:
        Food_Items_Txt.write('\n'.join(Food_Item_Template))
        Food_Items_Txt.write('\n')
    with open("Payment confirmation.txt", "w") as Payment_confirmation_Txt:
        Payment_confirmation_Txt.close()
    while True:
        print("======================================================================")
        print("I                        Welcome Customer!                           I")
        print("======================================================================")
        print("Please select a menu option via entering the numbers listed")
        print("")
        print("1. View all food items in each category")
        print("2. Become a Registered Customer")
        print("3. Login to program")
        print("4. Exit the program")
        print("")
        Answer = str(input("Enter Menu Number Here:- "))
        if Answer == "1":
            with open("Food Items.txt") as Food_Items_Txt:
                print("======================================================================")
                for line in Food_Items_Txt:
                    print(line.split(",", 1)[0], ":-", line.split(",", 1)[1])
                print("======================================================================")
        elif Answer == "2":
            print("")
            user_name = str(input("Please enter your desired username:- "))
            print("")
            account_password = str(input("Please enter your desired password:- "))
            Account_Details = '\n' + user_name + "," + account_password + "," + "Registered_Cus"
            registration(Account_Details)
        elif Answer == "3":
            program_start()
        elif Answer == "4":
            exit("You have exited the program")
        else:
            print("---------------------------------------------------------------------")
            print("You have entered an incorrect number, please enter 1,2,3 or 4")
            print("---------------------------------------------------------------------")


# This is admin menu where user can enter a number from 1 to 5 which allows them to select from 5 different options
# the first option allows them to add a new food item into any of the 5 pre defined food categories in the system
# the second option allows a user to modify a food item's details such as its name and how much stock is available in program. User can also delete food item from program
# the third option allows user to see various data present in program, such as food categories, food items in each category, successful customer orders detailing customer name, food item bought, and amount of food item purchased
# the fourth option allows user to search all orders made by a specific registered customer in program
# the fifth option logs user out of program and takes him/her back to the login screen
def admin_menu(username, account_password):
    while True:
        BreakCondition = False
        print("")
        print("")
        print("======================================================================")
        print("User type:-", get_user_type(username, account_password))
        print("======================================================================")
        print("Welcome back", username,)
        print("Please select a menu option via entering the numbers listed")
        print("")
        print("1. Add a new food Item into a pre-existing category")
        print("2. Modify a food item's details")
        print("3. Access records present in System")
        print("4. Search a specific customer's order/payments in system")
        print("5. Return to login Screen")

        print("======================================================================")
        MenuNumber = str(input("Enter menu number here:- "))
        print("======================================================================")

        if MenuNumber == "5":
            break
        elif MenuNumber == "1":
            BreakCondition = False
            while True:
                if BreakCondition == True:
                    break
                else:
                    print("======================================================================")
                    print("Please select which food category do you wish to add a new food item to:- ")
                    print("")
                    print("1. Grains")
                    print("2. RawMeats")
                    print("3. Dairy")
                    print("4. Vegetables")
                    print("5. Fruits")
                    print("")
                    print("======================================================================")
                    CategoryMenuNumber = str(input("Enter menu number here:- "))
                    print("======================================================================")
                    with open("Food Items.txt", "r") as FoodItems_txt:
                        Food_List = FoodItems_txt.read().splitlines()
                        Food_List_Grains1 = Food_List[0].split(",")
                        Food_List_RawMeats1 = Food_List[1].split(",")
                        Food_List_Dairy1 = Food_List[2].split(",")
                        Food_List_Vegetables1 = Food_List[3].split(",")
                        Food_List_Fruits1 = Food_List[4].split(",")
                        Food_Items_Modify1 = Food_List_Fruits1 + Food_List_Vegetables1 + Food_List_Dairy1 + Food_List_RawMeats1 + Food_List_Grains1
                        if CategoryMenuNumber == "1":
                            while True:
                                print("======================================================================")
                                Answer = input("Please enter the name of the food item you wish to add to the Grains Category:- ")
                                print("======================================================================")
                                if Answer not in Food_List_Grains1 and Answer not in Food_Items_Modify1:
                                    if not Answer.isalpha():
                                        print("---------------------------------------------------------------------")
                                        print("You have entered a invalid food item, please enter a different food item")
                                        print("---------------------------------------------------------------------")
                                    else:
                                        break
                                else:
                                    print("---------------------------------------------------------------------")
                                    print("You have entered a invalid food item, please enter a different food item")
                                    print("---------------------------------------------------------------------")
                            while True:
                                print("======================================================================")
                                Quantity = input("Please enter the amount of food item you are adding to the system:- ")
                                print("======================================================================")
                                if not Quantity.isnumeric():
                                    print("---------------------------------------------------------------------")
                                    print("Quantity of food item can only be defined by numbers!")
                                    print("---------------------------------------------------------------------")
                                else:
                                    break
                            grains(Answer, Quantity)
                        elif CategoryMenuNumber == "2":
                            while True:
                                print("======================================================================")
                                Answer = input("Please enter the name of the food item you wish to add to the Raw Meats Category:- ")
                                print("======================================================================")
                                if Answer not in Food_List_RawMeats1 and Answer not in Food_Items_Modify1:
                                    if not Answer.isalpha():
                                        print("---------------------------------------------------------------------")
                                        print("You have entered a invalid food item, please enter a different food item")
                                        print("---------------------------------------------------------------------")
                                    else:
                                        break
                                else:
                                    print("---------------------------------------------------------------------")
                                    print("You have entered a invalid food item, please enter a different food item")
                                    print("---------------------------------------------------------------------")
                            while True:
                                print("======================================================================")
                                Quantity = input("Please enter the amount of food item you are adding to the system:- ")
                                print("======================================================================")
                                if not Quantity.isnumeric():
                                    print("---------------------------------------------------------------------")
                                    print("Quantity of food item can only be defined by numbers!")
                                    print("---------------------------------------------------------------------")
                                else:
                                    break
                            raw_meats(Answer, Quantity)
                        elif CategoryMenuNumber == "3":
                            while True:
                                print("======================================================================")
                                Answer = input("Please enter the name of the food item you wish to add to the Dairy Category:- ")
                                print("======================================================================")
                                if Answer not in Food_List_Dairy1 and Answer not in Food_Items_Modify1:
                                    if not Answer.isalpha():
                                        print("---------------------------------------------------------------------")
                                        print("You have entered a invalid food item, please enter a different food item")
                                        print("---------------------------------------------------------------------")
                                    else:
                                        break
                                else:
                                    print("---------------------------------------------------------------------")
                                    print("You have entered a invalid food item, please enter a different food item")
                                    print("---------------------------------------------------------------------")
                            while True:
                                Quantity = input("Please enter the amount of food item you are adding to the system:- ")
                                if not Quantity.isnumeric():
                                    print("---------------------------------------------------------------------")
                                    print("Quantity of food item can only be defined by numbers!")
                                    print("---------------------------------------------------------------------")
                                else:
                                    break
                            dairy(Answer, Quantity)
                        elif CategoryMenuNumber == "4":
                            while True:
                                print("======================================================================")
                                Answer = input("Please enter the name of the food item you wish to add to the Vegetables Category:- ")
                                print("======================================================================")
                                if Answer not in Food_List_Vegetables1 and Answer not in Food_Items_Modify1:
                                    if not Answer.isalpha():
                                        print("---------------------------------------------------------------------")
                                        print("You have entered a invalid food item, please enter a different food item")
                                        print("---------------------------------------------------------------------")
                                    else:
                                        break
                                else:
                                    print("---------------------------------------------------------------------")
                                    print("You have entered a invalid food item, please enter a different food item")
                                    print("---------------------------------------------------------------------")
                            while True:
                                print("======================================================================")
                                Quantity = input("Please enter the amount of food item you are adding to the system:- ")
                                print("======================================================================")
                                if not Quantity.isnumeric():
                                    print("---------------------------------------------------------------------")
                                    print("Quantity of food item can only be defined by numbers!")
                                    print("---------------------------------------------------------------------")
                                else:
                                    break
                            vegetables(Answer, Quantity)
                        elif CategoryMenuNumber == "5":
                            while True:
                                print("======================================================================")
                                Answer = input("Please enter the name of the food item you wish to add to the Fruits Category:- ")
                                print("======================================================================")
                                if Answer not in Food_List_Fruits1 and Answer not in Food_Items_Modify1:
                                    if not Answer.isalpha():
                                        print("---------------------------------------------------------------------")
                                        print("You have entered a invalid food item, please enter a different food item")
                                        print("---------------------------------------------------------------------")
                                    else:
                                        break
                                else:
                                    print("---------------------------------------------------------------------")
                                    print("You have entered a invalid food item, please enter a different food item")
                                    print("---------------------------------------------------------------------")
                            while True:
                                print("======================================================================")
                                Quantity = input("Please enter the amount of food item you are adding to the system:- ")
                                print("======================================================================")
                                if not Quantity.isnumeric():
                                    print("---------------------------------------------------------------------")
                                    print("Quantity of food item can only be defined by numbers!")
                                    print("---------------------------------------------------------------------")
                                else:
                                    break
                            fruits(Answer, Quantity)
                        else:
                            print("---------------------------------------------------------------------")
                            print("You have entered an invalid answer!")
                            print("---------------------------------------------------------------------")
                while True:
                    print("======================================================================")
                    print("Would you like to add another food item or return to the admin screen?:- ")
                    print("")
                    print("1. Add another food item")
                    print("2. Return to admin menu ")
                    print("")
                    print("======================================================================")
                    RepeatQuestionAnswer = str(input("Enter menu number here:- "))
                    print("======================================================================")
                    if RepeatQuestionAnswer == "1":
                        break
                    elif RepeatQuestionAnswer == "2":
                        BreakCondition = True
                        break
                    else:
                        print("---------------------------------------------------------------------")
                        print("You have entered an invalid answer, please enter number 1 or 2")
                        print("---------------------------------------------------------------------")

        elif MenuNumber == "2":
            while True:
                if BreakCondition == True:
                    break
                else:
                    New_Food_Name = "0"
                    with open("Food Items.txt") as Food_Items_Txt:
                        print("======================================================================")
                        for line in Food_Items_Txt:
                            print(line.split(",", 1)[0], ":-", line.split(",", 1)[1])
                    with open("Food Items.txt") as Food_Items_ModifyTxt:
                        Food_Items_Modify_list = Food_Items_ModifyTxt.read().splitlines()
                        Food_Items_Modify_Grain_list = Food_Items_Modify_list[0].split(",")
                        Food_Items_Modify_RawMeats_list = Food_Items_Modify_list[1].split(",")
                        Food_Items_Modify_Dairy_list = Food_Items_Modify_list[2].split(",")
                        Food_Items_Modify_Vegetables_list = Food_Items_Modify_list[3].split(",")
                        Food_Items_Modify_Fruits_list = Food_Items_Modify_list[4].split(",")
                        Food_Items_Modify1 = Food_Items_Modify_Fruits_list + Food_Items_Modify_Vegetables_list + Food_Items_Modify_Dairy_list + Food_Items_Modify_RawMeats_list + Food_Items_Modify_Grain_list
                        while True:
                            print("===============================================================================================")
                            ModifyFood = input("Which Food Item do you wish to Modify? Enter 'None' if you wish to return to the admin menu:- ")
                            print("===============================================================================================")
                            if ModifyFood != Food_Items_Modify_Grain_list[0] and ModifyFood != Food_Items_Modify_RawMeats_list[0] and ModifyFood != Food_Items_Modify_Dairy_list[0] and ModifyFood != Food_Items_Modify_Vegetables_list[0] and ModifyFood != Food_Items_Modify_Fruits_list[0]:
                                break
                            else:
                                print("---------------------------------------------------------------------")
                                print("You can't modify category names!")
                                print("---------------------------------------------------------------------")

                        if ModifyFood == "None":
                            break
                        elif ModifyFood in Food_Items_Modify_Grain_list:
                            print("")
                            print("What do you wish to change about this food item?")
                            print("")
                            print("1. Rename food item")
                            print("2. Remove food item")
                            print("3. Increase/Decrease food item quantity")
                            print("4. Return to admin menu")
                            print("")
                            print("======================================================================")
                            Follow_up_answer = str(input("Enter menu number here:- "))
                            print("======================================================================")
                            if Follow_up_answer == "1":
                                while True:
                                    New_Food_Name = input("What do you wish to rename this food item to?:- ")
                                    print("================================================================================================")
                                    if New_Food_Name.isalpha():
                                        if New_Food_Name not in Food_Items_Modify1:
                                            modify_grains_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                                            break
                                        else:
                                            print("---------------------------------------------------------------------")
                                            print("You cannot rename food items to a name which already exists!")
                                            print("---------------------------------------------------------------------")
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("Please only use letters to rename this food item, special characters and numbers are not allowed")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "2":
                                modify_grains_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                            elif Follow_up_answer == "3":
                                while True:
                                    print("==============================================================")
                                    print("Do you wish to increase or decrease this food item's quantity?")
                                    print("==============================================================")
                                    print("")
                                    print("1. Increase this food item's quantity")
                                    print("2. Decrease this food item's quantity")
                                    print("3. Return to modify menu")
                                    print("")
                                    print("=======================================================")
                                    Follow_up_answer2 = input("Enter menu number here:- ")
                                    print("=======================================================")
                                    if Follow_up_answer2 == "3":
                                        break
                                    elif Follow_up_answer2 == "1":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to increase this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    elif Follow_up_answer2 == "2":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to decrease this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("You have entered an incorrect number, please enter 1,2 or 3")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "4":
                                break
                            else:
                                print("---------------------------------------------------------------------")
                                print("You have entered an invalid number, please select your food item again and enter 1,2,3 or 4 only")
                                print("---------------------------------------------------------------------")
                        elif ModifyFood in Food_Items_Modify_RawMeats_list:
                            print("")
                            print("What do you wish to change about this food item?")
                            print("")
                            print("1. Rename food item")
                            print("2. Remove food item")
                            print("3. Increase/Decrease food item quantity")
                            print("4. Return to admin menu")
                            print("")
                            print("======================================================================")
                            Follow_up_answer = input("Enter menu number here:- ")
                            print("======================================================================")
                            if Follow_up_answer == "1":
                                while True:
                                    New_Food_Name = input("What do you wish to rename this food item to?:- ")
                                    print("================================================================================================")
                                    if New_Food_Name.isalpha():
                                        if New_Food_Name not in Food_Items_Modify1:
                                            modify_rawmeats_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                                            break
                                        else:
                                            print("---------------------------------------------------------------------")
                                            print("You cannot rename food items to a name which already exists!")
                                            print("---------------------------------------------------------------------")
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("Please only use letters to rename this food item, special characters and numbers are not allowed")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "2":
                                modify_rawmeats_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                            elif Follow_up_answer == "3":
                                while True:
                                    print("==============================================================")
                                    print("Do you wish to increase or decrease this food item's quantity?")
                                    print("==============================================================")
                                    print("")
                                    print("1. Increase this food item's quantity")
                                    print("2. Decrease this food item's quantity")
                                    print("3. Return to admin menu")
                                    print("")
                                    print("=======================================================")
                                    Follow_up_answer2 = input("Enter menu number here:- ")
                                    print("=======================================================")
                                    if Follow_up_answer2 == "3":
                                        BreakCondition = True
                                        break
                                    elif Follow_up_answer2 == "1":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to increase this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    elif Follow_up_answer2 == "2":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to decrease this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("You have entered an invalid number, please enter 1,2 or 3")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "4":
                                break
                            else:
                                print("---------------------------------------------------------------------")
                                print("You have entered an invalid number, please select your food item again and enter 1,2,3 or 4 only")
                                print("---------------------------------------------------------------------")
                        elif ModifyFood in Food_Items_Modify_Dairy_list:
                            print("")
                            print("What do you wish to change about this food item?")
                            print("")
                            print("1. Rename food item")
                            print("2. Remove food item")
                            print("3. Increase/Decrease food item quantity")
                            print("4. Return to admin menu")
                            print("")
                            print("======================================================================")
                            Follow_up_answer = input("What do you wish to change?:- ")
                            print("======================================================================")
                            if Follow_up_answer == "1":
                                while True:
                                    New_Food_Name = input("What do you wish to rename this food item to?:- ")
                                    print("================================================================================================")
                                    if New_Food_Name.isalpha():
                                        if New_Food_Name not in Food_Items_Modify1:
                                            modify_dairy_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                                            break
                                        else:
                                            print("---------------------------------------------------------------------")
                                            print("You cannot rename food items to a name which already exists!")
                                            print("---------------------------------------------------------------------")
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("Please only use letters to rename this food item, special characters and numbers are not allowed")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "2":
                                modify_dairy_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                            elif Follow_up_answer == "3":
                                while True:
                                    print("==============================================================")
                                    print("Do you wish to increase or decrease this food item's quantity?")
                                    print("==============================================================")
                                    print("")
                                    print("1. Increase this food item's quantity")
                                    print("2. Decrease this food item's quantity")
                                    print("3. Return to admin menu")
                                    print("")
                                    print("=======================================================")
                                    Follow_up_answer2 = input("Enter menu number here:- ")
                                    print("=======================================================")
                                    if Follow_up_answer2 == "3":
                                        BreakCondition = True
                                        break
                                    elif Follow_up_answer2 == "1":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to increase this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    elif Follow_up_answer2 == "2":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to decrease this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("You have entered an invalid number, please enter 1,2 or 3")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "4":
                                break
                            else:
                                print("---------------------------------------------------------------------")
                                print("You have entered an invalid number, please select your food item again and enter 1,2,3 or 4 only")
                                print("---------------------------------------------------------------------")
                        elif ModifyFood in Food_Items_Modify_Vegetables_list:
                            print("")
                            print("What do you wish to change about this food item?")
                            print("")
                            print("1. Rename food item")
                            print("2. Remove food item")
                            print("3. Increase/Decrease food item quantity")
                            print("4. Return to admin menu")
                            print("")
                            print("======================================================================")
                            Follow_up_answer = input("What do you wish to change?:- ")
                            print("======================================================================")
                            if Follow_up_answer == "1":
                                while True:
                                    New_Food_Name = input("What do you wish to rename this food item to?:- ")
                                    print("================================================================================================")
                                    if New_Food_Name.isalpha():
                                        if New_Food_Name not in Food_Items_Modify1:
                                            modify_vegetables_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                                            break
                                        else:
                                            print("---------------------------------------------------------------------")
                                            print("You cannot rename food items to a name which already exists!")
                                            print("---------------------------------------------------------------------")
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("Please only use letters to rename this food item, special characters and numbers are not allowed")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "2":
                                modify_vegetables_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                            elif Follow_up_answer == "3":
                                while True:
                                    print("==============================================================")
                                    print("Do you wish to increase or decrease this food item's quantity?")
                                    print("==============================================================")
                                    print("")
                                    print("1. Increase this food item's quantity")
                                    print("2. Decrease this food item's quantity")
                                    print("3. Return to admin menu")
                                    print("")
                                    print("=======================================================")
                                    Follow_up_answer2 = input("Enter menu number here:- ")
                                    print("=======================================================")
                                    if Follow_up_answer2 == "3":
                                        BreakCondition = True
                                        break
                                    elif Follow_up_answer2 == "1":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to increase this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    elif Follow_up_answer2 == "2":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to decrease this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("You have entered an invalid number, please enter 1,2 or 3")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "4":
                                break
                            else:
                                print("---------------------------------------------------------------------")
                                print("You have entered an invalid number, please select your food item again and enter 1,2,3 or 4 only")
                                print("---------------------------------------------------------------------")
                        elif ModifyFood in Food_Items_Modify_Fruits_list:
                            print("")
                            print("What do you wish to change about this food item?")
                            print("")
                            print("1. Rename food item")
                            print("2. Remove food item")
                            print("3. Increase/Decrease food item quantity")
                            print("4. Return to admin menu")
                            print("")
                            print("======================================================================")
                            Follow_up_answer = input("What do you wish to change?:- ")
                            print("======================================================================")
                            if Follow_up_answer == "1":
                                while True:
                                    New_Food_Name = input("What do you wish to rename this food item to?:- ")
                                    print("================================================================================================")
                                    if New_Food_Name.isalpha():
                                        if New_Food_Name not in Food_Items_Modify1:
                                            modify_grains_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                                            break
                                        else:
                                            print("---------------------------------------------------------------------")
                                            print("You cannot rename food items to a name which already exists!")
                                            print("---------------------------------------------------------------------")
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("Please only use letters to rename this food item, special characters and numbers are not allowed")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "2":
                                modify_fruits_rename_remove(ModifyFood, Follow_up_answer, New_Food_Name)
                            elif Follow_up_answer == "3":
                                while True:
                                    print("==============================================================")
                                    print("Do you wish to increase or decrease this food item's quantity?")
                                    print("==============================================================")
                                    print("")
                                    print("1. Increase this food item's quantity")
                                    print("2. Decrease this food item's quantity")
                                    print("3. Return to admin menu")
                                    print("")
                                    print("=======================================================")
                                    Follow_up_answer2 = input("Enter menu number here:- ")
                                    print("=======================================================")
                                    if Follow_up_answer2 == "3":
                                        BreakCondition = True
                                        break
                                    elif Follow_up_answer2 == "1":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to increase this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    elif Follow_up_answer2 == "2":
                                        while True:
                                            print("=======================================================")
                                            Quantity = input("By how much do you wish to decrease this food item's quantity?:- ")
                                            print("=======================================================")
                                            if not Quantity.isnumeric():
                                                print("---------------------------------------------------------------------")
                                                print("You can only use numbers!")
                                                print("---------------------------------------------------------------------")
                                            else:
                                                break
                                        modify_quantity(ModifyFood, Follow_up_answer2, Quantity)
                                    else:
                                        print("---------------------------------------------------------------------")
                                        print("You have entered an invalid number, please enter 1,2 or 3")
                                        print("---------------------------------------------------------------------")
                            elif Follow_up_answer == "4":
                                break
                            else:
                                print("================================================================================================")
                                print("You have entered an invalid number, please select your food item again and enter 1,2,3 or 4 only")
                                print("================================================================================================")
                        else:
                            print("---------------------------------------------------------------------")
                            print("You have entered a unknown item, please try again")
                            print("---------------------------------------------------------------------")
        elif MenuNumber == "3":
            while True:
                print("======================================================================")
                print("I    Please select which records you wish to access in the system    I")
                print("======================================================================")
                print("")
                print("1. Food Categories")
                print("2. Food Items")
                print("3. Customer Orders")
                print("4. Return to Admin Menu")
                print("")
                print("======================================================================")
                RecordMenuNumber = input(" Enter menu number here:- ")
                print("======================================================================")
                if RecordMenuNumber == "4":
                    break
                elif RecordMenuNumber == "1":
                    with open("Food Items.txt") as Food_Items_Txt:
                        print("======================================================================")
                        for line in Food_Items_Txt:
                            print(line.split(",", 1)[0])
                        print("======================================================================")
                elif RecordMenuNumber == "2":
                    with open("Food Items.txt") as Food_Items_Txt:
                        print("======================================================================")
                        for line in Food_Items_Txt:
                            print(line.split(",", 1)[0], ":-", line.split(",", 1)[1])
                        print("======================================================================")
                elif RecordMenuNumber == "3":
                    with open("Payment confirmation.txt") as Payment_confirmation_Txt:
                        print("")
                        print("======================================================================")
                        for line in Payment_confirmation_Txt:
                            if line.isspace():
                                continue
                            else:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Customer:- ", line.split(",", 2)[0])
                                print("Item:- ", line.split(",", 2)[1])
                                print("Units:- ", line.split(",", 2)[2])
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("======================================================================")
                        print("")
                else:
                    print("---------------------------------------------------------------------")
                    print("You have entered an invalid answer, please enter a number from 1 to 4")
                    print("---------------------------------------------------------------------")
        elif MenuNumber == "4":
            while True:
                if BreakCondition == True:
                    break
                else:
                    print("======================================================================")
                    customer_name = input("Which customer's order records do you wish to find?:- ")
                    print("======================================================================")
                    with open("Payment confirmation.txt") as Payment_confirmation_Txt:
                        Payment_list1 = Payment_confirmation_Txt.read().splitlines()
                        if customer_name not in Payment_list1:
                            print("---------------------------------------------------------------------")
                            print("no records found!")
                            print("---------------------------------------------------------------------")
                        if not Payment_list1:
                            print("---------------------------------------------------------------------")
                            print("no records found!")
                            print("---------------------------------------------------------------------")
                        else:
                            for x in Payment_list1:
                                if customer_name in x:
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Customer:- ", x.split(",", 2)[0])
                                    print("Item:- ", x.split(",", 2)[1])
                                    print("Units:- ", x.split(",", 2)[2])
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                    while True:
                        print("======================================================================")
                        print("Do you wish to search again?")
                        print("")
                        print("1. Yes")
                        print("2. Return to admin menu")
                        print("")
                        print("======================================================================")
                        Answer = input("Enter menu number here?:- ")
                        print("======================================================================")
                        if Answer == "1":
                            break
                        elif Answer == "2":
                            BreakCondition = True
                            break
                        else:
                            print("---------------------------------------------------------------------")
                            print("You have entered an invalid answer, please enter 1 or 2")
                            print("---------------------------------------------------------------------")

        else:
            print("")
            print("---------------------------------------------------------------------")
            print("You have entered an invalid answer, please enter a number from 1 to 5")
            print("---------------------------------------------------------------------")


# this function, when called, will ask user for user_name and password, which is then verified through calling another function
# if the verification is successful, the user is then taken to their respective menus.
def program_start():
    while True:
        print("")
        print("======================================================================")
        print("I                         Welcome User                               I")
        print("======================================================================")
        print("")
        user_name = input("Enter your username here or enter 'None' to return the main menu:- ")
        if user_name == "None":
            break
        else:
            if user_name.isspace():
                print("---------------------------------------------------------------------")
                print("Invalid username!")
                print("---------------------------------------------------------------------")
            else:
                account_password = input(str("Enter your password here:- "))
                user_type = get_user_type(user_name, account_password)
                if user_type == "Administrator":
                    admin_menu(user_name, account_password)
                elif user_type == "Registered_Cus":
                    regcus_menu(user_name, account_password)
                else:
                    print("---------------------------------------------------------------------")
                    print("Unknown user!")
                    print("---------------------------------------------------------------------")


cus_menu()


# Problem = program thinking accepting using letters for login and id, and allowing access, added verification
# UserDetails = open("D:\\Documents\\Degree\\Python Programming\\Assignment Files\\Py Files\\User Details.txt","r")
# for line in UserDetails:
#     UserDataList = line.split()
#     print(UserDataList[1])