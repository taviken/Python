def dict_to_html_manual(data_dict):
    html_output = "<ul>\n"
    for key, value in data_dict.items():
        html_output += f"  <li>**{key}**: {value}</li>\n"
    html_output += "</ul>"
    return html_output


def dict_to_html_list(d):
    """
    Recursively converts a nested dictionary to an HTML unordered list.
    """
    html = "<ul>"
    for key, value in d.items():
        html += f"<li><strong>{key}:</strong> "
        if isinstance(value, dict):
            # If the value is a dictionary, recurse
            html += dict_to_html_list(value)
        else:
            # Otherwise, just add the value
            html += str(value)
        html += "</li>"
    html += "</ul>"
    return html


def generate_html_table(nested_dict):
    html = "<html><table border='1'>\n"
    # Create table headers (assuming all inner dicts have the same keys)
    headers = list(next(iter(nested_dict.values())).keys())
    html += (
        "  <tr><th>Child ID</th>"
        + "".join(f"<th>{h}</th>" for h in headers)
        + "</tr>\n"
    )

    # Create table rows
    for outer_key, inner_dict in nested_dict.items():
        html += f"  <tr><td>{outer_key}</td>"
        for value in inner_dict.values():
            html += f"<td>{value}</td>"
        html += "</tr>\n"

    html += "</table></html>"
    return html
