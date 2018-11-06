class state:
    def __init__(self,name):
        self.name = name
        self.nextstate = dict()
    def make_transit(self,command,change):
        self.nextstate[command] = change
    def next_state(self,command):

        if command in self.nextstate:
            return self.nextstate[command]
        else:
            return None


class Trans:
    def __init__(self):
        self.Transit = dict()
        self.construct_state()

    def construct_state(self):
        with open('Trans.in','rt') as f:
            for line in f.readlines():
                line = line.split('\n')[0]
                line = line.split("->")
                current = line[0].split(':')
                command = current[1].strip(' ')
                change = line[1].strip(' ')
                current = current[0]
                self.make_transit(current,command,change)
    def make_transit(self,current,command,change):

        if not current in self.Transit:
            self.Transit[current] = state(current)
        if not change in self.Transit:
            self.Transit[change] = state(change)
        self.Transit[current].make_transit(command, self.Transit[change])

    def move_state(self,current,command):
        nextstate = self.Transit[current].next_state(command)
        if nextstate == None:
            return "ERROR"
        return nextstate.name
trans = Trans()
def traverse_TCP_states(commands):

    state = 'CLOSED'
    for step in range(len(commands)):
        state = trans.move_state(state,commands[step])
        if state == 'ERROR':
            break
    return state
if __name__ == "__main__":

    assert traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]) =="CLOSE_WAIT"
    assert traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN","RCV_ACK"]) == "ESTABLISHED"
    assert traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"]) == "LAST_ACK"
    assert traverse_TCP_states(["APP_ACTIVE_OPEN"]) == "SYN_SENT"
    assert traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE"," APP_SEND"]) == "ERROR"
