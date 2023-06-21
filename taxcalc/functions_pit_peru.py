"""
pitaxcalc functions that calculate personal income tax liability.
"""
# CODING-STYLE CHECKS:
# pycodestyle functions.py
# pylint --disable=locally-disabled functions.py

import math
import copy
import numpy as np
from taxcalc.decorators import iterate_jit
'''
------------------------------------------
 FIRST CATEGORY INCOME 
------------------------------------------
'''
"Calculation for income from lease of goods"
@iterate_jit(nopython=True)
def income_lease(inc_lease, income_lease):
    income_lease = inc_lease
    return income_lease

"Calculation for income from free use of property"
@iterate_jit(nopython=True)
def income_property(value_prop_freeuse, rate_inc_prop_freeuse, income_prop_freeuse):
    income_prop_freeuse = value_prop_freeuse * rate_inc_prop_freeuse
    return income_prop_freeuse

"Calculation of deduction from lease income"
@iterate_jit(nopython=True)
def deduction_inc_lease(income_lease, rate_ded_lease, ded_inc_lease):
    ded_inc_lease = income_lease * rate_ded_lease
    return ded_inc_lease

"Calculation of deduction from free use property"
@iterate_jit(nopython=True)
def deduction_inc_property(income_prop_freeuse, rate_ded_prop_freeuse, ded_inc_prop_freeuse):
    ded_inc_prop_freeuse = income_prop_freeuse * rate_ded_prop_freeuse
    return ded_inc_prop_freeuse

"Calculation of net taxable first category income"
@iterate_jit(nopython=True)
def net_income_cat1(income_lease, income_prop_freeuse, ded_inc_lease, ded_inc_prop_freeuse):
    net_inc_cat1 = (income_lease - ded_inc_lease) + (income_prop_freeuse - ded_inc_prop_freeuse)
    return net_inc_cat1


'''
------------------------------------------
 SECOND CATEGORY INCOME 
------------------------------------------
'''

"Calculation of capital gains from stocks"
@iterate_jit(nopython=True)
def income_stocks_domestic(inc_stocks_dom, income_stocks_dom):
    income_stocks_dom = inc_stocks_dom
    return income_stocks_dom

"Calculation of capital gains from foreign market stocks"  
@iterate_jit(nopython=True)
def income_stocks_foreign(inc_stocks_foreign, income_stocks_foreign):
    income_stocks_foreign = inc_stocks_foreign
    return income_stocks_foreign

"Calculation of property sale income"  
@iterate_jit(nopython=True)
def income_property_sale(inc_gross_prop_sale, income_prop_sale):
    income_prop_sale = inc_gross_prop_sale
    return income_prop_sale

"Calculation of other capital sale income"  
@iterate_jit(nopython=True)
def income_capital_sale(inc_cap_other, income_cap_other):
    income_cap_other = inc_cap_other
    return income_cap_other

"Calculation of dividend income"  
@iterate_jit(nopython=True)
def income_dividend(inc_div, income_div):
    income_div = inc_div
    return income_div

"Calculation of interest income"  
@iterate_jit(nopython=True)
def income_interest(inc_interest, income_interest):
    income_interest = inc_interest
    return income_interest

"Calculation of deduction from capital gains from stocks"
@iterate_jit(nopython=True)
def deduction_stocks_domestic(income_stocks_dom, rate_ded_stocks_dom, ded_stocks_dom):
    ded_stocks_dom = income_stocks_dom * rate_ded_stocks_dom
    return ded_stocks_dom

"Calculation of deduction from capital gains from foreign market stocks"  
@iterate_jit(nopython=True)
def deduction_stocks_foreign(income_stocks_foreign, rate_ded_stocks_foreign, ded_stocks_foreign):
    ded_stocks_foreign = income_stocks_foreign * rate_ded_stocks_foreign
    return ded_stocks_foreign

"Calculation of deduction from property sale income"  
@iterate_jit(nopython=True)
def deduction_property_sale(income_prop_sale, rate_ded_prop_sale, ded_prop_sale):
    ded_prop_sale = income_prop_sale * rate_ded_prop_sale
    return ded_prop_sale

