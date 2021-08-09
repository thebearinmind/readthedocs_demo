class Person:
  """This is a test class for the Sphinx docs
  """
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    """This is a test function for the sphinx docs

    Args:
        abc (str): Person object
    """
    print("Hello my name is " + abc.name)