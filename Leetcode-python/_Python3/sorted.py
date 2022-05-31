def test(intervals):
    si = sorted(intervals, key=lambda x:x[0] )
    print(si)

if __name__ == "__main__":

    intervals = [
        [1, 2],
        [3, 5],
        [12, 7],
        [10, 9],
        [6, 8]
    ]

    test(intervals)