"Calculation of deduction from other capital sale income"  
@iterate_jit(nopython=True)
def deduction_capital_sale(income_cap_other, rate_ded_cap_other, ded_cap_other):
    ded_cap_other = income_cap_other * rate_ded_cap_other
    return ded_cap_other

"Calculation of deduction from dividend income"  
@iterate_jit(nopython=True)
def deduction_dividend(income_div, rate_ded_div, ded_div):
    ded_div = income_div * rate_ded_div
    return ded_div

"Calculation of deduction from interest income"  
@iterate_jit(nopython=True)
def deduction_interest(income_interest, rate_ded_interest, ded_interest):
    ded_interest = income_interest * rate_ded_interest
    return ded_interest

"Calculation of net taxable second category non-dividend income"
@iterate_jit(nopython=True)
def net_income_nondiv_cat2(income_stocks_dom, income_stocks_foreign, income_prop_sale, income_cap_other,income_interest,
                    ded_stocks_dom, ded_stocks_foreign, ded_prop_sale, ded_cap_other, ded_interest, net_inc_nondiv_cat2):
    net_inc_nondiv_cat2 =  (income_stocks_dom - ded_stocks_dom) + (income_stocks_foreign - ded_stocks_foreign) + \
                           (income_prop_sale - ded_prop_sale) + (income_cap_other - ded_cap_other) + (income_interest - ded_interest)
    return net_inc_nondiv_cat2

"Calculation of net taxable second category dividend income"
@iterate_jit(nopython=True)
def net_income_div_cat2(income_div, ded_div, net_inc_div_cat2):
    net_inc_div_cat2 = (income_div - ded_div)
    return net_inc_div_cat2

'''
-------------------------------------------------------------------
 NET TAXABLE FIRST AND SECOND CATEGORY INCOME - CAPITAL INCOME
-------------------------------------------------------------------
'''

"Calculation for tax base from capital income from first and second category"
@iterate_jit(nopython=True)
def tti_capital(net_inc_cat1, net_inc_nondiv_cat2, net_inc_div_cat2, tti_c):
    tti_c = net_inc_cat1 + net_inc_nondiv_cat2 + net_inc_div_cat2
    return tti_c

'''
------------------------------------------
 FOURTH CATEGORY INCOME 
------------------------------------------
'''


"Calculation of income from independent work"
@iterate_jit(nopython=True)
def income_indwork(inc_ind_work, income_ind_work):
    income_ind_work = inc_ind_work
    return income_ind_work

"Calculation of income from per diem by Directors"
@iterate_jit(nopython=True)
def income_director(inc_board_dir, income_board_dir):
    income_board_dir = inc_board_dir
    return income_board_dir


"Calculation of deduction - income from independent work"
@iterate_jit(nopython=True)
def deduction_indwork(income_ind_work, rate_ded_ind_work, ded_ind_work):
    ded_ind_work = income_ind_work * rate_ded_ind_work
    return ded_ind_work

"Calculation of deduction - income from per diem by Directors"
@iterate_jit(nopython=True)
def deduction_director(income_board_dir, rate_ded_board_dir, ded_board_dir):
    ded_board_dir = income_board_dir * rate_ded_board_dir
    return ded_board_dir

"Calculation of net fourth category income"
@iterate_jit(nopython=True)
def net_income_cat4(income_ind_work, income_board_dir, ded_ind_work, ded_board_dir, net_inc_cat4):
    net_inc_cat4 = (income_ind_work - ded_ind_work) + (income_board_dir - ded_board_dir)
    return net_inc_cat4


'''
------------------------------------------
 FIFTH CATEGORY INCOME 
------------------------------------------
'''

"Calculation of income from salaries"
@iterate_jit(nopython=True)
def income_salaries(inc_sal, income_sal):
    income_sal = inc_sal
    return income_sal


"Calculation of standard deduction - income from salaries"
@iterate_jit(nopython=True)
def deduction_salaries(income_sal, rate_ded_sal, ded_sal):
    ded_sal = income_sal * rate_ded_sal
    return ded_sal

"Calculation of net fifth category income"
@iterate_jit(nopython=True)
def net_income_cat5(income_sal, ded_sal, net_inc_cat5):
    net_inc_cat5 = income_sal - ded_sal
    return net_inc_cat5

'''
------------------------------------------
 FOREIGN SOURCE INCOME 
------------------------------------------
'''

