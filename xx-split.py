import os
import re

def _is_function_start(line):
    function_name = re.match(r"^ {2}(\w+):", line)
    if function_name:
        return function_name.group(1)

def _is_function_comment(line):
    return re.match(r"^ {2}#.*", line)

def _is_function_owner(line):
  function_owner = re.match(r"^ {4}owner: (.*)", line)
  if function_owner:
    return function_owner.group(1)


def _split_functions(lines):
    current_function = None
    function_owner = None
    content = []
    comments = []

    for line in lines:
        # Comments are "buffered" until we hit a function start
        if _is_function_comment(line):
            comments.append(line)
            continue

        # Start of new function
        if _is_function_start(line):
            if current_function and content:
                # hand back previous function content
                yield current_function, function_owner, content
                content = []

            current_function = _is_function_start(line)

            # prepend any pending comments
            if comments:
                content.extend(comments)
                comments = []
        
        if _is_function_owner(line):
          function_owner = _is_function_owner(line)

        # Collect lines for the current function
        if current_function:
            content.append(line)

    # Yield last function
    if current_function and content:
        yield current_function, function_owner, content


def main() -> None:
    with open("data/functions.yaml", "r") as file:
        lines = file.readlines()

    for function_name, function_owner, content in _split_functions(lines):
        out_file = f"{function_name}.yaml"
        with open(out_file, "w") as f:
            # include the top-level "function:" header for valid YAML
            f.write("function:\n")
            f.writelines(content)
        print(f"Created {out_file} owned by {function_owner}.")


if __name__ == "__main__":
    main()
