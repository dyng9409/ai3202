class Model(object):

    def __init__(self, name, states):
        self.name = name
        self.states = states
        self.stateTable = {
                'start':0
                }
        pass
#initializing at 26 so we dont need to add 26 for smoothing
#26 is number of letters (dont count dummy because never returns)
#spaces seem to always be transcribed properly, and dont ever seem to be
#erroneously inserted
#if this is the case, output space for transition model is 1 extra (27)

#so, if spaces CAN be erroneously inserted (but not replaced):
#emission space: [a-z_] for all except '_' which is always '_'
#transition space: [a-z_] for all
#emission normalization: count + 27, except for '_'
#transition norm: count+27

#if not, then emission space is only [a-z], norm = count+26
#tran space: [a-z_] norm = count+27, except '_' space=[a-z], norm = count+26
states = list('abcdefghijklmnopqrstuvwxyz_')
stateCounts = {}
for elt in states:
    stateCounts[elt] = 26

stateCounts['dummy'] = 28


