"""xin - prototypical unified cli for nix
"""

import tpv.cli
import tpv.pkg_resources

from plumbum import FG
from plumbum.cmd import ls, grep, wc, git


class NixRay(tpv.cli.Command):
    """nix-ray

    Assistant for debugging the phases of a nix expression
    """
    VERSION = 0
    entry_point_group="nix_ray.commands"

    verbose = tpv.cli.Flag(["v", "verbose"],
                           help="If given, I will be very talkative")

    def __call__(self, filename=None):
        self.help()
        # chain = ls['-la'] | grep['a'] | wc
        # print(chain)
        # chain & FG
        # if self.verbose:
        #     print "Yadda " * 200

    @tpv.cli.switch(['f', 'foo'], int)
    def foo(self, bar):
        """foomagic
        """
        self.bar = bar
        print(bar)

app = NixRay.run
