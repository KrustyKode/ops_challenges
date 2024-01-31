def parse_log(file_path):
    warns, errs, thrs = [], [], []

    with open(file_path, 'r') as f:
        for line in f:
            if "WARNING" in line:
                warns.append(line)
            elif "ERROR" in line:
                errs.append(line)
            elif "THREAT" in line:
                thrs.append(line)

    return warns, errs, thrs

log_path = input("Enter log file path: ")

warnings, errors, threats = parse_log(log_path)

print("Warnings:\n", "".join(warnings))
print("\nErrors:\n", "".join(errors))
print("\nThreats:\n", "".join(threats))
