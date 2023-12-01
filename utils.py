import time


def benchmark(repeat: int = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = []
            for _ in range(repeat):
                start_time = time.perf_counter_ns()
                result = func(*args, **kwargs)
                end_time = time.perf_counter_ns()
                elapsed_time = end_time - start_time
                times.append(elapsed_time)

            fastest_run = min(times)
            slowest_run = max(times)
            average_run = sum(times) / repeat

            print(f"Function '{func.__name__}' ran {repeat} times:")
            print(f"Fastest run: {fastest_run / 1_000_000:.5f} milliseconds")
            print(f"Slowest run: {slowest_run / 1_000_000:.5f} milliseconds")
            print(f"Average run: {average_run / 1_000_000:.5f} milliseconds")
            print(f"Solution: {result}")

        return wrapper

    return decorator
