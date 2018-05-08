# I like closures, though I don't usually feel like I need them.
#
# Quick example (arguments are not checked!).

def make_closure(s_arg):
    def m_closure(m_arg):
        # do something with s_arg, e.g.
        return s_arg * m_arg
    return m_closure

# Usage
func = make_closure(2)
print func(3)
