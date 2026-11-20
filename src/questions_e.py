# Extra exam questions, part E: Financial Analysis (24 on the district blueprint), Financial-Information
# Management (9), Risk Management (6) and Business Law (7). Heavy on the personal-finance PIs that recent
# FTDM district cases used (save and invest, types of investments, insurance needs, credit, TVM).
# Format: (PI, stem, [correct answer FIRST, then 3 wrong answers], explanation). All original.
Q = []
def q(pi, stem, opts, exp): Q.append((pi, stem, opts, exp))

# ---------------- Personal finance: saving, investing, goals ----------------
q("FI:270","Why should a young worker start investing for retirement as early as possible?",
  ["Compound growth has more years to work","Early investments are guaranteed not to lose value","Taxes on investments are lower for young people","Retirement accounts close to people over 30"],
  "The earlier you start, the more years your earnings can earn their own returns. Time matters more than the amount at first.")
q("FI:270","Which is the main reason to keep an emergency fund in a savings account rather than in stocks?",
  ["The money must be available quickly without risk of loss","Savings accounts earn higher long-term returns than stocks","Stocks cannot be sold","Emergency funds are taxed less in savings"],
  "Emergency money needs liquidity and safety. Stocks can drop sharply right when you need the cash.")
q("FI:270","Setting up an automatic transfer from each paycheck into savings before paying other expenses is called",
  ["paying yourself first.","dollar-cost averaging.","diversification.","compounding."],
  "Paying yourself first makes saving automatic so it isn't skipped.")
q("FI:077","Investing the same dollar amount in a fund every month, regardless of price, is called",
  ["dollar-cost averaging.","market timing.","day trading.","short selling."],
  "Dollar-cost averaging buys more shares when prices are low and fewer when high, and removes the temptation to time the market.")
q("FI:077","Which investment pools money from many investors and tracks a market index, such as the S&P 500, at a low cost?",
  ["Index fund","Certificate of deposit","Individual corporate bond","Savings bond"],
  "Index funds (mutual funds or ETFs) hold all the stocks in an index, giving broad diversification at low fees.")
q("FI:077","Which investment generally has the highest risk and the highest potential long-term return?",
  ["Stocks","Certificates of deposit","Treasury bills","Savings accounts"],
  "Stocks are ownership shares. They fluctuate more than bonds or cash but have historically earned the most over long periods.")
q("FI:077","When you buy a bond, you are",
  ["lending money to the issuer in exchange for interest","buying ownership in the company","buying an insurance policy","opening a deposit account"],
  "A bond is a loan to a government or company. Stocks are ownership.")
q("FI:077","Spreading money across stocks, bonds and cash so that one bad investment doesn't ruin a portfolio is",
  ["diversification.","leverage.","speculation.","liquidity."],
  "Diversification reduces risk because different investments don't all fall at the same time.")
q("FI:077","A fund that automatically shifts from mostly stocks to more bonds as a chosen retirement year approaches is a",
  ["target-date fund.","money market fund.","hedge fund.","sector fund."],
  "Target-date funds become more conservative over time, a simple one-fund option for retirement savers.")
q("FI:077","A real estate investment trust (REIT) lets an investor",
  ["own a share of a portfolio of income-producing properties","buy a single home with no down payment","avoid all investment risk","borrow money at a fixed rate"],
  "REITs own properties such as apartments or offices and pay out most of their income to shareholders.")
q("FI:065","Saving for a house down payment in four years is which type of financial goal?",
  ["Medium-term","Short-term","Long-term","Emergency"],
  "Short-term goals are usually under 1 year, medium-term about 1 to 5 years, long-term more than 5 years.")
q("FI:062","Using the Rule of 72, about how long will it take money to double at an 8% annual return?",
  ["9 years","6 years","12 years","16 years"],
  "Divide 72 by the interest rate: 72 ÷ 8 = 9 years.")
