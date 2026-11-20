# (pi, question, [correct, wrong, wrong, wrong], explanation)  -- correct answer is ALWAYS listed first; the app shuffles.
Q = []
def q(pi, stem, opts, exp): Q.append((pi, stem, opts, exp))

# --- statements ---
q("FI:093","A business owner wants to know what the company owns and owes as of December 31. Which financial statement should she review?",
 ["Balance sheet","Income statement","Cash flow statement","Sales budget"],
 "The balance sheet is a snapshot of assets, liabilities and equity on one date. The income statement and cash flow statement cover a period of time.")
q("FI:094","Revenue minus cost of goods sold equals",
 ["gross profit.","net income.","operating expenses.","retained earnings."],
 "Gross profit = revenue − COGS. Net income comes after operating expenses, interest and taxes are subtracted too.")
q("FI:091","Which of the following would appear as a cash inflow on a business's statement of cash flows?",
 ["Selling a used delivery van","Paying suppliers for inventory","Paying employee wages","Repaying a bank loan"],
 "Selling an asset brings cash in (an investing inflow). The other three are cash payments out.")
q("FI:091","A company buys new ovens for $40,000 cash. On the statement of cash flows, this is reported as a(n)",
 ["investing activity.","operating activity.","financing activity.","owner's withdrawal."],
 "Buying or selling long-term assets like equipment is an investing activity.")
q("FI:091","Thornbury Tools paid a $5,000 dividend to its shareholders. Where does this appear on the statement of cash flows?",
 ["Financing activities","Operating activities","Investing activities","It does not appear"],
 "Transactions with owners and lenders (dividends, issuing stock, borrowing, repaying debt) are financing activities.")
q("FI:630","Net income earned and kept by the company is reported on the statement of changes in equity as",
 ["retained earnings.","contributed capital.","accounts payable.","dividends payable."],
 "Retained earnings is the equity component that accumulates net income not paid out as dividends.")
q("FI:630","A corporation pays its shareholders $2 per share from profits. On the statement of shareholders' equity, this payment is",
 ["recorded under dividends and reduces equity.","recorded as an operating expense.","added to contributed capital.","recorded as a liability on the income statement."],
 "Dividends are distributions of profit to owners. They reduce retained earnings and total equity. They are not an expense.")
q("FI:579","After comparing what she forecast with what actually happened last quarter, a café owner found sales were 12% lower than planned. She has identified a",
 ["variance.","dividend.","depreciation.","liability."],
 "A variance is the difference between budgeted or forecast figures and actual results.")
q("FI:579","Which is the most important reason a small business owner needs accurate financial information?",
 ["To make informed decisions about running and growing the business","To avoid ever paying taxes","To guarantee the business will never lose money","To replace the need for a budget"],
 "Financial information supports decisions: pricing, hiring, borrowing, investing. It can't guarantee profit or replace planning.")
q("FI:354","The finance function of a business is responsible for managing working capital and",
 ["making capital budgeting decisions.","designing advertising campaigns.","recruiting new employees.","setting quality standards for production."],
 "Finance obtains funds, invests them (capital budgeting) and manages working capital. Marketing, HR and operations handle the others.")
q("FI:093","Assets = $250,000 and liabilities = $90,000. What is the owner's equity?",
 ["$160,000","$340,000","$90,000","$250,000"],
 "Assets = Liabilities + Equity, so Equity = $250,000 − $90,000 = $160,000.")
q("FI:094","Which item would NOT appear on an income statement?",
 ["Cash on hand","Sales revenue","Rent expense","Cost of goods sold"],
 "Cash on hand is an asset on the balance sheet. The income statement shows revenues and expenses.")
q("FI:085","Under accrual accounting, a consulting firm that finishes a project in March but is paid in April records the revenue in",
 ["March, when it was earned.","April, when cash was received.","Both March and April.","Whichever month the owner chooses."],
 "Accrual accounting records revenue when it is earned, regardless of when cash arrives.")

# --- institutions & markets ---
q("FI:336","A growing manufacturer wants to raise $50 million by issuing new stock to the public for the first time. Which institution would it most likely hire?",
 ["Investment bank","Credit union","Savings and loan association","Insurance company"],
 "Investment banks underwrite new stock and bond issues and help firms find outside sources of capital.")
