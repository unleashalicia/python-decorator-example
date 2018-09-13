def decorator_function( original_function ):
  def wrapper_function():
    return original_function()
  return wrapper_function

def do_thing():
  print('did thing')

decorated_do_thing = decorator_function( do_thing )

decorated_do_thing()
