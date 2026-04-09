def format_size(size_in_kib: int) -> str:
    size_in_bytes = size_in_kib * 1024
    units = ["Б", "KiB", "MiB", "GiB", "TiB"]
    size = float(size_in_bytes)
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    if unit_index == 0:
        return f"{int(size)} {units[unit_index]}"
    return f"{size:.2f} {units[unit_index]}"


def get_summary_rss(ps_output_file_path: str) -> str:
    total_rss_kib = 0

    with open(ps_output_file_path, "r", encoding="utf-8") as output_file:
        lines = output_file.readlines()[1:]

    for line in lines:
        columns = line.split()
        if len(columns) > 5:
            try:
                rss_value = int(columns[5])
                total_rss_kib += rss_value
            except ValueError:
                continue

    return format_size(total_rss_kib)


if __name__ == '__main__':
    path: str = 'output_file.txt'
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)