import sys


class GeneratorInterface(object):
    def Generate(self):
        raise NotImplementedError("Should have implemented Generate")


class GeneratorGenerator(GeneratorInterface):
    def __init__(self, some_yielder_class, yielder_init_args=None):
        self.generatee = some_yielder_class
        self.yielder_init_args = yielder_init_args

    def Generate(self, iterations):
        for x in range(0, iterations):
            if self.yielder_init_args is not None:
                gen = self.generatee(self.yielder_init_args)
            else:
                gen = self.generatee()

            yield gen


class ExampleGenerator(GeneratorInterface):
    def Generate(self, iterations):
        for x in range(0, iterations):
            yield 'This is example number ' + str(x)

if __name__ == "__main__":
    gen = GeneratorGenerator(ExampleGenerator)

    counter = 0
    for generator in gen.Generate(3):
        counter += 1

        print('This is generator number ' + str(counter))

        for x in generator.Generate(3):
            print(str(x) + ' of generator number ' + str(counter))
