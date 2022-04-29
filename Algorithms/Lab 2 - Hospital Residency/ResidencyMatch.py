"""
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

Thor Madsen and John David Mohr

"""

import sys
import csv


class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        """
        Think of

            unmatched_hospitals
            residents_mappings
            hospitals_mappings
            matches

        as being instance data for your class.

        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        """

        # list of unmatched hospitals
        self.unmatched_hospitals = []

        # list of unmatched residents
        self.unmatched_residents = []

        # dictionaries representing preferences mappings

        self.residents_mappings = {}
        self.hospitals_mappings = {}

        # dictionary of matches where mapping is resident:hospital
        self.matches = {}

        # read in the preference files

        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''

        preferences = csv.reader(open(sys.argv[1], 'r'), delimiter=',')
        for row in preferences:
            resident = row[0].strip()

            # all residents are initially unmatched
            self.unmatched_residents.append(resident)

            # maps a resident to a list of preferences
            self.residents_mappings[resident] = [x.strip() for x in row[1:]]

            # initially have each resident as unmatched
            self.matches[resident] = None

        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''

        preferences = csv.reader(open(sys.argv[2], 'r'), delimiter=',')
        for row in preferences:
            hospital = row[0].strip()

            # all hospitals are initially unmatched
            self.unmatched_hospitals.append(hospital)

            # maps a hospital to a list of preferences
            self.hospitals_mappings[hospital] = [x.strip() for x in row[1:]]

    def reportMatches(self):
        print(self.matches)

    def runMatch(self):
        """
        Use the debugger or print statements to determine
        what the contents of the data structures are
        """
        hospitalPref = self.hospitals_mappings
        residentPref = self.residents_mappings
        matches = self.matches
        unmatchedResidents = self.unmatched_residents
        unmatchedHospitals = self.unmatched_hospitals

        prefValue = 0


        while(unmatchedHospitals is not None):

            if len(unmatchedHospitals) == 0:
                return

            # Go to next unmatched hospitals first choice
            curResident = hospitalPref[unmatchedHospitals[0]][prefValue]
            # Check if resident has accepted request
            if curResident in unmatchedResidents:

                # If resident has not accepted request, auto accept
                matches[unmatchedResidents.pop(unmatchedResidents.index(curResident))] = unmatchedHospitals.pop(0)

            # Else compare offers priority
            else:

                curResPriority = list(residentPref[curResident])

                # If the current offer is greater than the accepted offer accept the new offer
                if curResPriority.index(matches[curResident]) > curResPriority.index(unmatchedHospitals[0]):

                    # Appending residents current match and removing their new match
                    unmatchedHospitals.append(matches[curResident])
                    matches[curResident] = unmatchedHospitals.pop(0)
                    prefValue = 0
                # If the priority is lower move to hospitals next choice
                else:
                    prefValue += 1
        return



if __name__ == "__main__":

    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()

    # report the matches
    match.reportMatches()