q("FI:336","Which financial institution is a not-for-profit cooperative owned by its members?",
 ["Credit union","Commercial bank","Investment bank","Brokerage firm"],
 "Credit unions are member-owned and not-for-profit, so they often offer lower loan rates and fees.")
q("FI:336","Which international institution provides loans and advice to developing countries to reduce poverty?",
 ["The World Bank Group","The Federal Reserve","The FDIC","The New York Stock Exchange"],
 "The World Bank Group finances development projects in lower-income countries. The Fed and FDIC are US institutions.")
q("FI:336","The primary purpose of an insurance company is to help customers",
 ["minimize financial risk.","maximize investment returns.","avoid paying taxes.","obtain mortgages."],
 "Insurance transfers risk. The customer pays a premium and the insurer covers specified losses.")
q("FI:337","Treasury bills that mature in 13 weeks are traded in the",
 ["money market.","capital market.","commodities market.","insurance market."],
 "The money market handles short-term debt (under one year), such as T-bills and commercial paper.")
q("FI:337","Investors who buy and sell shares of a company after its initial public offering are trading in the",
 ["secondary market.","primary market.","money market.","derivatives market."],
 "The primary market is the original sale by the issuer. Later trades between investors happen in the secondary market.")
q("FI:337","A trader buys oil futures contracts. This activity takes place in the",
 ["commodities market.","money market.","foreign exchange market.","insurance market."],
 "Commodity markets trade raw goods like oil, gold and wheat, and futures contracts on them.")
q("FI:337","Contracts such as options and swaps, whose values depend on an underlying asset, are traded in the",
 ["derivatives market.","primary market.","money market.","mortgage market."],
 "Derivatives get their value from an underlying asset like a stock, a commodity or an interest rate.")
q("FI:573","A national bank merges with a large insurance company so it can offer customers both products. This is an example of",
 ["convergence.","consolidation.","deregulation.","diversification of currency."],
 "Convergence combines firms from different financial sectors. Consolidation combines firms in the same sector.")
q("FI:573","Two regional banks merge to form one larger bank. This is an example of",
 ["consolidation.","convergence.","bancassurance.","securitization."],
 "Same-sector mergers are consolidation. They often create more liquid capital and economies of scale.")
q("FI:573","A strategy in which a bank sells insurance products to its customers is called",
 ["bancassurance.","underwriting.","front-running.","hedging."],
 "Bancassurance is a convergence strategy: banks distribute insurance through their branches and customer base.")

# --- economy, globalization, securities info ---
q("FI:574","During an economic contraction, stock prices in most industries tend to",
 ["decrease.","increase rapidly.","stay exactly the same.","double."],
 "Contractions bring lower GDP, hiring and spending, so company earnings and stock prices generally fall.")
q("FI:574","When a country's unemployment rate is high, which of the following is most likely?",
 ["The economy's output decreases.","Consumer spending increases sharply.","Stock prices rise across all industries.","Inflation rises quickly."],
 "Fewer people working means less income and spending, so output falls.")
q("FI:574","Shares of utility and grocery companies often hold their value during recessions because these industries",
 ["sell products people need in every phase of the business cycle.","are not affected by interest rates.","never compete with other firms.","are owned by the government."],
 "Defensive industries sell essentials, so demand stays steady while cyclical industries swing with the economy.")
q("FI:575","An investor keeps nearly all of her money in U.S. stocks and ignores foreign markets because she believes international investing is too risky. This is called",
 ["home bias.","herd mentality.","front-running.","dollar-cost averaging."],
 "Home bias is preferring domestic investments and missing the diversification benefits of foreign markets.")
q("FI:575","Which is a common characteristic of emerging markets?",
 ["Volatility, with chances for rapid growth and sharp declines","Guaranteed stable returns","No foreign investment","Very slow population growth"],
 "Emerging markets can grow fast but are less stable, with political, currency and liquidity risks.")
q("FI:575","A country holds an unexpected election that creates political uncertainty. Its currency's value will most likely",
 ["decrease.","increase.","stay fixed by law.","double."],
 "Global investors prefer stability. Uncertainty usually weakens a currency, at least temporarily.")
