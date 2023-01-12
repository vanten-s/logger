
import sys
import datetime

log_files = [ sys.stdout, open( "log.txt", "w" ) ]

def log( func ):
    def logged_function( *args, **kwargs ):
        return_val = func( *args, **kwargs )
        for log_file in log_files:
            now_string = datetime.datetime.now().time().strftime( "%H:%M:%S" )
            log_file.write( f"[{now_string}] called {func.__name__}" )

        return return_val

    return logged_function




