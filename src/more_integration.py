from scipy.special import roots_genlaguerre

# play with Laguerre integration
def genLaguerreInt():
    # extract the coefficients
    n = 3
    alpha = 1/2
    x,w = roots_genlaguerre(n, alpha, False)

    # print the result
    print("Sample points: ")
    print(x)
    print("Weights: ")
    print(w)

    # print the result
    print("")
    print("Access a single point")
    print("Sample point: ")
    print(x[0])
    print("Weights: ")
    print(w[0])

# The main function
def main():
    genLaguerreInt()

if __name__ == "__main__":
    main()