q("FI:238","You deposit $5,000 at 4% interest compounded annually. How much will you have after 2 years?",
  ["$5,408","$5,400","$5,200","$5,816"],
  "Year 1: $5,000 × 1.04 = $5,200. Year 2: $5,200 × 1.04 = $5,408. The extra $8 is interest on interest.")
q("FI:238","Simple interest on $3,000 at 5% per year for 3 years is",
  ["$450","$150","$473","$3,450"],
  "Simple interest = principal × rate × time = $3,000 × 0.05 × 3 = $450.")
q("FI:569","An employer matches 100% of employee 401(k) contributions up to 4% of salary. An employee earning $50,000 contributes 4%. How much does the employer add per year?",
  ["$2,000","$4,000","$1,000","$500"],
  "4% of $50,000 = $2,000 from the employee, matched dollar-for-dollar with $2,000 from the employer.")
q("FI:569","What is the main tax difference between a Roth IRA and a traditional IRA?",
  ["Roth contributions are made after tax and qualified withdrawals are tax-free","Roth contributions are tax-deductible and withdrawals are taxed","Traditional IRAs are never taxed","Only Roth IRAs can hold stocks"],
  "Roth: pay tax now, tax-free later. Traditional: tax deduction now, pay tax when you withdraw.")
q("FI:831","Which account offers tax-free growth when the money is used for qualified education expenses?",
  ["529 plan","Health savings account","Traditional IRA","Certificate of deposit"],
  "529 plans are state-sponsored education savings plans. Earnings are tax-free for qualified education costs.")
q("FI:572","A legal document that states how a person's property should be distributed after death is a",
  ["will.","power of attorney.","deed.","prospectus."],
  "A will directs who gets your property and can name a guardian for minor children. A power of attorney works only while you're alive.")
q("FI:562","Kendra has $18,000 in assets and owes $11,000 on a car loan and credit cards. Her net worth is",
  ["$7,000","$29,000","$11,000","-$7,000"],
  "Net worth = assets − liabilities = $18,000 − $11,000 = $7,000.")
q("FI:066","Under the 50/30/20 budgeting guideline, what share of after-tax income goes to savings and paying down debt?",
  ["20%","50%","30%","10%"],
  "50% needs, 30% wants, 20% savings and extra debt payments.")
q("FI:068","On a pay stub, the amount left after taxes and other deductions are subtracted is",
  ["net pay.","gross pay.","year-to-date earnings.","withholding."],
  "Gross pay is total earnings before deductions. Net pay is what you take home.")
q("FI:067","Which tax is withheld from paychecks to fund Social Security and Medicare?",
  ["FICA","Sales tax","Property tax","Excise tax"],
  "FICA (Federal Insurance Contributions Act) taxes fund Social Security and Medicare.")

# ---------------- Credit ----------------
q("FI:071","Which habit does the most to help a person build a good credit score?",
  ["Paying every bill on time","Opening many new credit cards at once","Using the full credit limit every month","Closing the oldest credit card"],
  "Payment history is the largest factor in a FICO score, about 35%.")
q("FI:071","A credit card has a $2,000 limit and a $1,500 balance. What is the credit utilization rate?",
  ["75%","25%","50%","133%"],
  "Utilization = balance ÷ limit = $1,500 ÷ $2,000 = 75%. Keeping it under 30% helps your score.")
q("FI:072","How can consumers check their credit reports from the three major bureaus for free?",
  ["At AnnualCreditReport.com","By paying a credit repair company","Only by applying for a loan","Through the Federal Reserve"],
  "AnnualCreditReport.com is the official free source for Equifax, Experian and TransUnion reports.")
q("FI:782","A $1,000 loan for one year costs $120 in interest and $30 in fees. What is the total finance charge?",
  ["$150","$120","$30","$1,150"],
  "The finance charge includes interest and fees: $120 + $30 = $150.")
q("FI:568","Paying off debts from the highest interest rate to the lowest, while making minimum payments on the rest, is the",
  ["avalanche method.","snowball method.","consolidation method.","minimum method."],
  "The avalanche method saves the most interest. The snowball method pays smallest balances first for quick wins.")
