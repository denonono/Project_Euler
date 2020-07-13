one_hundred = "onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefortyfortyonefortytwofortythreefortyfourfortyfivefortysixfortysevenfortyeightfortyninefiftyfiftyonefiftytwofiftythreefiftyfourfiftyfivefiftysixfiftysevenfiftyeightfiftyninesixtysixtyonesixtytwosixtythreesixtyfoursixtyfivesixtysixsixtysevensixtyeightsixtynineseventyseventyoneseventytwoseventythreeseventyfourseventyfiveseventysixseventysevenseventyeightseventynineeightyeightyoneeightytwoeightythreeeightyfoureightyfiveeightysixeightyseveneightyeighteightynineninetyninetyoneninetytwoninetythreeninetyfourninetyfiveninetysixninetysevenninetyeightninetynine"
hundred = "oneHundred"
twohundred = "TwoHundred"
threehundred = "ThreeHundred"
fourhundred = "FourHundred"
fivehundred = "FiveHundred"
sixhundred = "SixHundred"
sevenhundred = "SevenHundred"
eighthundred = "EightHundred"
ninehundred = "NineHundred"
onetousand = "OneThousand"
AND = "and"

Lenght_1_99 = len(one_hundred)
LenghtOfAdd = 99 * len(AND)

Lenght_100_199 = 100*len(hundred)+ Lenght_1_99 + LenghtOfAdd
Lenght_200_299 = 100*len(twohundred) + Lenght_1_99 + LenghtOfAdd
Lenght_300_399 = 100 * len(threehundred) + Lenght_1_99 + LenghtOfAdd
Lenght_400_499 = 100 * len(fourhundred) + Lenght_1_99 + LenghtOfAdd
Lenght_500_599 = 100 * len(fivehundred) + Lenght_1_99 + LenghtOfAdd
Lenght_600_699 = 100 * len(sixhundred) + Lenght_1_99 + LenghtOfAdd
Lenght_700_799 = 100 * len(sevenhundred) + Lenght_1_99 + LenghtOfAdd
Lenght_800_899 = 100 * len(eighthundred) + Lenght_1_99 + LenghtOfAdd
Lenght_900_999 = 100 * len(ninehundred) + Lenght_1_99 + LenghtOfAdd
Lenght_1000 = len(onetousand)

print(Lenght_1_99 + Lenght_100_199 + Lenght_200_299 + Lenght_300_399 + Lenght_400_499 + Lenght_500_599 + Lenght_600_699 + Lenght_700_799 + Lenght_800_899 + Lenght_900_999 + Lenght_1000)
