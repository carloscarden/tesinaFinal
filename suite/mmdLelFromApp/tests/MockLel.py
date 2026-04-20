

from suite.mmdLelFromApp.models.lel.Categoria import Categoria
from suite.mmdLelFromApp.models.lel.LelMmd import LelMmd


class MockLel:

    def lelMockeadoHospital(self):
        
        lel1 = LelMmd(Categoria.VERBO,  'Administer', ''' Action performed by a doctor, that consists
in dispensing at a certain date and hour a dose of a drug to deal with some disease
of a patient in some seriousness in order to obtain some outcome.''')
        lel2 = LelMmd(Categoria.OBJETO, 'Dose', ''' Amount of a drug that is taken once, or
regularly over a period of time''')
        lel3 = LelMmd(Categoria.SUJETO, 'Patient', ''' Person who is ill or hurt, characterized by
gender and city.''' )
        lel4 = LelMmd(Categoria.OBJETO, 'Drug', ''' Medicine or other substance which has a
physiological effect when ingested or otherwise introduced into the body according to
its administration mode. The drug is also
characterized by an elimination mode''')
        lel5 = LelMmd(Categoria.SUJETO, 'Doctor', '''A person with a medical degree whose job
is to treat patients. The doctor works for a hospital and belongs to a Department''')
        lel6 = LelMmd(Categoria.SUJETO, 'Disease', ''' Illness affecting humans''')
        lel7 = LelMmd(Categoria.OBJETO, 'Outcome', ''' The result of a medical treatment''')
        lel8 = LelMmd(Categoria.OBJETO, 'Hour', ''' One of the 24 parts that a day is divided into''')
        lel9 = LelMmd(Categoria.OBJETO, 'Date', ''' A particular day of a month, in a particular year.''')
        lel10 = LelMmd(Categoria.OBJETO, 'Seriousness', '''Degree of risk of the life of a patient.''')
        lel11 = LelMmd(Categoria.OBJETO, 'Administration mode', ''''The way of giving a drug to somebody.''')
        lel12 = LelMmd(Categoria.OBJETO, 'Elimination mode', '''The process of removing or getting rid of the
drug completely''')
        lel13 = LelMmd(Categoria.OBJETO, 'Physiological effect', '''The expected result of administering a drug,
it belongs to one family.''')
        lel14 = LelMmd(Categoria.OBJETO, 'Family', '''  A group into which drugs that have similar characteristics are divided based on their
physiological effect''')
        lel15 = LelMmd(Categoria.SUJETO, 'Department', '''A section of a hospital.''')
        lel16 = LelMmd(Categoria.SUJETO, ' Hospital', ''' An institution in which the sick or injured
are given medical and surgical treatment. A hospital is located in a city.''')
        lel17 = LelMmd(Categoria.OBJETO, 'City', ''' A city belongs to a state.''')
        lel18 = LelMmd(Categoria.OBJETO, 'State', ''' A state belongs to a country.''')
        lel19 = LelMmd(Categoria.OBJETO, 'Country', ''' An area of land that has or used to have its
own government and laws.''')
        lel20 = LelMmd(Categoria.OBJETO, 'Month', ''' Any of the twelve periods of time into which
a year is divided.''')
        lel21 = LelMmd(Categoria.OBJETO, 'Year', '''The period from January 1 to December 31.''')
        lel22 = LelMmd(Categoria.OBJETO, 'Género', '''A range of identities with reference to social
and cultural differences.''')

        lels = [lel1, lel2, lel3, lel4, lel5, lel6, lel7, lel8, lel9, lel10, lel11, lel12, lel13, lel14, 
         lel15, lel16, lel17, lel18, lel19, lel20, lel21, lel22]

        return lels

    def lelMockeadoEmpresaAutos(self):

        lel1 = LelMmd(Categoria.VERBO.value,  'Sell a car', ''' Operation in which a client pays a price to obtain a car on a date in a store.''')

        lel2 = LelMmd(Categoria.OBJETO.value, 'Price', '''Amount of money that the client must pay for the car.''')

        lel3 = LelMmd(Categoria.OBJETO.value, 'Car', '''Four-wheel vehicle that may have different packages and can be used
either privately or commercially. A car has a model.''')


        lel4 = LelMmd(Categoria.OBJETO.value, 'Store', '''Facility where the purchase has been done. 
                   A store is located in one city.''')

        lel5 = LelMmd(Categoria.OBJETO.value, 'Date', '''The day when the purchase has been done.''')

        lel6 = LelMmd(Categoria.SUJETO.value, 'Client', '''A person or organization. 
                   A client may be described by gender and age''')

        lel7 = LelMmd(Categoria.OBJETO.value, 'Gender', '''Male or female.''')

        lel8 = LelMmd(Categoria.SUJETO.value, 'Model', '''A car design that belongs to one segment. 
                   A model has an engine capacity and is manufactured in one or more factories''' )

        lel9 = LelMmd(Categoria.OBJETO.value, 'Segment', '''A category that groups different car models according to 
                   their size, use, and capacity''')
        

        lel10 = LelMmd(Categoria.OBJETO.value, 'Factory', '''A place where cars are manufactured''')
        
        
        lel11 = LelMmd(Categoria.OBJETO.value, 'Engine capacity', 
                    '''The measurement of the total volume of the cylinders normally 
        expressed in cubic centimeters or litres, e.g., 1800 cc''')
        
        lel17 = LelMmd(Categoria.OBJETO.value, 'City', ''' A city belongs to a state.''')
        lel18 = LelMmd(Categoria.OBJETO.value, 'State', ''' A state belongs to a country.''')
        lel19 = LelMmd(Categoria.OBJETO.value, 'Country', ''' An area of land that has or used to have its
own government and laws.''')
        
        lels = [lel1,lel2,lel3,lel4,lel5, lel6, lel7, lel8, lel9, lel10, lel11, lel17, lel18, lel19]
        return lels 

