from cx_Freeze import setup, Executable
 
# Dependencies are automatically detected, but it might need
# fine tuning.
includefiles = ['constantes.py', 'character.py', 'game.py', 'maze.py']
excludes = ['Tkinter']
buildOptions = dict(packages = [], excludes = [])
 
base = 'Console'
 
executables = [
    Executable('D:/Programmation/Repos_Git/MacGyverOPCR/macgyver.py', base=base, targetName = 'mcgyver.exe')
]
 
setup(name='MacGyver',
      version = '1.0',
      description = 'Labyrinthe MacGyver',
      options = dict(build_exe = buildOptions),
      executables = executables)