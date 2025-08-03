from langchain.tools import tool 
import yfinance as yf 
import json

@tool
def simple_screener(screen_type:str, offset:int)-> str: 
    """Returns screened assets (stocks, funds, bonds) given popular criteria. 

    Args:
        screen_type: One of a default set of stock screener queries from yahoo finance. 
        aggressive_small_caps
        day_gainers
        day_losers
        growth_technology_stocks
        most_actives
        most_shorted_stocks
        small_cap_gainers
        undervalued_growth_stocks
        undervalued_large_caps
        conservative_foreign_funds
        high_yield_bond
        portfolio_anchors
        solid_large_growth_funds
        solid_midcap_growth_funds
        top_mutual_funds
      offset: the pagination start point

    Returns:
        The a JSON output of assets that meet the criteria
        """
    
    query = yf.PREDEFINED_SCREENER_QUERIES[screen_type]['query']
    result = yf.screen(query, offset=offset, size=5) 

    with open('output.json', 'w') as f: 
          json.dump(result, f) 
     
    fields = ["shortName","bid","ask","exchange", "fiftyTwoWeekHigh", "fiftyTwoWeekLow", "averageAnalystRating", "dividendYield", "symbol"] 
    output_data = []
    for stock_detail in result['quotes']: 
        details = {}
        for key, val in stock_detail.items(): 
            if key in fields: 
                details[key] = val 
        output_data.append(details) 
    
    return f"Stock Screener Results: {output_data}"

if __name__ == '__main__': 
    print(simple_screener({"screen_type":"day_gainers", "offset":0}))

    
