class A(object):

    @property
    def name(self):
        return self.get_name()

    def get_name(self):
        return "In class A"


class B(A):

    def get_name(self):
        return "In class B"


a = B()
print(a.name)