q("FI:274","A public company announces that its CEO resigned unexpectedly. It must report this event to the SEC on Form",
 ["8-K.","10-K.","W-2.","1040."],
 "Form 8-K reports major unscheduled events within days. The 10-K is the annual report.")
q("FI:274","Which source contains a corporation's audited financial statements along with management's discussion of the year?",
 ["Annual report","Stock table","Securities prospectus for a different company","Credit report"],
 "The annual report, including the 10-K filed with the SEC, is one of the best sources of company financial data.")
q("FI:275","In a stock table, a blank in the dividend column means the company",
 ["does not currently pay dividends.","is bankrupt.","paid a dividend that day.","is not traded on an exchange."],
 "The dividend column shows the annual dividend per share. A blank means none is currently paid.")
q("FI:275","Which stock table column helps an investor judge how volatile a stock has been over the past year?",
 ["52-week high and low","Ticker symbol","Volume","Dividend"],
 "A wide gap between the 52-week high and low means the price has swung a lot.")
q("FI:275","A stock's relative strength line is rising. This indicates the stock is",
 ["outperforming the overall market.","losing value every day.","about to pay a dividend.","trading below its 52-week low."],
 "Relative strength compares a stock's performance to the market. A rising line means it's beating the market.")
q("FI:275","In a stock table, the 'Open' price is",
 ["the first price at which the stock traded that day.","the highest price of the year.","the price of the last trade the previous week.","the price set by the SEC."],
 "Open = first trade of the day. Close = last trade of the day.")

# --- TVM & money ---
q("FI:238","You invest $1,000 at 5% interest compounded annually. About how much will you have after 2 years?",
 ["$1,102.50","$1,100.00","$1,050.00","$1,200.00"],
 "FV = 1,000 × 1.05² = 1,000 × 1.1025 = $1,102.50. Simple interest would give $1,100.")
q("FI:238","Marcus deposits $2,000 for one year at 6% interest. What is the future value?",
 ["$2,120","$2,012","$2,600","$2,060"],
 "Interest = $2,000 × .06 = $120, so FV = $2,120.")
q("FI:238","How much must you invest today at 10% compounded annually to have $12,100 in two years?",
 ["$10,000","$11,000","$9,800","$12,100"],
 "PV = FV ÷ (1 + i)ⁿ = 12,100 ÷ 1.21 = $10,000.")
q("FI:238","In the formula FV = PV × (1 + i)ⁿ, the letter n represents the",
 ["number of periods.","nominal value.","net income.","number of investors."],
 "n is the number of compounding periods, usually years. i is the interest rate per period.")
q("FI:062","The time value of money means that",
 ["a dollar today is worth more than a dollar received in the future.","money loses all value after one year.","interest rates never change.","future dollars are always worth more."],
 "Money available now can be invested to earn interest, so it is worth more than the same amount later.")
q("FI:060","Kai saves part of each paycheck in a jar to spend next summer. Which function of money does this illustrate?",
 ["Store of value","Medium of exchange","Unit of measure","Standard of deferred payment only"],
 "Money as a store of value lets people hold wealth to use later.")
q("FI:058","A customer taps her phone at the register to pay with a card stored in a digital wallet. This is an example of",
 ["contactless purchasing.","barter.","a check payment.","a cash advance."],
 "Contactless payments use cards stored electronically in a digital wallet or tap-enabled card.")
q("FI:059","A currency that is decentralized and not issued by any government is called",
 ["cryptocurrency.","a treasury note.","a banknote.","fiat money."],
 "Cryptocurrencies run on decentralized networks (blockchains) rather than being issued by a central bank.")
q("FI:002","Which of the following is a purpose of credit?",
 ["It allows buyers to purchase now and pay later.","It eliminates the cost of borrowing.","It guarantees a lower price.","It replaces the need for income."],
 "Credit lets people and businesses buy before paying in full, usually at a cost (interest).")
q("FI:002","A bank evaluates whether a borrower has enough income to make loan payments. Which of the five Cs of credit is this?",
 ["Capacity","Character","Collateral","Conditions"],
 "Capacity is the ability to repay, judged by income and debt-to-income. Character is trustworthiness; collateral is pledged assets.")
