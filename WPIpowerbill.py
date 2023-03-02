#WPI Power bill estimation 
#2/10/2023

#in kw-hr/day in 2001
sep01=57000
oct01=61000
dec01=63000

#Power rates in 2022 [cent/kwh]
pr=0.141

#average power rate increase per year
apri=0.003

#years since 2001:
time=2023-2001

#compounding intrest moment [estimating that a month is 30 days]
c_kw_sep01=(sep01*((1+apri)**time)-sep01)*pr*30
c_kw_oct01=(oct01*((1+apri)**time)-oct01)*pr*30
c_kw_dec01=(dec01*((1+apri)**time)-dec01)*pr*30

total_bill=c_kw_sep01*12

print("Epic WPI Electric Bill Estimator")
print("Cost Est. Month of Sep:",c_kw_sep01)
print("Cost Est. Month of Oct:",c_kw_oct01)
print("Cost Est. Month of Dec:",c_kw_dec01)
print("Estimated Yearly Cost:",total_bill)