# run for instructions

from agent import run_agent
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cv", required=True, help="Path to CV file (.txt or .pdf)")
    parser.add_argument("--job", required=True, help="Path to Job Description (.txt)")
    args = parser.parse_args()

    run_agent(args.cv, args.job)

if __name__ == "__main__":
    main()

