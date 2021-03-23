import types


def udir(o):
    """
    Uber dir
    Returns only visible attributes of object
    """
    prop = dir(o)
    prop = [i for i in prop if not i.startswith('_')]
    
    return prop

def var_info(obj, max_len=200):
    """Returns type-info about the attributes of an object"""
    ret = [] 
    
    attributes = udir(obj)
    for name in attributes:
        val = getattr(obj,name)
        if isinstance(val,str):
            str_val = val[:max_len].replace(r'\n',r'\n')
            ret.append(
                f'{name}: str -> {str_val}')
            continue
        if isinstance(val,bool):
            ret.append(f'{name}: bool -> {val}')
            continue
        if isinstance(val,int):
            ret.append(f'{name}: int -> {val}')
            continue
        if isinstance(val, types.BuiltinFunctionType):
            ret.append(f'{name}()')
            continue
        """
        Todo: figure out these
        types.BuiltinMethodType
        types.MethodType
        types.FunctionType
        """
        ret.append(f'{name} -> {type(val)}')
    
    return ret

def _exclude_non_capitalized(lst):
    """Returns all list elements that are capitalized"""
    ret = []
    for l in lst:
        if l[0].isupper():
            ret.append(l)
    return ret
    
def _find_type_match(obj):
    """Returns all types that the object matches"""
    ret = []
    all_types_names = udir(types)
    all_types_names = _exclude_non_capitalized(all_types_names)
    for t in all_types_names:
        type_obj = getattr(types,t)
        if isinstance(obj, type_obj):
            ret.append(type_obj)
    return ret
        


        