q("FI:066","Which is a variable expense in a personal budget?",
 ["Groceries","Monthly rent","Car insurance premium","Fixed loan payment"],
 "Variable expenses change month to month. Rent, insurance premiums and fixed loan payments stay the same.")
q("FI:081","Which type of life insurance covers the policyholder for a set number of years and builds no cash value?",
 ["Term life","Whole (ordinary) life","Universal life","Variable life"],
 "Term life is temporary and cheaper. Whole life lasts for life and builds cash value.")
q("FI:061","Wages, salaries and tips are examples of",
 ["earned income.","passive income.","capital gains.","dividends."],
 "Earned income comes from working. Interest, dividends and capital gains are investment income.")

# --- managerial ---
q("FI:660","Which type of accounting prepares reports for a company's internal managers to help them make day-to-day decisions?",
 ["Managerial accounting","Financial accounting","Tax accounting","Government accounting"],
 "Managerial accounting serves internal users and isn't bound by GAAP. Financial accounting serves outside users.")
q("FI:660","Financial accounting ___ historical data, while managerial accounting ___ data for decision-making.",
 ["records; interprets","interprets; records","hides; publishes","audits; ignores"],
 "Financial accounting records and reports what happened. Managerial accounting interprets it to plan and control.")
q("FI:658","A company spent $20,000 on market research last year for a product it may not launch. When deciding whether to launch, this $20,000 is a",
 ["sunk cost.","variable cost.","differential cost.","opportunity cost."],
 "Sunk costs are already spent and can't be recovered, so they shouldn't affect the decision.")
q("FI:658","Option A costs $6,000 and Option B costs $8,500. The differential cost is",
 ["$2,500.","$14,500.","$6,000.","$8,500."],
 "Differential cost is the difference between two alternatives: $8,500 − $6,000 = $2,500.")
q("FI:658","Which of the following is a direct cost for a furniture maker?",
 ["Wood used to build tables","Electricity for the factory","The CEO's salary","Insurance on the building"],
 "Direct costs trace to a specific product. Utilities, executive pay and insurance are indirect (overhead).")
q("FI:663","Electricity for an entire factory that makes five different products is an example of a(n)",
 ["indirect cost.","direct cost.","sunk cost.","differential cost."],
 "Indirect costs are shared and can't easily be traced to one product, so they must be allocated.")
q("FI:663","Assigning a share of the building's rent to each department based on square footage is an example of",
 ["cost allocation.","variance analysis.","capital budgeting.","depreciation."],
 "Cost allocation assigns indirect costs to cost objects using a cost driver, here square footage.")
q("FI:661","A project manager compares the labor hours she budgeted with the hours actually worked. She is performing",
 ["variance analysis.","marginal analysis.","horizontal analysis.","break-even analysis."],
 "Variance analysis compares planned and actual figures to find why they differ and improve future estimates.")
q("FI:661","Variance analysis shows a project needed far more labor than estimated. What should the manager most likely do next?",
 ["Reevaluate the estimated time and labor for future projects","Ignore the difference","Cut the marketing budget","Fire the entire team"],
 "The value of variance analysis is learning from the gap and refining future estimates and budgets.")
q("FI:659","A bakery owner considers whether staying open one extra hour will bring in more revenue than the added wage and utility costs. She is using",
 ["marginal analysis.","vertical analysis.","ratio analysis.","sunk-cost analysis."],
 "Marginal analysis compares the added benefit and added cost of one change in activity.")
q("FI:662","Cost accounting helps a business",
 ["identify the causes of variances and improve efficiency.","prepare its tax return.","attract new customers.","sell stock to the public."],
 "Cost accounting captures the full cost of production so managers can find inefficiencies and control costs.")
q("FI:106","A store sets its spending plan for next year, but sales turn out 20% higher than expected. Its fixed budget did not change. A weakness of a static budget is that it",
 ["does not adjust for changes in activity levels.","is too flexible.","cannot be written down.","includes only revenue."],
 "A static (fixed) budget stays at one activity level. A flexible budget adjusts to actual volume.")
