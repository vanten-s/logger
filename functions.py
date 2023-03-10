
import sys
import datetime

log_files = [ sys.stdout, open( "log.txt", "w" ) ]

def write_to_log_files( string ):
    now_string = datetime.datetime.now().time().strftime( "%H:%M:%S" )
    for log_file in log_files:
        log_file.write( f"[{now_string}] {string}\n" )

def log_error( string ):
    write_to_log_files( f"ERROR:   {string}" )

def log_info( string ):
    write_to_log_files( f"INFO:    {string}" )

def log_warning ( string ):
    write_to_log_files( f"WARNING: {string}" )

def log( func ):
    def logged_function( *args, **kwargs ):
        try:
            return_val = func( *args, **kwargs )

        except Exception as e:
            log_warning( f"Function {func.__name__} gave error {e}" )
            return_val = None

        log_info( f"Function {func.__name__} was called" )

        return return_val

    return logged_function




