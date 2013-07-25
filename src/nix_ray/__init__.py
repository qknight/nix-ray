"""xin - prototypical unified cli for nix
"""

import tpv.cli
import tpv.pkg_resources

from plumbum.cmd import ls, grep, wc, git
from tpv.ordereddict import OrderedDict


@tpv.pkg_resources.children_from_entry_points(
    entry_point_group="nix_ray.commands",
)
class NixRay(OrderedDict):
    """nix-ray

    Assistant for debugging the phases of a nix expression
    """
    verbose = tpv.cli.Flag(["v", "verbose"],
                           help="If given, I will be very talkative")

    def __call__(self, filename=None):
        if self.nested_command:
            return
        chain = ls['-la'] | grep['a'] | wc
        print(chain)
        print(chain())
        if self.verbose:
            print "Yadda " * 200

    @tpv.cli.switch(['f', 'foo'], int)
    def foo(self, bar):
        """foomagic
        """
        self.bar = bar
        print(bar)


app = tpv.cli.application(NixRay)()