q("FI:073","Which action best protects against identity theft?",
  ["Freezing your credit with the three bureaus","Using the same password for every account","Carrying your Social Security card in your wallet","Sharing account numbers on social media"],
  "A credit freeze stops new accounts from being opened in your name. It is free.")
q("FI:063","The Truth in Lending Act requires lenders to",
  ["disclose the APR and total finance charges before a loan is made","offer the lowest rate in the market","approve all loan applications","give loans without interest"],
  "The Truth in Lending Act requires clear disclosure of credit costs so consumers can compare.")
q("FI:625","Which document will a lender most likely request when you apply for a car loan?",
  ["Proof of income, such as recent pay stubs","Your high school transcript","Your medical records","A list of your friends"],
  "Lenders verify capacity to repay with income documents and check credit history.")

# ---------------- Insurance ----------------
q("FI:571","A couple with a new baby depends on both of their incomes. Which insurance need should they review first?",
  ["Life insurance on both parents","Pet insurance","Flood insurance on their car","Travel insurance"],
  "When others depend on your income, life insurance replaces it if you die. A new child is a key trigger to review coverage.")
q("FI:571","Which insurance replaces part of your income if an illness or injury keeps you from working?",
  ["Disability insurance","Liability insurance","Term life insurance","Homeowners insurance"],
  "Disability insurance pays a portion of income during a long illness or injury.")
q("FI:571","An inexpensive policy that adds extra liability protection above home and auto coverage is",
  ["umbrella insurance.","whole life insurance.","renters insurance.","collision insurance."],
  "Umbrella policies cover large liability claims, such as lawsuits, beyond your other policies' limits.")
q("FI:081","The amount a policyholder must pay out of pocket before insurance begins to pay a claim is the",
  ["deductible.","premium.","copay limit.","beneficiary."],
  "The premium is what you pay for the policy. The deductible is what you pay per claim before coverage starts.")
q("FI:081","Choosing a higher deductible on an insurance policy usually",
  ["lowers the premium","raises the premium","has no effect on the premium","cancels the policy"],
  "Taking on more of the risk yourself (higher deductible) lowers what the insurer charges.")
q("FI:081","Which type of life insurance lasts your whole life and builds cash value?",
  ["Whole life insurance","Term life insurance","Disability insurance","Umbrella insurance"],
  "Whole (permanent) life insurance builds cash value but costs much more than term insurance for the same coverage.")

# ---------------- Institutions, markets, economy ----------------
q("FI:336","The FDIC insures deposits at member banks up to",
  ["$250,000 per depositor, per bank, per ownership category","$100,000 per bank","$1 million per person","the full amount with no limit"],
  "The FDIC standard limit is $250,000. Credit union deposits get the same protection from the NCUA.")
q("FI:336","Which statement about credit unions compared with banks is most accurate?",
  ["Credit unions are member-owned not-for-profits and often have lower loan rates","Credit unions are owned by outside shareholders","Credit union deposits are not insured","Credit unions cannot make loans"],
  "Credit unions return earnings to members through better rates and lower fees. Deposits are insured by the NCUA.")
q("FI:336","Which organization protects customers' securities and cash if their brokerage firm fails?",
  ["SIPC","FDIC","SEC","FINRA"],
  "SIPC protects up to $500,000, including $250,000 cash, if a brokerage fails. It does not protect against market losses.")
q("FI:337","A company sells new shares of stock to the public for the first time in the",
  ["primary market through an initial public offering (IPO).","secondary market.","money market.","foreign exchange market."],
  "New securities are sold in the primary market. Later trading between investors happens in the secondary market.")
q("FI:337","Which market is used for long-term borrowing and investing, such as stocks and bonds that last longer than a year?",
  ["Capital market","Money market","Commodities market","Insurance market"],
  "Capital markets handle long-term funds. Money markets handle short-term debt of one year or less.")
