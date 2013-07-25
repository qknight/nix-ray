import tpv.cli

from tpv.ordereddict import OrderedDict


class Bar(OrderedDict):
    """Install something

    And a longer descriptions for it.

    Stretching over multiple lines.
    """
    jiha = tpv.cli.Flag(["j", "jiha"],
                        help="If given, I will be very foo")

    def __call__(self, *programs):
        print("Removing %s %s" % (self.foo, programs,))

cmd = Bar()
