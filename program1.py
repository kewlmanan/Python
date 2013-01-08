#! /usr/bin/python

import os,sys,re

if __name__=="__main__":

    try:
        fp=open("grocery","r")
    except:
        print "Grocery list log could not be opened"
        sys.exit(-1)
    
    # Get rid of trailing new line characters 
    lines=[]
    for line in fp.readlines():
        lines.append(line.rstrip('\n'))
    
    # Get the unique customers first
    res=os.popen("awk -F\| '{print$1}' grocery | sort | uniq")
    customer_list=res.readlines()

    # Parse the lines and get necessary info
    total_revenue={}
    print "\n------------------------- REPORT 1 ---------------------------"
    for customer in customer_list:
        print "\nSpending per category for %s" %customer
        category_hash={}
        for line in lines:
            tmp_list=line.split('|')
            # Populate the total revenue
            if tmp_list[0] != customer.rstrip('\n') :
                continue
            if tmp_list[0] not in total_revenue:
                total_revenue[tmp_list[0]]=float(tmp_list[3])
            else:
                total_revenue[tmp_list[0]]=total_revenue[tmp_list[0]]+float(tmp_list[3])
            # Populate the revenue per category
            if tmp_list[1] not in category_hash:
                category_hash[tmp_list[1]]=float(tmp_list[3])
            else:
                category_hash[tmp_list[1]]=category_hash[tmp_list[1]]+float(tmp_list[3])
        
        # Generate revenue per category for a customer
        for category in category_hash.keys():
            print category+" --- %s" %category_hash[category]
            sales_tax=0.0925 * category_hash[category]
            print "Sales Tax for "+category+" : %.2f" %sales_tax 
    
    print "\n------------------------- REPORT 2 ---------------------------"
    # Generate total revenue
    print "\nTotal Revenue per customer with their sales tax applicable"
    for customer in total_revenue.keys():
        print customer+" --- %s" %total_revenue[customer]
        sales_tax = 0.0925 * total_revenue[customer]
        print "Total Sales Tax : %.2f\n" %sales_tax