q("FI:337","A U.S. company exchanges dollars for euros to pay a supplier in Germany. This takes place in the",
  ["foreign exchange market.","stock market.","bond market.","insurance market."],
  "The foreign exchange (forex) market is where currencies are traded.")
q("FI:574","A long period in which stock prices fall 20% or more from their peak is called a",
  ["bear market.","bull market.","correction.","rally."],
  "A bear market is a drop of 20% or more. A correction is a drop of about 10%. A bull market is a long rise.")
q("FI:574","When interest rates rise, what generally happens to the prices of existing bonds?",
  ["They fall","They rise","They stay the same","They double"],
  "New bonds pay higher rates, so older bonds paying lower rates become less valuable.")
q("FI:575","An investor buys shares of a Japanese company on a U.S. exchange through an American depositary receipt (ADR). The main added risk is",
  ["currency risk from changes in the yen-dollar exchange rate","FDIC insurance limits","guaranteed losses","higher U.S. income tax rates"],
  "Foreign investments carry exchange-rate risk: returns change when currencies move.")
q("FI:573","The Gramm-Leach-Bliley Act of 1999 allowed",
  ["banks, securities firms and insurance companies to combine under one company","the creation of the FDIC","the end of credit cards","banks to stop paying interest"],
  "GLBA repealed parts of the Glass-Steagall Act, allowing financial convergence, and added privacy rules.")

# ---------------- Business finance and accounting ----------------
q("FI:093","A company has current assets of $90,000 and current liabilities of $60,000. What is its current ratio?",
  ["1.5","0.67","30,000","150"],
  "Current ratio = current assets ÷ current liabilities = $90,000 ÷ $60,000 = 1.5.")
q("FI:094","A business has revenue of $400,000, cost of goods sold of $240,000 and operating expenses of $100,000. What is its net income before taxes?",
  ["$60,000","$160,000","$140,000","$300,000"],
  "Gross profit = $400,000 − $240,000 = $160,000. Net income before taxes = $160,000 − $100,000 = $60,000.")
q("FI:106","A budget that starts from zero each year and requires every expense to be justified is a",
  ["zero-based budget.","fixed budget.","flexible budget.","incremental budget."],
  "Zero-based budgeting makes managers justify every expense instead of adding a percentage to last year's budget.")
q("FI:106","Break-even point in units = fixed costs ÷ (price per unit − variable cost per unit). A food truck has $30,000 in fixed costs, sells meals for $12 and has $7 in variable cost per meal. How many meals must it sell to break even?",
  ["6,000","2,500","4,286","10,000"],
  "Contribution per meal = $12 − $7 = $5. $30,000 ÷ $5 = 6,000 meals.")
q("FI:355","A financial manager delays recording expenses so this quarter's profit looks better before a loan review. This is",
  ["unethical and misleading to lenders.","an acceptable way to manage earnings.","required by GAAP.","a form of risk transfer."],
  "Manipulating the timing of expenses misrepresents results. Ethics in finance requires honest, accurate reporting.")
q("FI:353","Generally accepted accounting principles (GAAP) in the United States are set by the",
  ["Financial Accounting Standards Board (FASB).","Federal Reserve.","Internal Revenue Service.","FDIC."],
  "FASB sets U.S. GAAP. The SEC requires public companies to follow it. The IASB sets international standards (IFRS).")
q("FI:352","Which is a key benefit of cloud-based accounting software for a small business?",
  ["The owner and accountant can see up-to-date records from anywhere","It removes the need for any record keeping","It guarantees the business will be profitable","It eliminates all cybersecurity risk"],
  "Cloud tools such as QuickBooks Online and Xero give real-time access and automate bank feeds, though data must still be secured.")

# ---------------- Financial-Information Management ----------------
q("FM:009","A company's net income is $50,000 on revenue of $500,000. What is its net profit margin?",
  ["10%","50%","1%","25%"],
  "Net profit margin = net income ÷ revenue = $50,000 ÷ $500,000 = 10%.")
