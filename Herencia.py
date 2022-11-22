class Persona():
  def __init__(self):
    self.__Nombre=""
    self.__Apellido=""
    self.__Edad=0

  def GetNombre(self):
    return self.__Nombre

  def SetNombre(self, nombre):
    self.__Nombre=nombre
  
  def GetApellido(self):
    return self.__Apellido

  def SetApellido(self, apellido):
    self.__Apellido = apellido

  def GetEdad(self):
    return self.__Edad

  def SetEdad(self, edad):
    self.__Edad=edad

  
class Alumno(Persona):
  def __init__(self):
    self.__Curso=""
    self.__Asignatura=""

  def GetCurso(self):
    return self.__Curso

  def SetCurso(self, curso):
    self.__Curso= curso

  def GetAsignatura(self):
    return self.__Asignatura
  
  def SetAsignatura(self, asignatura):
    self.__Asignatura = asignatura 

  def MostrarAlumno(self):
    print("alumno: ")
    print("\tNombre:",self.GetNombre())
    print("\tApellido:",self.GetApellido())
    print("\tEdad:",self.GetEdad())
    print("\tCurso:",self.__Curso)
    print("\tMatricula:",self.__Asignatura)
    print(" ")
    

alumno=Alumno()
alumno.SetNombre("Jorge")
alumno.SetApellido("Henao")
alumno.SetEdad("30")
alumno.SetCurso("bachillerato")
alumno.SetAsignatura(["matematicas","Tecnologia"])
alumno.MostrarAlumno()
