# "Const" definition (It's not really const, it's just for display)
MAX_VALUE = 999999999
MIN_VALUE = 100000000


def check_id_valid(id_number):
    """Check if the number is valid  in israel.
       :param id_number: a number between 111,111,111 and 999,999,999
        type id_number: int

       :return: if the number is valid  in israel
       :rtype: bool

       """
    # Casting to string for easy parsing
    id_number = str(id_number)

    # Sum all odd digit (from index 0 until 8, by 2 steps)
    sum_ = sum([int(id_number[i]) for i in range(0, 9, 2)])

    # Sum all even digit (from 1 index until 8 by 2 steps, and combination of 2 digits)
    sum_ += sum([((int(id_number[i]) * 2) // 10) + int(id_number[i]) % 10 for i in range(1, 8, 2)])

    # checking control digit
    if sum_ % 10 == 0:
        return True
    return False


class IDIterator:

    """ A class create valid ID numbers
        until MAX number
        Attributes:
           _id = current id number

        Methods:
            __init__ =Initialize _id attributes
            __iter__ = return the current id number
            __next__ =Run on the number line until you get stuck on a correct number
        raises :
            StopIteration : when the next id number big then MAX_VALUE

        """
    def __init__(self, id_number):
        self._id = id_number

    def __iter__(self):
        return self

    def __next__(self):
        i = self._id

        # Run on the number line
        while True:
            i += 1
            #  Until you get stuck
            if i >= MAX_VALUE:
                raise StopIteration("can't create number big as {}".format(MAX_VALUE))

            # Or find a correct number
            if check_id_valid(i):
                self._id = i

                return i


def id_generator(id_number):
    """  Id_generator create valid ID numbers.
       param: id_number: base ID between 111,111,111 and 999,999,999
       type: id_number: int

       :yield:
                next valid id number
       :yield type : int

       raises :
                StopIteration : when the next id number is bigger than MAX_VALUE
       """

    # Initialize  a loop variable
    i = id_number

    # Long run on all the numbers
    while True:
        i += 1
        if i >= MAX_VALUE:

            # Until we get stuck
            raise StopIteration("can't create number big as {}".format(MAX_VALUE))

        # Or find a correct number
        if check_id_valid(i):
            yield i


def main():
    """    Main function receive id number from user
            and method to create ids
            and after that give to user 10 valid id
       return:None
       raises :
                ValueError -  when id_number input isn't number or smaller / bigger
                        when method input is not 'it' or 'gen'
       """


    # Input and check input
    id_number = input("enter your id number ")

    try:
        if not id_number.isnumeric():
            raise TypeError("{} was not a number ".format(id_number))

        # Casting
        id_number = int(id_number)

        # Check input as number
        if id_number < MIN_VALUE or id_number > MAX_VALUE:
            raise ValueError(
                '{} the number bigger or smaller then  normal ID_number '
                .format(id_number))
    # When user enter not a number input
    except TypeError as te:
        print(te)

    # When user enter invalid number
    except ValueError as ve:
        print(ve)

    # When other failure
    except Exception as e:
        print(e)
    # The program continue when aren't problems
    else:
        # select options to create,
        # input and check input
        try:
            create_function = input("Generator or Iterator? (gen/it)? ")
            if create_function == 'gen':
                n = id_generator(id_number)

            elif create_function == 'it':
                n = IDIterator(id_number)

            else:
                raise ValueError(" the input isn't relevant ")

            # Create ID numbers by select function (respectively)
            for i in range(10):
                print(n.__next__())
        # When is happened problem from generator
        except RuntimeError as rt:
            print(rt)

        # When user enter not relevant input
        except ValueError as ve:
            print(ve)

        # When iterator finish all numbers
        except StopIteration as esi:
            print(esi)

        # When other failure
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()