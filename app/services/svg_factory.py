from app.constant import Constant
from app.services.rating_badge_generator import RatingBadgeGenerator


def make_svg_generator(generator_type: str):
    """Returns the appropriate generator class."""
    generators = {
        Constant.RATING_BADGE: RatingBadgeGenerator,
    }
    return generators[generator_type]


class SVGFactory:
    """Factory class for getting generating SVG."""

    @classmethod
    def get_svg_generator(cls, svg_type):
        """Returns the appropriate question handler."""
        return make_svg_generator(svg_type)
