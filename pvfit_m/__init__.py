from pkg_resources import get_distribution, DistributionNotFound

import pvfit_m.api  # NOQA
import pvfit_m.data  # NOQA

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = None