q("FM:014","Return on equity (ROE) measures",
  ["how much profit a company generates with the owners' investment","how quickly inventory sells","how much cash is on hand","how many shares are outstanding"],
  "ROE = net income ÷ shareholders' equity. It shows how efficiently owners' money is used.")
q("FM:014","A company's debt-to-equity ratio rises from 0.5 to 2.0 over three years. What does this most likely mean?",
  ["The company now relies much more on borrowed money and is riskier","The company paid off its debt","The company is more profitable","Shareholders invested more money"],
  "A higher debt-to-equity ratio means more financing comes from creditors, which raises financial risk.")
q("FM:013","Before deciding to open a new branch, a manager uses budgeting software to see what profit would look like if sales were 10% lower or 10% higher than expected. This is",
  ["scenario (what-if) analysis.","an external audit.","normalization.","a variance report."],
  "What-if analysis tests how results change under different assumptions.")
q("FM:011","Which technology helps finance teams detect unusual transactions in real time?",
  ["Machine learning fraud-detection software","A paper ledger","A fax machine","A spreadsheet printed monthly"],
  "Machine learning flags transactions that don't fit normal patterns for review.")
q("FM:003","An accountant is asked by her manager to classify a personal expense as a business expense. The most ethical response is to",
  ["refuse and explain it would misstate the financial records","do it because the manager asked","do it but keep a private note","ask a coworker to do it instead"],
  "Ethical financial-information management requires accurate records even under pressure.")
q("FM:016","A company reports how much water and energy it saves along with its financial results. This is an example of",
  ["a non-traditional use of financial information (sustainability reporting).","a cash flow statement.","a variance analysis.","a balance sheet."],
  "Sustainability and ESG reports connect environmental and social results to financial performance.")
q("FM:002","Which is a responsibility of the financial-information management function?",
  ["Collecting, analyzing and reporting financial data for decision-making","Designing the company's logo","Hiring sales staff","Setting the Federal Reserve's interest rate"],
  "FIM turns financial data into useful information for managers, investors and regulators.")
q("FM:009","A lender reviews a client's debt-to-income ratio. If the client earns $6,000 a month and has $2,100 in monthly debt payments, the ratio is",
  ["35%","28%","65%","2.86%"],
  "Debt-to-income = monthly debt payments ÷ gross monthly income = $2,100 ÷ $6,000 = 35%.")

# ---------------- Risk Management ----------------
q("RM:058","A bank requires employees to take at least one week of consecutive vacation each year so someone else handles their work. The main purpose is to",
  ["uncover fraud that requires daily attention to hide","reduce payroll costs","improve marketing","meet minimum wage laws"],
  "Mandatory vacation is an internal control: schemes often fall apart when someone else does the job.")
q("RM:058","Which is an example of an external risk to a bank?",
  ["A sudden rise in interest rates","An employee entering data incorrectly","A broken teller machine","A weak hiring process"],
  "External risks come from outside the company (economy, regulation, nature). Internal risks come from inside.")
q("RM:062","Under enterprise risk management, a company's risk appetite is",
  ["the amount and type of risk it is willing to accept to reach its goals","the total value of its insurance policies","the number of risks it has eliminated","its credit rating"],
  "Risk appetite guides which risks to accept, reduce or avoid across the organization.")
q("RM:062","The COSO framework is widely used to guide",
  ["internal control and enterprise risk management","stock trading","tax filing","marketing campaigns"],
  "COSO publishes the most widely used frameworks for internal control (2013) and ERM (2017).")
q("RM:042","A bank runs a simulated ransomware attack to see how quickly employees respond. This is an example of",
  ["using technology to test and strengthen risk controls.","a sunk cost.","front-running.","an external audit."],
  "Testing incident response helps find weaknesses before a real attack.")
