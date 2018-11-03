from IPython.core.magic import register_line_magic, register_cell_magic
import tempfile

def load_ipython_extension(ipython):
    pass

def load_ipython_extension(ipython):
    pass

@register_cell_magic
def pytest(line, cell):
    """
    Save previous cells with function definitions i
    and current cell as a test case
    """
    import pytest as pt
    import re
    #import pdb; pdb.set_trace()
    #previous_commands = globals().get('In', [])
    ip = get_ipython()
    previous_commands = ip.user_ns['_ih']
    current_command_number = len(previous_commands) - 1
    _, test_file = tempfile.mkstemp(text=True, suffix='.py', prefix='test_')
    
    # Save a filtered command history to file
    with open(test_file, 'w') as f:
        f.write(
            '\n'.join(
                c for c in previous_commands 
                if "get_ipython" not in c 
                and "@register" not in c
                and not re.match(r"^assert .*", c)
            )
        )
        f.write("\n{}\n".format(cell))
    
    # Run pytest on the file
    #args = line.split() + [f'-k {current_command_number}'] + [test_file]
    args = line.split()  + [test_file]
    print(args) 
    pt.main(args)