"Calculation of income from foreign sources"
@iterate_jit(nopython=True)
def income_foreign(inc_foreign_net, net_inc_foreign):
    net_inc_foreign = inc_foreign_net
    return  net_inc_foreign


'''
------------------------------------------
 DEDUCTION - FOURTH, FIFTH CATEGORY INCOME 
------------------------------------------
'''

"Calculation of standard deduction - income from labor"
@iterate_jit(nopython=True)
def deduction_std_labor(net_inc_cat4, net_inc_cat5, peru_tax_unit, rate_ded_std, ded_std):
    net_inc_cat4_5 = net_inc_cat4 + net_inc_cat5
    max_ded_std = peru_tax_unit * rate_ded_std
    ded_std = min(net_inc_cat4_5, max_ded_std)
    return ded_std

"Calculation of additional deduction - income from labor"
@iterate_jit(nopython=True)
def deduction_addl_labor(peru_tax_unit, ded_3UIT, rate_ded_addl, ded_addl):
    max_ded_addl = peru_tax_unit * rate_ded_addl
    ded_addl = min(ded_3UIT, max_ded_addl)
    return ded_addl


'''
------------------------------------------
 DEDUCTION - FINANCIAL TRANSACTION TAX 
------------------------------------------
'''
"Calculation of deduction - financial trasanction tax"
@iterate_jit(nopython=True)
def deduction_fin_transtax(ded_fin_transtax, ded_fintax):
    ded_fintax = ded_fin_transtax
    return ded_fintax

'''
------------------------------------------
 DEDUCTION - DONATIONS FOR CHARITABLE PURPOSES
------------------------------------------
'''
"Calculation of deduction - charitable donations"
@iterate_jit(nopython=True)
def deduction_donations(net_inc_cat4, net_inc_cat5, net_inc_foreign, ded_charitable, rate_ded_donation, max_ded_char, ded_donation):
    max_ded_donation = max_ded_char * (net_inc_cat4 + net_inc_cat5 + net_inc_foreign)
    ded_donation = min(ded_charitable, max_ded_donation)*rate_ded_donation
    return ded_donation


'''
------------------------------------------
 NET CATEGORY 4 & 5 AND FOREIGN SOURCE INCOME 
------------------------------------------
'''

"Calculation of net income from labor and foreign sources"
@iterate_jit(nopython=True)
def income_labor_all(net_inc_cat4, net_inc_cat5, tti_c, switch_flat_sch, net_inc_foreign, ded_std, ded_addl, ded_fintax, ded_donation, tti_w):
    tti_w = (net_inc_cat4 + net_inc_cat5) + tti_c*switch_flat_sch
    tti_w = tti_w - ded_std - ded_addl - ded_fintax - ded_donation + net_inc_foreign
    return tti_w


'''
-----------------------------------------------------------------------------
 CALCULATION OF NET TAXABLE INCOME FROM ALL SOURCES 
-----------------------------------------------------------------------------
'''

@iterate_jit(nopython=True)
def net_taxable_income(tti_w, tti_c, tti):
    """
    Compute sum of net income from all categories of income.
    """
    tti = tti_w + tti_c
    return tti

'''
-----------------------------------------------------------------------------
 CALCULATION OF TAX LIABILITY - LABOR INCOME AT PROGRESSIVE RATE SCHEDULE
-----------------------------------------------------------------------------
'''


"Calculation for incorporating behavior - uses tax elasticity of total tax from labour income "
"Elasticity = % Change in income / % Change in tax rate "

