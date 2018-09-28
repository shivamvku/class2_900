# try :
# 	a = int(input('Enter a numbr -1 \n'))
# 	b = int(input('Enter a numbr -2 \n'))

# 	print(a/b)

# except ZeroDivisionError:
# 	print('There is zero in denominator')
# except ValueError:
# 	print('Check yout input')



# try :
# 	a = int(input('Enter a numbr -1 \n'))
# 	b = int(input('Enter a numbr -2 \n'))
# 	a/b

# except (ZeroDivisionError,ValueError):
# 	print('Check your input\n')

# else:
# 	print(a/b)

# finally:
# 	print('Program excution completed')
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning


# a = 25 

class Error(Exception):
	pass
class OverageError(Error):
	pass
class UnderageError(Error):
	pass
class NotYetBoarnError(Error):
	pass

age = 24

try:
	in_age = int(input('Guess the age of the person\n'))

	if in_age <= 0:
		raise NotYetBoarnError
	elif in_age < age:
		raise UnderageError
	elif in_age > age:
		raise OverageError
except NotYetBoarnError:
	print('The person is not yet boarn\n')
except UnderageError:
	print('The person is more older than you think.....\n')
except OverageError:
	print('The person is more younger than you think......\n')

else:
	print('You have gusesed the correct age\n')
finally:
	print('Finised eecution')