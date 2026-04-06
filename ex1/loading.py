#!/usr/bin/env python3

import importlib
import sys


def error_message(dependencie: str) -> None:
    print(f"[ERROR] {dependencie} not installed")
    print("To install it:")
    print(f"  pip install {dependencie}")
    print(f"  poetry add {dependencie}\n")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    all_ok: bool = True
    print("Checking dependencies")
    try:
        pandas = importlib.import_module("pandas")
        print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
    except ImportError:
        error_message("pandas")
        all_ok = False

    try:
        numpy = importlib.import_module("numpy")
        print(f"[OK] numpy {numpy.__version__} - Numerical computation ready")
    except ImportError:
        error_message("numpy")
        all_ok = False

    try:
        matplotlib = importlib.import_module("matplotlib")
        plt = importlib.import_module("matplotlib.pyplot")
        print(
            f"[OK] matplotlib {matplotlib.__version__} - Visualization ready"
        )
    except ImportError:
        error_message("matplotlib")
        all_ok = False

    if not all_ok:
        print("\nPlease install missing dependencies and try again.")
        print(
            "Using pip:",
            "  python3 -m venv venv",
            "  source venv/bin/activate",
            "  pip install -r requirements.txt",
            "",
            "  Using Poetry:",
            "  poetry install",
            sep="\n"
        )
        sys.exit(1)

    file_name: str = "matrix_analysis.png"

    print("\nAnalyzing Matrix data...")

    #  1. Generate data with numpy
    data = numpy.random.randint(0, 1000, size=1000)

    #  2. Organize data with panda
    df = pandas.DataFrame(data, columns=["signal"])

    print("Processing 1000 data points")
    print("Generating visualization")

    #  3. Generate plot with matplotlib
    plt.plot(df["signal"])

    #  4. Save image
    plt.savefig(file_name)

    print("\nAnalysis complete!")
    print(f"Results saved to: {file_name}")


if __name__ == "__main__":
    main()
