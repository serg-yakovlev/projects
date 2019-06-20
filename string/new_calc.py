#import calculator2 as c2


#print(arg1, arg2, action)
#print(dir(calculator2))
#print(__name__)
#print(c2.__name__)
# m_arg1, m_arg2, m_action = c2.inpData()
# try:
#     m_arg1, m_arg2, m_action = c2.checkData(m_arg1, m_arg2, m_action)
# except CalcException as e:
#     print(e)
#     exit(1)
# c2.outputData(m_arg1, m_arg2, m_action)

from calculator2 import inpData

a, b, c = inpData()
