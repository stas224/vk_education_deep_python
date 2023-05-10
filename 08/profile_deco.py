import cProfile
import pstats
import io


def profile_deco(func):
    stats = cProfile.Profile()

    def inner(*args, **kwargs):
        stats.enable()
        result = func(*args, **kwargs)
        stats.disable()
        return result

    def print_stat():
        stm = io.StringIO()
        pstats.Stats(stats, stream=stm).sort_stats('cumulative').print_stats()
        print(stm.getvalue())

    inner.print_stat = print_stat
    return inner