q("RM:043","Which law requires the CEO and CFO of a public company to personally certify the accuracy of financial reports?",
  ["Sarbanes-Oxley Act","Fair Labor Standards Act","Truth in Lending Act","Gramm-Leach-Bliley Act"],
  "Sarbanes-Oxley (2002), passed after Enron and WorldCom, requires executive certification and internal-control reporting.")
q("RM:041","A financial firm discovers a data breach. Which action is most ethical?",
  ["Notify affected customers promptly and help them protect their accounts","Wait to see if anyone notices","Delete the logs","Blame a vendor publicly before investigating"],
  "Ethical risk management means transparency and protecting those affected. Most states also require breach notification.")

# ---------------- Business Law ----------------
q("BL:133","Which agency regulates the securities industry and enforces federal securities laws?",
  ["Securities and Exchange Commission (SEC)","Federal Deposit Insurance Corporation (FDIC)","Internal Revenue Service (IRS)","Consumer Product Safety Commission"],
  "The SEC protects investors and oversees securities markets. FINRA regulates broker-dealers under SEC oversight.")
q("BL:133","A broker makes excessive trades in a client's account mainly to earn commissions. This illegal practice is",
  ["churning.","diversifying.","rebalancing.","hedging."],
  "Churning puts the broker's commissions ahead of the client's interest.")
q("BL:133","Which agency was created by the Dodd-Frank Act to protect consumers in financial products such as mortgages and credit cards?",
  ["Consumer Financial Protection Bureau (CFPB)","Federal Reserve","FINRA","SIPC"],
  "Dodd-Frank (2010) created the CFPB after the 2008 financial crisis.")
q("BL:133","Under Regulation Best Interest, a broker-dealer recommending an investment to a retail customer must",
  ["act in the customer's best interest and not put its own interest first","guarantee the investment will make money","recommend only the cheapest product","avoid charging any commission"],
  "Reg BI (2020) requires brokers to act in the retail customer's best interest and disclose conflicts.")
q("BL:134","Which retirement account lets an employee contribute pre-tax money directly from a paycheck?",
  ["Traditional 401(k)","Roth IRA","Taxable brokerage account","Savings bond"],
  "Traditional 401(k) contributions reduce taxable income now; withdrawals are taxed in retirement.")
q("BL:134","An investor holds a stock for more than one year before selling it at a profit. The gain is taxed as a",
  ["long-term capital gain, usually at a lower rate","short-term capital gain at ordinary income rates","sales tax","gift tax"],
  "Gains on investments held more than one year get lower long-term capital gains rates.")
q("BL:148","Banks must report cash transactions over $10,000 to the government to help prevent",
  ["money laundering.","inflation.","identity theft.","insider trading."],
  "Under the Bank Secrecy Act, banks file Currency Transaction Reports and suspicious activity reports to fight money laundering.")
q("BL:148","A bank checks a new customer's identity documents before opening an account. This is required by",
  ["know-your-customer (KYC) and anti-money-laundering rules.","the Fair Labor Standards Act.","GAAP.","the CARD Act."],
  "Customer identification programs help stop fraud, money laundering and terrorist financing.")
q("BL:003","Which form of business ownership protects the owners' personal assets from business debts while letting profits pass through to their personal tax returns?",
  ["Limited liability company (LLC)","Sole proprietorship","General partnership","Nonprofit corporation"],
  "LLCs give limited liability with pass-through taxation. Sole proprietors and general partners have unlimited liability.")
q("BL:003","An S corporation differs from a C corporation mainly because an S corporation",
  ["passes profits through to owners' personal tax returns, avoiding double taxation","has unlimited shareholders","cannot have employees","pays a higher corporate tax"],
  "S corps avoid corporate income tax but are limited to 100 shareholders who must be U.S. citizens or residents.")
q("BL:002","For a contract to be legally binding, which element is required?",
  ["Offer and acceptance between parties who have legal capacity","A notary's signature","A written document in every case","A payment of at least $500"],
  "Contracts need agreement (offer and acceptance), consideration, capacity and a legal purpose. Many contracts can be oral.")