@iterate_jit(nopython=True)
def cal_tti_labor(rate1, rate2, rate3, rate4, rate5, tbrk1, tbrk2, tbrk3, tbrk4, tbrk5,
                         rate1_curr_law, rate2_curr_law, rate3_curr_law, rate4_curr_law, rate5_curr_law, 
                         tbrk1_curr_law, tbrk2_curr_law, tbrk3_curr_law, tbrk4_curr_law, tbrk5_curr_law,
                         elasticity_pit_taxable_income_threshold, elasticity_pit_taxable_income_value, 
                         tti_w, tti_w_behavior):
    """
    Compute taxable total income after adjusting for behavior.
    """  
    
    elasticity_taxable_income_threshold0 = elasticity_pit_taxable_income_threshold[0]
    elasticity_taxable_income_threshold1 = elasticity_pit_taxable_income_threshold[1]
    #elasticity_taxable_income_threshold2 = elasticity_pit_taxable_income_threshold[2]
    elasticity_taxable_income_value0=elasticity_pit_taxable_income_value[0]
    elasticity_taxable_income_value1=elasticity_pit_taxable_income_value[1]
    elasticity_taxable_income_value2=elasticity_pit_taxable_income_value[2]
    if tti_w <=0:
        elasticity=0
    elif tti_w < elasticity_taxable_income_threshold0:
        elasticity=elasticity_taxable_income_value0
    elif tti_w < elasticity_taxable_income_threshold1:
        elasticity=elasticity_taxable_income_value1
    else:
        elasticity=elasticity_taxable_income_value2

    if tti_w < 0:
        marg_rate=0
    elif tti_w <= tbrk1:
        marg_rate=rate1
    elif tti_w <= tbrk2:
        marg_rate=rate2
    elif tti_w <= tbrk3:
        marg_rate=rate3
    elif tti_w <= tbrk4:
        marg_rate=rate4
    else:        
        marg_rate=rate5

    if tti_w < 0:
        marg_rate_curr_law=0
    elif tti_w <= tbrk1_curr_law:
        marg_rate_curr_law=rate1_curr_law
    elif tti_w <= tbrk2_curr_law:
        marg_rate_curr_law=rate2_curr_law
    elif tti_w <= tbrk3_curr_law:
        marg_rate_curr_law=rate3_curr_law
    elif tti_w <= tbrk4_curr_law:
        marg_rate_curr_law=rate4_curr_law
    else:        
        marg_rate_curr_law=rate5_curr_law
    
    frac_change_net_of_pit_rate = ((1-marg_rate)-(1-marg_rate_curr_law))/(1-marg_rate_curr_law)
    frac_change_tti_w = elasticity*(frac_change_net_of_pit_rate)  
    tti_w_behavior = tti_w*(1+frac_change_tti_w)
    return tti_w_behavior
    
"Calculation for PIT from labor income incorporating behaviour"
@iterate_jit(nopython=True)
def cal_pit_w(tti_w_behavior, peru_tax_unit, rate1, rate2, rate3, rate4, rate5, rate6, tbrk1, tbrk2, tbrk3, tbrk4, tbrk5, tbrk6, pit_w):
    """
    Compute tax liability given the progressive tax rate schedule specified
    by the (marginal tax) rate* and (upper tax bracket) brk* parameters and
    given taxable income (taxinc)
    """
    taxinc = tti_w_behavior/peru_tax_unit  
    
    pit_w = (rate1 * min(taxinc, tbrk1) +
                    rate2 * min(tbrk2 - tbrk1, max(0., taxinc - tbrk1)) +
                    rate3 * min(tbrk3 - tbrk2, max(0., taxinc - tbrk2)) +
                    rate4 * min(tbrk4 - tbrk3, max(0., taxinc - tbrk3)) +
                    rate5 * min(tbrk5 - tbrk4, max(0., taxinc - tbrk4)) +
                    rate6 * max(0., taxinc - tbrk5))
    pit_w *= peru_tax_unit    
    return pit_w


'''
-----------------------------------------------------------------------------
 CALCULATION OF TAX LIABILITY - CAPITAL INCOME 
-----------------------------------------------------------------------------
'''


