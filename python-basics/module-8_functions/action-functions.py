def write_log(message):
    with open(r'C:\Users\gianc\Downloads\app.log', 'a') as file:
        file.write(message + '\n')
# write_log('App started.')
# write_log('User logged in.')
write_log('App terminated.')