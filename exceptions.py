#Define a class that inherits from an exception type
class InvalidArgumentsError(Exception):
    def __init__(self, num_of_args):
        # Set some exception infomation
        self.num_of_args = num_of_args
	print "Should have 4 arguments, but you had " + num_of_args


