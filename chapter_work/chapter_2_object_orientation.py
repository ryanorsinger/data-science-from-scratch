class CountingClicker:
    """ A class can/should have a docstring """
    def __init__(self, count = 0):
        self.count = count
    
    def __repr__():
        """ Object's representation of itself """
        return f"CountingClicker(count={self.count})"

    def click(self, num_times = 1):
        """ Click the counter some number of times """
        self.count += num_times
    
    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start at zero"
clicker.click()
clicker.click()
assert clicker.read() == 2, "clicked twice should count twice"
clicker.reset()
clicker.read() == 0, "reset sets to zero"
clicker.click()
clicker.read() == 1, "One click"
