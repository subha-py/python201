import importlib.util

def check_module(module_name):
    """
    Checks if module can be imported without actually importing it
    :param module_name:
    :return:
    """
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module: {module} not found'.format(module=module_name))
        return None
    else:
        print('Module: {module} can be imported'.format(module=module_name))
        return module_spec
def import_module_from_spec(module_spec):
    """
    import module via the passed in module specification
    returns the newly imported module
    :param module_spec:
    :return:
    """
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module

if __name__ == '__main__':
    module_spec = check_module('fake_module')
    module_spec = check_module('collections')
    if module_spec:
        module = import_module_from_spec(module_spec)
        print(dir(module))