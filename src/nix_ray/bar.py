import tpv.cli


class Bar(tpv.cli.Command):
    """Install something

    And a longer descriptions for it.

    Stretching over multiple lines.
    """
    jiha = tpv.cli.Flag(["j", "jiha"],
                        help="If given, I will be very foo")

    def __call__(self, *programs):
        print("Removing %s %s" % (self.jiha, programs,))
