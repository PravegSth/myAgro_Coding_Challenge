# Calculate the total days when farmer gets the light
def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
    day = min(D1,D2,D3)
    power = 0

    while True:
        if D1 == day:
            K = K - R1
            D1 += 1

        if D2 == day:
            K = K - R2
            D2 += 1

        if D3 == day:
            K = K - R3
            D3 += 1

        if K >= 0:
            power += 1
        else:
            break

        day += 1

    return power


# For testing purpose
if __name__ == '__main__':
    days_of_power = get_days_of_power(1000, 3, 500, 10, 1500, 7, 21000)
    print("Total days of Power:", days_of_power)