"Calculation behavior"
@iterate_jit(nopython=True)
def cal_tti_capital(rate_tax_cat1, rate_tax_cat1_curr_law,
                    rate_tax_cat2, rate_tax_cat2_curr_law,
                    rate_tax_div, rate_tax_div_curr_law,
                    elasticity_pit_capital_income_threshold,
                    elasticity_pit_capital_income_value,
                    tti_c, net_inc_cat1, net_inc_nondiv_cat2, net_inc_div_cat2, 
                    tti_cat1_behavior, tti_cat2_behavior, tti_div_behavior):
    """
    Compute capital income taking income elasticity into account
    """
    tti_cat1 = net_inc_cat1 
    tti_cat2 = net_inc_nondiv_cat2
    tti_div = net_inc_div_cat2
    elasticity_pit_capital_income_threshold0 = elasticity_pit_capital_income_threshold[0]
    elasticity_pit_capital_income_threshold1 = elasticity_pit_capital_income_threshold[1]
    
    elasticity_pit_capital_income_value0=elasticity_pit_capital_income_value[0]
    elasticity_pit_capital_income_value1=elasticity_pit_capital_income_value[1]
    elasticity_pit_capital_income_value2=elasticity_pit_capital_income_value[2]
    
    if tti_c <= 0:
        elasticity=0
    elif tti_c <= elasticity_pit_capital_income_threshold0:
        elasticity=elasticity_pit_capital_income_value0
    elif tti_c <= elasticity_pit_capital_income_threshold1:
        elasticity=elasticity_pit_capital_income_value1
    else:
        elasticity=elasticity_pit_capital_income_value2
    
    frac_change_net_of_pit_capital_income_rate_cat1 = ((1-rate_tax_cat1)-(1-rate_tax_cat1_curr_law))/(1-rate_tax_cat1_curr_law)
    frac_change_tti_cat1 = elasticity*(frac_change_net_of_pit_capital_income_rate_cat1)
    tti_cat1_behavior = tti_cat1*(1+frac_change_tti_cat1)
    
    frac_change_net_of_pit_capital_income_rate_cat2 = ((1-rate_tax_cat2)-(1-rate_tax_cat2_curr_law))/(1-rate_tax_cat2_curr_law)
    frac_change_tti_cat2 = elasticity*(frac_change_net_of_pit_capital_income_rate_cat2)
    tti_cat2_behavior = tti_cat2*(1+frac_change_tti_cat2)
    
    frac_change_net_of_pit_capital_income_rate_div = ((1-rate_tax_div)-(1-rate_tax_div_curr_law))/(1-rate_tax_div_curr_law)
    frac_change_tti_div = elasticity*(frac_change_net_of_pit_capital_income_rate_div)
    tti_div_behavior = tti_div*(1+frac_change_tti_div)
    
    return tti_cat1_behavior, tti_cat2_behavior, tti_div_behavior


"Calculation for PIT from capital"
@iterate_jit(nopython=True)
def cal_pit_c(rate_tax_cat1, rate_tax_cat2, rate_tax_div, tti_cat1_behavior, tti_cat2_behavior, tti_div_behavior, switch_flat_sch, pit_c):
    pit_c = ((tti_cat1_behavior*rate_tax_cat1) + (tti_cat2_behavior*rate_tax_cat2) + (tti_div_behavior*rate_tax_div))*(1 - switch_flat_sch)
    return pit_c


'''
-----------------------------------------------------------------------------
 CALCULATION OF AGGREGATE TAX LIABILITY - TAX ON LABOR AND CAPITAL INCOME 
-----------------------------------------------------------------------------
'''


@iterate_jit(nopython=True)
def cal_total_pit(pit_w, pit_c, pitax):
    """
    Compute PIT.
    """
    pitax = pit_w + pit_c
    return pitax

'''
-----------------------------------------------------------------------------
 CALCULATION OF NET TAX LIABILITY - AFTER FOREIGN TAX CREDIT
-----------------------------------------------------------------------------
'''

@iterate_jit(nopython=True)
def cal_net_pit(pitax, foreign_tax_credit, pitax_net):
    """
    Compute PIT.
    """
    pitax_net = pitax - foreign_tax_credit
    return pitax_net

'''
-----------------------------------------------------------------------------
 CALCULATION OF GROSS TOTAL INCOME FROM ALL SOURCES 
-----------------------------------------------------------------------------
'''

@iterate_jit(nopython=True)
def gross_total_income(income_lease, income_prop_freeuse, income_stocks_dom, income_stocks_foreign, 
                       income_prop_sale, income_cap_other, income_div, income_ind_work, income_board_dir, 
                       income_sal, net_inc_foreign, total_gross_income):
    """
    Compute sum of net income from all categories of income.
    """
    total_gross_income = income_lease + income_prop_freeuse + income_stocks_dom + income_stocks_foreign + \
                        income_prop_sale + income_cap_other + income_div + income_ind_work + \
                        income_board_dir + income_sal + net_inc_foreign
    return (total_gross_income)