import badges
import templatefilters


# All badges awarded for spending a certain amount of time watching
# videos, total
class VideoTimeBadge(badges.Badge):

    def is_satisfied_by(self, *args, **kwargs):
        user_data = kwargs.get("user_data", None)
        if user_data is None:
            return False

        # Make sure they've watched at least X seconds
        return user_data.total_seconds_watched >= self.seconds_required

    def extended_description(self):
        return ("Bekijk %s van een video" %
                templatefilters.seconds_to_time_string(self.seconds_required))


@badges.active_badge
class ActOneSceneOneBadge(VideoTimeBadge):
    def __init__(self):
        VideoTimeBadge.__init__(self)
        self.seconds_required = 60 * 20
        self.description = "Plezierige Luisteraar"
        self.badge_category = badges.BadgeCategory.BRONZE
        self.points = 0
