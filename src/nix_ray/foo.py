import tpv.cli


class Foo(tpv.cli.Command):
    """Install something

    And a longer descriptions for it.

    Stretching over multiple lines.
    """
    abc = tpv.cli.Flag(["a", "abc"],
                       help="If given, I will be very foo")

    def __call__(self, *programs):
        print("Removing %s %s" % (self.foo, programs,))


class Baz(tpv.cli.Command):
    """Install something

    And a longer descriptions for it.

    Stretching over multiple lines.
    """
    baaz = tpv.cli.Flag(["b", "baaz"],
                        help="If given, I will be very foo")

    def __call__(self, *programs):
        print("Removing %s %s" % (self.foo, programs,))
