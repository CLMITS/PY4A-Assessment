class num_convert :
    rm = [[1000000000,"[(M)]"],[500000000,"[(D)]"],[100000000,"[(C)]"],[50000000,"[(L)]"],[10000000,"[(X)]"],[5000000,"[(V)]"],[1000000,"(M)"],[500000,"(D)"],[100000,"(C)"],[50000,"(L)"],[10000,"(X)"],[5000,"(V)"],[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]
    w1 = [[100,"Hundred "],[90,"Ninety "],[80,"Eighty "],[70,"Seventy "],[60,"Sixty "],[50,"Fifty "],[40,"Forty "],[30,"Thirty "],[20,"Twenty "],
         [19,"Nineteen "],[18,"Eighteen "],[17,"Seventeen "],[16,"Sixteen "],[15,"Fifteen "],[14,"Fourteen "],[13,"Thirteen "],[12,"Twelve "],[11,"Eleven "],
         [10,"Ten "],[9,"Nine "],[8,"Eight "],[7,"Seven "],[6,"Six "],[5,"Five "],[4,"Four "],[3,"Three "],[2,"Two "],[1,"One "]]
    w2 = [[7,"Sextillion "],[6,"Quintillion "],[5,"Quadrillion "],[4,"Trillion "],[3,"Billion "],[2,"Million "],[1,"Thousand "],[0,""]] # Group of 3 Zero's
    ##_____________________________________________________________________________________________________________________________________________
    def __init__(self, n):
        self.n = int(str(n))        # Making it error free in the input of value
    ##_____________________________________________________________________________________________________________________________________________
    ## NUMBER TO ROMAN
    def roman(self):
        r, s = 0, ""                # Set variables
        sn = self.n                 # re-assign User's input value
        if len(str(sn))<11:         # Set Limitation for Roman Convertion
            for x,y in self.rm :        # For Looping the whole value in the list and separating the value of x and y... x = 1000000,500000,... y = "(M)","(D)",...
                r = sn//x               # is the input value divisible by 1000,900,500
                for z in range(0,r):    # range to r, execute once the value is divisible inside the list else r = 0 will not loop
                    s+=y                # s record the equivalent "Roman Numeral Value" which is from the "y"
                sn %= x                 # self.n records a new value of the remainder, and check if divisible inside the for loop x,.
        return s if s!="" else "Capacity for Roman Convertion is upto 10 Digits only"
    ##_____________________________________________________________________________________________________________________________________________
    ## NUMBER TO WORDS
    def words(self):
        lv,r,s,ss,v = 0,0,"","",""       # Set variables
        sn = list(str(self.n))           # Making input value into a list
        ln = len(sn)                     # Lenght of the string
        while ln>0:
            sa=int("".join(map(str,sn[-3:])))   # convert list value [-3:] into numbers, same as "".join([str(x) for x in sn[-3:]]) but map() is much faster in process
            s=""                                # reset "s" value, prevent word duplication
            for x,y in self.w1 :                # Looping the whole list self.w1
                r = sa//x                       # Getting the value which is divisible in the whole list self.w1
                if r==1:
                    if len(str(sa))==3 and str(sa)[0:1]=="1":       # Condition to insert word "One " on the third element
                        s+="One "
                    s+=y                                            # adding value into "s" which is our numerical words from "y"
                elif r>1 :
                    vv = [x for x in self.w1 if r == x[0]]          # checking the equivalent value of r inside our whole list self.w1
                    s += (vv[0][1] + y)                             # getting the equivalent numerical words from the whole list
                sa %= x                                             # Getting the remainder value, this will affect our divisor formula r = sa//x
            v = [x for x in self.w2 if lv == x[0]]                  # Loop for Wordings for Thousand, Millions, Billions, Trillions
            vs = v[0][1]                                            # Getting the numerical words
            ss=s+vs+ss                                              # Gathering all the numerical words
            del sn[-3:]                                             # Deleting the last 3 digit value because we are done processing
            ln = len(sn)                                            # checking again for the length of the strings
            lv+=1                                                   # This helps getting the exact Division for Thousand, Millions, Billions
        return ss                                                   # Return the complete numerical Words
inp=input("\nPlease input your numbers to be converted: ")
print("\nYour Number into Words is:\n",num_convert(inp).words())
print("\nYour Number into Roman Numeral is:\n",num_convert(inp).roman(),"\n")
