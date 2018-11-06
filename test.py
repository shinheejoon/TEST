import assign
import unittest

class assign_test(unittest.TestCase):



    def test_assign_case1(self):
        res = assign.traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"])
        self.assertEqual(res,"CLOSE_WAIT")
    def test_assign_case2(self):
        res = assign.traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN","RCV_ACK"])
        self.assertEqual(res,"ESTABLISHED")
    def test_assign_case3(self):
        res = assign.traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"])
        self.assertEqual(res,"LAST_ACK")
    def test_assign_case4(self):
        res = assign.traverse_TCP_states(["APP_ACTIVE_OPEN"])
        self.assertEqual(res,"SYN_SENT")
    def test_assign_case5(self):
        res = assign.traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE"," APP_SEND"])
        self.assertEqual(res,"ERROR")
    def test_assign_case6(self):
        res = assign.traverse_TCP_states(["xxxx"])
        self.assertEqual(res,"ERROR")




if __name__ == '__main__':
    unittest.main()
