macroFunctions=("authentication","payments","reports")
print("Macro-functions are: \n",macroFunctions)
# tuples are immutable so we cannot change it, so the following commented lines will not work
# macroFunctions.append("hello")
# print("Tried to append the tuple: \n",macroFunctions)
# alternatively we can add one tuple with another one
microFunctions=("registration","login","logout")
macroFunctions+=microFunctions
print("After incrementing the first tuple with the second one: \n",macroFunctions)

# we can also join two tuples
components=macroFunctions+microFunctions
print("After adding two tuples together as components: \n",components)