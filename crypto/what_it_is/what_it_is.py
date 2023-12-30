def function01(parameter):
    if isinstance(parameter, str):
        parameter = parameter.encode("utf-8")
    return int.from_bytes(parameter, "big")

def function02(parameter1):
    if isinstance(parameter1, int):
        parameter2 = parameter1.bit_length()
    parameter3 = (parameter2 + 7) >> 3
    return parameter1.to_bytes(parameter3, "big")

def function03(parameter1, parameter2, parameter3): 
    parameter4 = 1
    while parameter2 > 0:
        if parameter2 % 2: 
            parameter4 = (parameter4 * parameter1) % parameter3
        parameter1 = parameter1 ** 2 % parameter3
        parameter2 //= 2
    return parameter4

def function04(parameter1, parameter2):
    parameter3, parameter4 = parameter1, parameter2
    parameter5, parameter6 = 1, 0
    while parameter4 > 0:
        parameter7 = parameter3 // parameter4
        parameter5, parameter6 = parameter6, parameter5 - parameter6*parameter7
        parameter3, parameter4 = parameter4, parameter3 - parameter4*parameter7
    while parameter5<0:
        parameter5 = parameter5 + parameter2
    return parameter5

def function05(parameter1, parameter2, parameter3):
    parameter4 = function03(parameter3, parameter1, parameter2)
    return (parameter1,parameter2,parameter4)

def function06(parameter1, parameter2, parameter3, parameter4):
    parameter5 = (parameter1-1)*(parameter2-1)
    parameter6 = function04(parameter3, parameter5)
    parameter7 = parameter1 * parameter2
    parameter8 = parameter6 % parameter5
    parameter9 = function03(parameter4, parameter8, parameter7)
    return (parameter1,parameter2,parameter6,function02(parameter9))


parameter1=xxx
parameter2=xxx
parameter3=function01('flag{xxx}')
print(function05(parameter1, parameter2, parameter3))

#(1836324694929784476835108099082056174623084578715252194723684441811276964517815670916307672124429913298496109300736190015819472793792279373184805908421456486694085063067063116357217287305124179013788469283723172636904638581802402597710348100997359577835237064629686970148402423333202856291219631775949382153, 136526881908113280139666110635735107693088803876031066751555428677304548687550866069207624840461524764086836159397112467161084272104167993059454092316535836685482393830468346596449981820239359935619643450339323251265651114969689690328974794077702063811237319607989773131915084856622897317444230904967018499483, 94108329054248869854965522726100119302473989317007422449777707711419541735157816488729349838573684573669553406173953572857360948443836947505984378585736170828054577274980983062145116243706001321267875138881608815196472181187295654595270495453318008011064151019684272317170183568255501087494831553126973871908)