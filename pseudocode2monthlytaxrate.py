BEGIN
    PROMPT user for total sales for the month
    SET state_tax_rate TO 0.05
    SET county_tax_rate TO 0.025

    FUNCTION calculate_taxes(total_sales)
        SET state_tax TO total_sales * state_tax_rate
        SET county_tax TO total_sales * county_tax_rate
        SET total_tax TO state_tax + county_tax
        RETURN state_tax, county_tax, total_tax
    END FUNCTION

    CALL calculate_taxes(total_sales)
    DISPLAY "State Tax: " + state_tax
    DISPLAY "County Tax: " + county_tax
    DISPLAY "Total Sales Tax: " + total_tax
END
