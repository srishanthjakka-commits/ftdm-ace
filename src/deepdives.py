# PI deep dives: every Tier 2 (Finance cluster) PI plus the Tier 1 PIs that FTDM case studies use most.
# Fields: plain = how to explain it to a judge in 1-2 sentences; key = must-know terms; apply = how to use it
# with a client; proof = real-world facts with sources; trap = common exam trap; chart = visual to sketch in prep;
# learn = official or reputable places to read more. Facts checked November 2026.
DD = []
def dd(pi, plain, key, apply, proof, trap="", chart="", learn=()):
    DD.append(dict(pi=pi, plain=plain, key=key, apply=apply, proof=proof, trap=trap, chart=chart, learn=[list(x) for x in learn]))

INV = ("SEC Investor.gov", "https://www.investor.gov")
CFPB = ("Consumer Financial Protection Bureau", "https://www.consumerfinance.gov")
FDIC = ("FDIC", "https://www.fdic.gov")
FED = ("Federal Reserve", "https://www.federalreserve.gov")
IRS = ("IRS", "https://www.irs.gov")
SBA = ("U.S. Small Business Administration", "https://www.sba.gov")
FINRA = ("FINRA", "https://www.finra.org")
EDGAR = ("SEC EDGAR filings", "https://www.sec.gov/edgar")
COSO = ("COSO", "https://www.coso.org")
BLS = ("BLS Occupational Outlook Handbook", "https://www.bls.gov/ooh")
III = ("Insurance Information Institute", "https://www.iii.org")
FTC = ("FTC IdentityTheft.gov", "https://www.identitytheft.gov")
ACR = ("AnnualCreditReport.com", "https://www.annualcreditreport.com")
SSA = ("Social Security Administration", "https://www.ssa.gov")
SAID = ("Federal Student Aid", "https://studentaid.gov")
TD = ("TreasuryDirect", "https://www.treasurydirect.gov")
NCUA = ("NCUA", "https://www.ncua.gov")
FASB = ("FASB", "https://www.fasb.org")
FINCEN = ("FinCEN", "https://www.fincen.gov")
NGPF = ("Next Gen Personal Finance (free lessons)", "https://www.ngpf.org")
MBA = ("MBA Research (publisher of the LAPs the exam cites)", "https://www.mbaresearch.org")

# =================== TIER 2: FINANCE CLUSTER ===================
dd("BL:133","The finance industry is one of the most regulated in the country because it handles other people's money. Firms must follow securities, banking, consumer-protection and privacy laws, and break them at the cost of fines, bans and trust.",
 ["Securities Act of 1933 (disclose new securities) and Securities Exchange Act of 1934 (created the SEC)","Regulators: SEC (securities), FINRA (brokers), Federal Reserve, OCC and FDIC (banks), CFPB (consumer products), state insurance departments","Illegal practices: insider trading, front-running, churning, Ponzi and pump-and-dump schemes","Regulation Best Interest (2020) for brokers; fiduciary duty for registered investment advisers"],
 "Show the client the law protects them: \"Our recommendations must be in your best interest, and you can check our record on FINRA BrokerCheck.\" For a firm, name the specific law, the regulator and the consequence.",
 ["Wells Fargo paid $3 billion in 2020 to settle criminal and civil cases over millions of fake accounts (U.S. Department of Justice).","FTX founder Sam Bankman-Fried was sentenced to 25 years in 2024 for fraud (U.S. Department of Justice)."],
 "Front-running uses a client's pending order; insider trading uses non-public company news. Don't mix them up.",
 "Comparison table: practice, why it's illegal, regulator, penalty.", [INV, FINRA])
dd("BL:134","Taxes change the real return of almost every financial decision, so finance professionals plan around them: which account to use, when to sell, and how to finance a business.",
 ["Capital gains: held over 1 year = long-term (lower rates); 1 year or less = short-term (ordinary income rates)","Capital losses offset gains (tax-loss harvesting); up to $3,000 of extra losses a year can offset ordinary income","Tax-advantaged accounts: 401(k), IRA, Roth IRA, HSA, 529","Interest on business debt is generally deductible; dividends are not, which favors debt financing"],
 "Turn tax rules into client wins: \"Put this in a Roth IRA while your tax rate is low, and hold investments over a year to get the lower long-term rate.\"",
 ["2026 standard deduction: $16,100 single, $32,200 married filing jointly (IRS, Oct. 2025).","2027 IRA limit stays $7,500; 401(k) rises to $25,500 (IRS Notice 2026-66)."],
 "Losses offset gains first, then up to $3,000 of ordinary income; they don't erase all income.",
 "Two bars: after-tax value of the same investment in a taxable account vs a Roth.", [IRS])
dd("BL:148","Compliance is the system a financial firm uses to follow laws, regulations and its own policies. Its job is to prevent violations first, then detect and correct them.",
 ["Prevent, detect, correct (in that order)","Chief compliance officer, written policies, training, monitoring and testing, reporting to the board","Anti-money laundering: Bank Secrecy Act, Currency Transaction Reports over $10,000, Suspicious Activity Reports, Know Your Customer","Consequences of noncompliance: fines, audits, lawsuits, license loss, reputation damage"],
 "Frame compliance as protection, not red tape: \"Strong compliance keeps customers' money safe and keeps regulators from shutting down the products you depend on.\"",
 ["Banks must file a Currency Transaction Report for cash transactions over $10,000 (FinCEN, Bank Secrecy Act)."],
 "The compliance department's first priority is prevention, not punishment.",
 "Flowchart: prevent (policies, training) → detect (monitoring) → correct (fix, report).", [FINCEN, FINRA])
dd("BL:149","Regtech is technology that automates compliance: monitoring transactions, screening customers, keeping records and filing reports, which cuts cost and catches patterns people miss.",
 ["Transaction monitoring and trade surveillance software","Automated identity verification (KYC) and sanctions screening","Electronic recordkeeping and audit trails","AI flags anomalies; humans review the alerts"],
 "Recommend specific tools: \"Trade-surveillance software flags any employee trade near a client order, so the compliance team reviews it the same day.\"",
 ["The SEC requires public-company financial statements to be tagged in XBRL so computers can read them (SEC)."],
 "Technology reduces compliance costs; it doesn't remove the need for human judgment.",
 "Before/after bars: hours spent on manual checks vs automated.", [("SEC", "https://www.sec.gov")])
dd("CR:012","Finance professionals must put clients first: understand their goals, give suitable advice, explain costs and conflicts, protect their information, and keep serving them over time.",
 ["Know Your Customer and suitability: goals, time horizon, risk tolerance before recommending","Fiduciary duty / Regulation Best Interest","Disclose fees and conflicts of interest","Confidentiality (Gramm-Leach-Bliley privacy rules)","Ongoing service: regular reviews, clear communication"],
 "This was a 2026 district PI. Open with it: \"Before we recommend anything, here's how we work for you: we learn your goals, we explain how we're paid, we act in your best interest, and you can verify us on FINRA BrokerCheck.\"",
 ["Regulation Best Interest has required broker-dealers to act in retail customers' best interest since June 30, 2020 (SEC).","CFP professionals must act as fiduciaries when giving financial advice (CFP Board Code of Ethics)."],
 "The first thing to learn is the client's needs and expectations, not which product to sell.",
 "Process flow: discover → analyze → recommend → implement → review (a loop).", [INV, ("FINRA BrokerCheck", "https://brokercheck.finra.org")])
dd("CR:024","CRM technology stores every client's information and interactions in one place so the whole team can give personal, consistent service and spot what each client needs next.",
 ["Single customer view: contact history, accounts, goals, life events","Uses: reminders, segmentation, cross-selling, retention alerts","Data mining: regression predicts a number, classification predicts a category","Human judgment separates useful data from noise; privacy rules apply"],
 "Make it concrete: \"When a client's direct deposit jumps, the CRM prompts the advisor to call about raising 401(k) contributions.\"",
 ["Salesforce offers a Financial Services Cloud built for banks, wealth managers and insurers (Salesforce)."],
 "CRM's main purpose is serving customers better over time, not just storing names.",
 "Hub-and-spoke diagram: client in the center, data sources around it.", [])
dd("FI:336","Financial institutions move money from people who have it (savers) to people who need it (borrowers) and provide safety, payments and risk protection along the way.",
 ["Depository: commercial banks, credit unions, savings and loans","Non-depository: insurance companies, brokerages, investment banks, mutual fund companies, pension funds","Federal Reserve: the central bank; FDIC and NCUA insure deposits up to $250,000","Investment banks underwrite new stocks and bonds"],
 "Match the institution to the need: \"Keep your emergency fund at an FDIC-insured bank or NCUA-insured credit union; invest for retirement through a brokerage protected by SIPC.\"",
 ["No depositor has lost a penny of FDIC-insured funds since insurance began in 1934 (FDIC).","Silicon Valley Bank failed in March 2023 after customers tried to withdraw about $42 billion in one day (Federal Reserve)."],
 "SIPC protects you if the brokerage fails, not if the market drops.",
 "Comparison table: bank vs credit union vs brokerage (owner, insurance, best for).", [FDIC, NCUA, ("SIPC", "https://www.sipc.org")])
dd("FI:337","Financial markets are where money and risk change hands. Each market fits a different need: short-term cash, long-term growth, raw materials, currencies or protection.",
 ["Money market: debt under 1 year (T-bills, CDs, commercial paper)","Capital market: stocks and bonds (long-term)","Primary market (IPO, new issues) vs secondary market (trading afterward)","Commodities, derivatives (options, futures), foreign exchange, insurance markets"],
 "This was a 2024 and 2026 district PI. Tie each market to the client's goal: \"Your emergency fund lives in the money market, your retirement money in the capital market, and your insurance comes from the insurance market.\"",
 ["The foreign exchange market is the world's largest, trading trillions of dollars a day (Bank for International Settlements triennial survey)."],
 "T-bills are money market, not capital market, because they mature in a year or less.",
 "Ladder diagram: time horizon (short to long) matched to markets and products.", [INV, TD])
dd("FI:573","Convergence is when firms from different financial sectors combine or sell each other's products. Consolidation is when firms in the same sector merge. Both create bigger, broader companies.",
 ["Convergence: bank + insurer + brokerage (one-stop shopping, bancassurance)","Consolidation: bank buys bank","Made legal by the Gramm-Leach-Bliley Act (1999), which repealed parts of Glass-Steagall","Pros: economies of scale, convenience, more products. Cons: less competition, too-big-to-fail risk, culture and system clashes"],
 "Weigh it for the client: \"Partnering with an insurer adds services members want, but we'd pilot it first and keep members' data protected.\"",
 ["Citicorp and Travelers merged in 1998 to form Citigroup (Federal Reserve History).","Capital One completed its acquisition of Discover in May 2025 (Capital One).","FDIC-insured institutions fell from more than 14,000 in the mid-1980s to fewer than 4,500 (FDIC)."],
 "Different sectors = convergence; same sector = consolidation.",
 "Venn diagram: banking, insurance, investing, with the overlap labeled convergence.", [("Federal Reserve History", "https://www.federalreservehistory.org")])
dd("FI:574","The economy and financial markets move together. Growth, inflation, interest rates and unemployment change company profits and investors' moods, which move stock and bond prices.",
 ["Business cycle: expansion, peak, contraction, trough","Higher interest rates: bond prices fall, borrowing slows, stocks often wobble","Inflation erodes purchasing power; the Fed raises rates to fight it","Defensive sectors (utilities, groceries) hold up in recessions; cyclical sectors swing"],
 "Use today's numbers, with the date: \"The Fed raised rates to 3.75%-4.00% in September 2026 because inflation was running about 3.7%, so safe savings pay about 4% right now.\"",
 ["Unemployment was 4.1% in October 2026 (Bureau of Labor Statistics).","The Fed held its target range at 3.75%-4.00% on Oct. 28, 2026 (Federal Reserve).","The S&P 500 fell about 37% in 2008 and recovered for investors who stayed in (S&P Dow Jones Indices)."],
 "When rates rise, existing bond prices fall, not rise.",
 "Line chart: interest rates rising while bond prices fall (two lines crossing).", [FED, ("Bureau of Labor Statistics", "https://www.bls.gov")])
dd("FI:575","Financial globalization means money, investment and financial firms move across borders. It brings growth and diversification, but also currency risk and faster spread of crises.",
 ["Exchange rates: a strong dollar makes U.S. exports pricier and imports cheaper","Emerging markets: higher growth, more volatility","Home bias: investing only in your own country","Contagion: the 2008 crisis spread worldwide; ADRs let U.S. investors buy foreign stocks"],
 "Recommend measured international exposure: \"A slice of international index funds diversifies you, because foreign markets don't always move with the U.S.\"",
 ["U.S. companies make up roughly 60% of global stock market value, so a U.S.-only portfolio skips about 40% of the world (MSCI All Country World Index)."],
 "Political uncertainty usually weakens a country's currency.",
 "World map sketch or pie: U.S. vs international share of global stock value.", [INV])
dd("FI:274","Investors learn about securities from company filings, annual reports, financial news and data services. The most reliable sources are the company's own audited filings.",
 ["SEC filings on EDGAR: 10-K (annual), 10-Q (quarterly), 8-K (major events within 4 business days), proxy statement","Annual report and prospectus","Financial news and data: Wall Street Journal, Bloomberg, Yahoo Finance","Analyst reports and ratings agencies (Moody's, S&P, Fitch)"],
 "Teach the client to verify: \"Before buying any stock a friend recommends, read its latest 10-K on the SEC's free EDGAR site.\"",
 ["EDGAR gives free public access to corporate filings (SEC)."],
 "Unexpected events (CEO resigns, merger) = 8-K, not 10-K.",
 "Table: filing, how often, what it tells you.", [EDGAR, INV])
dd("FI:275","A stock table summarizes a stock's trading: price range, dividends, valuation and volume. Reading it tells you how a stock has behaved and how the market values it.",
 ["52-week high/low: volatility","Dividend and yield %: income (yield = annual dividend ÷ price)","P/E ratio: price ÷ earnings per share","Volume, open, close, net change"],
 "Use it in a client conversation: \"This stock's 52-week range is wide, so it swings a lot, which may not fit your short timeline.\"",
 ["A blank dividend column means the company doesn't currently pay a dividend."],
 "Yield goes down when price goes up (same dividend, higher price).",
 "Annotated mini stock table with each column labeled.", [INV])
dd("FI:630","The statement of changes in equity shows why the owners' stake grew or shrank during a period: profits kept, new investment, dividends paid and stock bought back.",
 ["Beginning equity + net income + new stock issued − dividends − buybacks = ending equity","Retained earnings: profits kept in the business","Links the income statement to the balance sheet","Dividends reduce equity but are not an expense"],
 "Explain it as a story: \"You earned $80,000, paid yourself $30,000 in draws and kept $50,000 in the business, so your equity grew $50,000.\"",
 ["Public companies report it in their 10-K alongside the other financial statements (SEC EDGAR)."],
 "Dividends appear on the equity statement, not the income statement.",
 "Waterfall bars: beginning equity, plus profit, minus dividends, ending equity.", [EDGAR])
dd("FI:238","Time value of money means a dollar today is worth more than a dollar later because it can earn interest. You calculate future value to see growth and present value to see what you need today.",
 ["FV = PV × (1 + i)^n; PV = FV ÷ (1 + i)^n","Simple interest = principal × rate × time","Rule of 72: years to double ≈ 72 ÷ rate","Compounding frequency matters; annuities are equal regular payments"],
 "Do one quick calculation out loud: \"$10,000 at 4% for one year is $10,400. Leave it at 0.25% and you get $10,025.\" Judges remember numbers.",
 ["$200 a month from age 22 to 65 at 8% grows to about $895,000; starting at 32 gives about $387,000 (future value of an annuity)."],
 "PV formula divides; FV formula multiplies. n is the number of periods.",
 "Line chart: start now vs wait 10 years, two growth curves.", [INV])
dd("FI:658","Managerial accounting sorts costs by how they behave and whom they belong to, so managers can make better decisions.",
 ["Direct (traceable to one product) vs indirect/overhead (shared)","Fixed (same at any volume) vs variable (changes with volume)","Sunk cost: already spent, ignore it","Differential cost: the difference between two options; opportunity cost: value of the option given up"],
 "Use cost types to cut through emotion: \"The $200,000 already spent is a sunk cost. The question is whether the next $80,000 earns more than $80,000.\"",
 ["Classic indirect cost: electricity for a factory that makes several products."],
 "Sunk costs should not affect future decisions.",
 "Two stacked bars: fixed vs variable costs at low and high volume.", [])
dd("FI:659","Marginal analysis compares the extra benefit of one more unit or one change with its extra cost. Keep going while the extra benefit is bigger.",
 ["Marginal benefit vs marginal cost","Used for pricing, staffing, production, extra hours","Ignore sunk costs","Diminishing returns: each added unit eventually adds less"],
 "\"Staying open one more hour brings in about $300 and costs $120 in wages and power, so the extra hour adds $180.\"",
 ["The law of diminishing returns is a core economics principle taught in every introductory course."],
 "Compare the added (marginal) amounts, not the totals.",
 "Two lines: marginal benefit falling, marginal cost rising, crossing at the best level.", [])
dd("FI:660","Managerial accounting creates financial information for people inside the company to plan, control and decide. It isn't bound by GAAP and looks forward.",
 ["Internal users vs financial accounting's external users","Budgets, cost analysis, performance reports","Flexible format, frequent, forward-looking","Not required by law"],
 "\"Your tax return and bank statements look backward. A monthly managerial report shows you which service lines actually make money.\"",
 ["GAAP, set by FASB, governs financial accounting for external reporting, not internal managerial reports (FASB)."],
 "Financial accounting records history for outsiders; managerial accounting interprets data for insiders.",
 "Two-column comparison: financial vs managerial accounting.", [FASB])
dd("FI:661","Variance analysis compares what you planned with what actually happened, then asks why, so you can fix problems and plan better next time.",
 ["Variance = actual − budget","Favorable (revenue above or costs below plan) vs unfavorable","Price vs volume variances","Management by exception: investigate only significant gaps"],
 "\"Labor ran 15% over budget for three months. Variance analysis shows the estimate was too low, so we'll re-estimate hours for future projects.\"",
 ["Variance analysis is a standard managerial-accounting tool covered in the MBA Research LAPs that DECA exams cite (MBA Research)."],
 "Comparing forecast to actual = variance analysis.",
 "Grouped bars: budget vs actual by category, gaps highlighted.", [MBA])
dd("FI:662","Cost accounting budgets plan the cost of producing a product or service, broken into materials, labor and overhead, so managers can control costs.",
 ["Direct materials budget","Direct labor budget","Manufacturing overhead budget","Standard costs as benchmarks"],
 "\"Building a labor budget by job shows which jobs run over, so we can bid them correctly next time.\"",
 ["Cost accounting captures variable, fixed and operating costs of production."],
 "Cost accounting's purpose: find the causes of variances and improve efficiency.",
 "Stacked bar: materials, labor, overhead per unit.", [])
dd("FI:663","Cost allocation assigns shared costs, like rent or IT, to products or departments using a fair driver, so each one's true cost and profit are clear.",
 ["Cost objects: products, departments, regions","Cost drivers: square footage, machine hours, headcount","Activity-based costing (ABC): allocate by activities actually used","Better pricing and profitability decisions"],
 "\"We'd allocate rent by square footage, so the department using 40% of the space carries 40% of the rent.\"",
 ["Activity-based costing gives a more accurate picture of each product's profitability than volume-based allocation."],
 "Allocation is for indirect costs; direct costs are traced, not allocated.",
 "Pie chart: rent split by department square footage.", [])
dd("NF:124","Advanced database skills mean structuring, querying and analyzing data across related tables to answer business questions and spot problems like fraud.",
 ["Relational tables linked by primary and foreign keys","Queries with multiple criteria; filters; normalization reduces duplicates","First step of a multi-table query: pinpoint the question","Benford's Law tests measured data for fabrication"],
 "\"We'd query vendor and employee tables for matching addresses, which catches fake vendors in seconds.\"",
 ["In many naturally occurring data sets, about 30% of numbers start with 1 and under 5% start with 9 (Benford's Law)."],
 "Benford's Law doesn't work on assigned numbers like phone numbers or IDs.",
 "Simple diagram: two tables joined by a key.", [])
dd("PD:152","The finance industry offers careers in banking, accounting, corporate finance, insurance, investments and personal financial planning, many with strong pay and growth.",
 ["Banking: teller, loan officer, branch manager","Accounting: CPA, auditor, controller","Investments: analyst, broker, portfolio manager","Insurance: agent, underwriter, actuary, claims adjuster; planning: CFP"],
 "If the judge plays a student or HR director, map interests to roles and the credential for each.",
 ["Personal financial advisors and financial analysts each earned a median of roughly $100,000 a year in recent data (BLS Occupational Outlook Handbook)."],
 "Actuaries calculate risk with statistics; underwriters decide whether to accept it.",
 "Career map: four branches with roles and credentials.", [BLS])
dd("PD:153","Relationships drive finance careers: networking brings referrals, mentors and opportunities, and clients come mostly through trust and word of mouth.",
 ["Professional associations (AICPA, CFA Institute, Financial Planning Association)","Conferences, seminars, community events","Referral systems and follow-up","Social media used professionally (LinkedIn), within compliance rules"],
 "\"We'd host free money workshops for local business owners. It builds trust and brings referrals.\"",
 ["Many finance credentials, such as the CFP, require continuing education, which also builds professional networks (CFP Board)."],
 "The main networking benefit for a planner is meeting potential clients and contacts.",
 "Network web: you in the center, connections around.", [])
dd("PD:213","Corporate governance is how a company is directed and controlled. Strong governance protects owners, prevents fraud and makes investors willing to pay more.",
 ["Board oversight, accountability, transparency, ethics","Protects shareholders and stakeholders","Lowers the cost of capital","Failures: Enron, WorldCom, FTX"],
 "\"Investors pay a premium for companies they trust. Independent directors and an audit committee are how you earn that trust before an IPO.\"",
 ["Sarbanes-Oxley (2002) was passed after the Enron and WorldCom scandals (SEC).","WeWork withdrew its 2019 IPO after investors raised governance concerns (SEC filings, news coverage)."],
 "Poor governance lowers investor confidence.",
 "Org chart: shareholders → board (committees) → CEO → management.", [("SEC", "https://www.sec.gov")])
dd("PD:301","Every employee helps the company meet its governance goals by following the code of conduct, keeping accurate records, avoiding conflicts and reporting wrongdoing.",
 ["Follow policies and the code of conduct","Accurate records and honest reporting","Disclose conflicts of interest","Speak up: whistleblower protections under SOX and Dodd-Frank"],
 "\"Governance isn't just the board. A teller who reports a suspicious transaction is doing governance.\"",
 ["The SEC whistleblower program pays awards of 10% to 30% of sanctions over $1 million (SEC)."],
 "Employees who see how their work connects to company goals feel more purpose.",
 "Pyramid: board at top, managers, every employee at the base.", [("SEC Whistleblower Program", "https://www.sec.gov/whistleblower")])
dd("PD:302","Governance structures change with company size, ownership, laws, industry rules and events like scandals or going public.",
 ["Internal factors: ownership, size, culture, bylaws","External factors: laws (SEC, SOX), stock exchange rules, regulators, activist investors","Going public brings the biggest change","Scandals and crises trigger reform"],
 "\"Going public means SEC reporting, Sarbanes-Oxley controls and exchange listing rules, so the board needs independent directors.\"",
 ["NYSE and Nasdaq require a majority of independent directors and an independent audit committee (exchange listing rules)."],
 "Government regulation is an external governance mechanism.",
 "Two columns: internal vs external factors.", [])
dd("PD:214","A well-governed company has an independent board, key committees, honest reporting, internal and external audits, and a strong ethics program.",
 ["Board of directors with independent members; separate CEO and chair","Audit, compensation and nominating committees","Internal audit and an independent external audit","Transparency, code of conduct, whistleblower hotline"],
 "Recommend a checklist and a timeline: \"Months 1-6: add two independent directors. Months 6-12: form an audit committee.\"",
 ["Sarbanes-Oxley Section 404 requires management to report on internal control over financial reporting (SEC)."],
 "External audits focus on whether financial statements are accurate.",
 "Org chart with committees under the board.", [COSO])
dd("PD:303","Governance adds approvals, oversight and reporting to management decisions. It can slow decisions slightly but makes them more accountable and less risky.",
 ["Board approval for major decisions (acquisitions, big spending)","Delegation of authority limits","Reporting and accountability","Balance speed with control"],
 "\"Requiring board approval over $5 million adds a week, but it stops a single executive from betting the company.\"",
 ["Governance processes put checks on management's biggest decisions to reduce risk."],
 "Governance doesn't take away management's daily decisions; it oversees the big ones.",
 "Flowchart: decision → size check → manager approves or board approves.", [])
dd("FM:002","Financial-information management collects, stores, analyzes and reports financial data so leaders make sound decisions. Accurate information is the whole point.",
 ["Data → information → decisions","Benchmarking against competitors","Systems: accounting software, ERP","Mergers often disrupt FIM systems"],
 "\"One clean financial system means you see actual vs budget every week instead of guessing.\"",
 ["Cloud accounting tools such as QuickBooks Online and Xero connect to bank feeds and update reports automatically (vendor information)."],
 "FIM's main purpose: accurate information for decision-making.",
 "Flow: data sources → system → reports → decisions.", [])
dd("FM:003","Ethics in financial information means honest, accurate and confidential handling of data, even under pressure, because investors, lenders and clients rely on it.",
 ["Accuracy, objectivity, confidentiality","Conflicts of interest: disclose and step aside","Audit trails and stewardship","Pressure to manipulate numbers is the classic dilemma"],
 "\"We'd refuse to record a personal expense as a business expense and explain it would misstate the records.\"",
 ["Enron's 2001 collapse also brought down its auditor, Arthur Andersen (SEC, Justice Department)."],
 "The ethical move with a conflict of interest is to disclose it and remove yourself.",
 "Decision tree: is it accurate? legal? would I be OK if it were public?", [])
dd("FM:011","Technology automates and secures financial-information work: cloud accounting, ERP, automated data capture, analytics and AI, with cybersecurity to protect it.",
 ["Cloud accounting, ERP, bank feeds","Automated data collection reduces entry errors","AI and machine learning for anomalies and forecasts","Cybersecurity: firewalls, encryption, multifactor authentication, backups"],
 "\"Automating invoice entry cuts typos, and multifactor authentication protects the cloud system.\"",
 ["Microsoft reports that multifactor authentication blocks over 99% of automated account-compromise attacks (Microsoft security research)."],
 "The main downside of cloud systems is cybersecurity risk.",
 "Before/after process: manual steps vs automated steps.", [])
dd("FM:013","Budgeting applications build budgets, compare them to actual results and run what-if scenarios, so managers can plan and react quickly.",
 ["Spreadsheets and budgeting software","Cash flow budget spots shortfalls","What-if (scenario) analysis","Bottom-up vs top-down budgeting; flexible vs static"],
 "\"In the budget model, a rainy summer cuts revenue 20%. Here's the cash reserve that covers it.\"",
 ["Budgeting software can model unlimited scenarios to show the impact of decisions."],
 "A static budget doesn't adjust when activity changes; a flexible one does.",
 "Three bars: best, expected, worst case.", [CFPB])
dd("FM:014","Financial analysis applications turn statements into insight with ratios, trends and comparisons, so you can judge liquidity, profitability and risk.",
 ["Liquidity: current ratio, acid-test","Leverage: debt-to-equity","Profitability: net margin, ROA, ROE","Horizontal (over time) and vertical (as % of a base) analysis"],
 "Calculate one ratio in the roleplay: \"Your current ratio is $90,000 ÷ $60,000 = 1.5, healthy, but it was 2.0 last year, so watch it.\"",
 ["Lenders commonly look for a debt service coverage ratio of about 1.25 or higher (common commercial lending standards)."],
 "Debt-to-equity measures risk from borrowing, not profitability.",
 "Line chart: a key ratio over 3 years with a target line.", [EDGAR])
dd("FM:009","Analyzing customer financial information means judging whether a person or business can handle credit, using credit reports, ratios and payment history.",
 ["Five Cs of credit","Credit reports and scores; debt-to-income ratio","Business customers: financial statements and ratios","Credit standards decide who gets credit"],
 "\"Your debt-to-income is 35%. Getting it under 36% and your score above 700 opens better mortgage rates.\"",
 ["FICO scores weigh payment history about 35% and amounts owed about 30% (myFICO)."],
 "Capacity = ability to repay; character = trustworthiness; collateral = pledged assets.",
 "Gauge chart: debt-to-income with green, yellow, red zones.", [ACR])
dd("FM:016","Financial information also drives non-traditional tools: lean (cut waste), Six Sigma (cut defects), activity-based costing (true costs) and sustainability reporting (environmental and social impact).",
 ["Lean: maximize customer value, minimize waste","Six Sigma: DMAIC (define, measure, analyze, improve, control)","Activity-based costing: overhead by activities used","Sustainability/ESG reporting; ISSB standards (IFRS S1 and S2, 2023)"],
 "\"A lean review of the loan process cut 14 steps to 6, saving two days per application.\"",
 ["The International Sustainability Standards Board issued IFRS S1 and S2 in 2023 (IFRS Foundation)."],
 "Lean = waste; Six Sigma = defects and variation.",
 "Before/after process map with removed steps crossed out.", [("IFRS Foundation", "https://www.ifrs.org")])
dd("RM:041","Ethical risk management means being honest about risks, not hiding them from customers or regulators, and not cutting corners that put people at risk.",
 ["Disclose risks honestly","Don't shift risk to customers through deception","Cutting quality to save money raises safety and reputation risk","Breach notification and transparency"],
 "\"If there's a data breach, notify customers quickly and help them protect their accounts. Hiding it multiplies the damage.\"",
 ["Every U.S. state has a data breach notification law (National Conference of State Legislatures)."],
 "Hiding safety flaws in fine print is unethical even if it reduces liability on paper.",
 "Scale drawing: short-term savings vs long-term risk.", [])
dd("RM:042","Technology helps measure, predict and reduce risk: data analytics, machine learning fraud detection, risk modeling and cybersecurity.",
 ["Machine learning flags unusual transactions","Risk modeling simulates outcomes (Monte Carlo)","Backups, disaster recovery, incident-response drills","Cybersecurity is itself a top risk"],
 "\"Real-time fraud scoring stops a suspicious transfer before it leaves the account.\"",
 ["Consumers reported losing about $12.5 billion to fraud in 2024 (FTC)."],
 "Technology supports risk decisions; people still decide.",
 "Risk matrix with cyber risk plotted high-likelihood, high-impact.", [("FTC", "https://www.ftc.gov")])
dd("RM:043","Risk management has legal sides: compliance with safety, privacy and financial laws, contracts that assign responsibility, and insurance regulation.",
 ["Sarbanes-Oxley internal controls; OSHA workplace safety","Contracts: indemnification, limitation of liability, waivers","Insurance law; captive insurance","Privacy and data-breach laws"],
 "\"We'd put a clear liability clause in the partnership agreement so each partner's responsibilities are written down.\"",
 ["Sarbanes-Oxley requires CEOs and CFOs to certify financial reports (SEC)."],
 "SOX applies to public companies' internal controls over financial reporting.",
 "Table: risk, law or contract that addresses it.", [("OSHA", "https://www.osha.gov")])
dd("RM:058","Risk control reduces how often or how badly losses happen. Internal controls handle risks inside the company; external risks like the economy must be planned for, not prevented.",
 ["Internal controls: separation of duties, dual approval, reconciliations, mandatory vacations","External risks: inflation, recessions, disasters, new laws","Preventive vs detective controls","Insurance transfers what can't be controlled"],
 "\"No one person should approve, pay and reconcile. Splitting those duties would have stopped this fraud.\"",
 ["Organizations lose an estimated 5% of revenue to fraud each year (ACFE Occupational Fraud Report)."],
 "A change in inflation is external and largely uncontrollable.",
 "Flowchart showing duties split among three people.", [COSO, ("ACFE", "https://www.acfe.com")])
dd("RM:062","Enterprise risk management looks at all of a company's risks together, across every department, against how much risk the company is willing to take.",
 ["Risk appetite and tolerance","Risk inventory (register) with likelihood, impact and owner","Strategic, operational, financial, compliance, reputational risks","COSO ERM framework (2017); limitation: relies on management's estimates"],
 "\"Today each department manages its own risks. ERM puts them on one risk register so leaders see how a recession and a cyberattack could hit at once.\"",
 ["COSO's Enterprise Risk Management framework (2017) is a widely used ERM standard (COSO)."],
 "ERM = integrated, organization-wide; traditional = silos.",
 "Risk matrix (likelihood × impact) with top risks plotted.", [COSO])

# =================== TIER 1: PIs FTDM CASES USE MOST ===================
dd("FI:270","People save for safety and short-term goals and invest for long-term growth. Money that sits idle loses buying power to inflation, so starting early matters most.",
 ["Pay yourself first; automate it","Emergency fund of 3-6 months before investing beyond the match","Compound growth: time is the biggest driver","Inflation erodes idle cash"],
 "This was a 2024 and 2026 district PI. Make it personal: \"Your $10,000 in a 0.25% account loses about $345 of buying power a year with inflation near 3.7%. Automating $300 a month into an index fund fixes that.\"",
 ["The S&P 500 has compounded at roughly 10% a year since 1928, about 7% after inflation (NYU Stern / Damodaran data).","Inflation was 3.7% for the 12 months through September 2026 (BLS)."],
 "Saving and investing do different jobs: safety vs growth.",
 "Line chart: start now vs start in 10 years.", [INV, NGPF])
dd("FI:077","Common investments range from safe and low-return (savings, CDs, Treasuries) to riskier and higher-return (bonds, stocks, real estate). Diversified funds mix them.",
 ["Stocks (ownership), bonds (loans), mutual funds and ETFs (baskets)","Index funds: low cost, broad diversification","CDs, Treasury bills, money market funds: safe and short-term","Real estate and REITs; risk-return tradeoff"],
 "Match investments to goals: \"Emergency fund in high-yield savings, house down payment in CDs, retirement in a target-date index fund.\"",
 ["Fidelity, Schwab and Vanguard offer automatic recurring investments; Fidelity and Schwab offer fractional shares (company sites)."],
 "Higher potential return always comes with higher risk.",
 "Risk-return staircase from savings to stocks.", [INV, TD])
dd("FI:571","Insurance needs depend on what you'd lose and who depends on you. Most families need health, auto, home or renters, life, disability and liability coverage.",
 ["Life: term is cheaper; 10-12× income is a common guideline","Disability replaces about 60% of income","Umbrella for extra liability","Review at life events: marriage, baby, house, business"],
 "This was a 2025 and 2026 district PI. Find the gaps: \"You have health, auto and home, but nothing replaces your income if one of you dies or can't work, so we'd add term life and disability.\"",
 ["About 1 in 4 of today's 20-year-olds will become disabled before retirement age (Social Security Administration)."],
 "Term life has no cash value; whole life does and costs much more.",
 "Coverage checklist chart: have vs need, gaps circled.", [III, ("NAIC (state insurance regulators)", "https://www.naic.org")])
dd("FI:081","Insurance pools risk: many people pay premiums so the few who suffer a covered loss get paid. You transfer a risk you can't afford to carry alone.",
 ["Premium, deductible, coverage limit, claim, beneficiary","Higher deductible = lower premium","Pure risk is insurable; speculative risk is not","Insurers spread risk across many policyholders"],
 "\"Raising your deductible from $500 to $1,000 lowers your premium, and your emergency fund covers the difference.\"",
 ["Insurance transfers risk from the individual to the insurer (Insurance Information Institute)."],
 "Deductible = what you pay first; premium = what you pay for the policy.",
 "Diagram: many premiums flow into a pool, one claim flows out.", [III])
dd("FI:569","Retirement planning means saving in tax-advantaged accounts early, investing for growth, and planning income from savings and Social Security.",
 ["401(k) with employer match; traditional vs Roth","IRAs; catch-up contributions after 50","Social Security: claim between 62 and 70","Target-date funds; withdrawal planning"],
 "\"Contribute enough to get the full match first. It's an instant 100% return.\"",
 ["2027 401(k) limit $25,500, catch-up $8,500, ages 60-63 catch-up $11,750; IRA $7,500 (IRS Notice 2026-66).","Social Security benefits rise 3.6% in January 2027 (SSA, Oct. 14, 2026)."],
 "Roth = pay tax now, tax-free later; traditional = deduction now, taxed later.",
 "Bar chart: balance at 65 for starting at 25, 35, 45.", [SSA, IRS])
dd("FI:831","College can be paid for with savings, scholarships, grants, work-study and loans. Planning early lowers the debt.",
 ["529 plans: tax-free for qualified education costs","FAFSA unlocks grants, work-study, federal loans","Federal vs private loans","Unused 529 money: change beneficiary or roll up to $35,000 to a Roth IRA (SECURE 2.0)"],
 "\"Open a 529 at birth. $150 a month at 6% grows to about $58,000 by 18.\"",
 ["Children born 2025-2028 can receive a $1,000 federal seed deposit in a Trump Account (2025 tax law; IRS Form 4547)."],
 "Grants don't need to be repaid; loans do.",
 "Stacked bar: how college gets paid (grants, savings, work, loans).", [SAID, ("SEC Investor.gov on 529 plans", "https://www.investor.gov")])
dd("FI:065","Financial goals turn wishes into plans. SMART goals are specific, measurable, achievable, relevant and time-bound, and split into short, medium and long term.",
 ["SMART goals","Short (under 1 year), medium (1-5), long (over 5)","Prioritize: protect, then save, then grow","Review and adjust"],
 "\"Instead of 'save more,' let's set: $30,000 emergency fund in 18 months by saving $1,700 a month.\"",
 ["Writing down specific goals is standard practice in financial planning (CFPB 'Your Money, Your Goals' toolkit)."],
 "A house down payment in four years is a medium-term goal.",
 "Timeline with goals placed at 1, 3 and 10 years.", [CFPB])
dd("FI:066","A budget is a plan for income and spending that makes sure saving happens. It separates fixed from variable costs and needs from wants.",
 ["50/30/20 guideline","Fixed vs variable expenses","Zero-based budgeting: every dollar assigned","Track, compare, adjust monthly"],
 "\"On $6,000 take-home: $3,000 needs, $1,800 wants, $1,200 to savings and debt.\"",
 ["The 50/30/20 guideline was popularized in 'All Your Worth' (2005) by Elizabeth Warren and Amelia Warren Tyagi."],
 "Groceries are variable; rent is fixed.",
 "Pie chart: 50/30/20 split with dollar amounts.", [CFPB, NGPF])
dd("FI:062","Time value of money: a dollar today beats a dollar tomorrow because today's dollar can earn interest. Waiting has a real cost.",
 ["Compound vs simple interest","Future value and present value","Rule of 72","Opportunity cost of delay"],
 "This was a 2024 district PI. \"Waiting six months to move $10,000 into a 4.10% certificate gives up about $190.\"",
 ["At 8%, money doubles in about 9 years (Rule of 72)."],
 "TVM says money today is worth more, not less.",
 "Two growth lines: invest now vs later.", [INV])
dd("FI:002","Credit lets you buy now and pay later. Used well it builds a credit history that lowers future borrowing costs; used badly it costs a lot in interest.",
 ["Purposes: big purchases, emergencies, building history","Five Cs of credit","Secured vs unsecured; installment vs revolving","Cost: interest and fees (APR)"],
 "Judges asked about this in 2026: \"Use credit cards like debit: autopay the full statement balance and keep balances under 30% of the limit.\"",
 ["Average interest on credit card accounts charged interest has been above 20% in recent years (Federal Reserve G.19)."],
 "Credit's purpose is buying now and paying later, not free money.",
 "Line chart: debt growth paying minimums vs full balance.", [CFPB])
dd("FI:071","Using credit wisely means borrowing only what you can repay, paying on time, keeping balances low and protecting your credit history.",
 ["Pay on time (35% of FICO)","Keep utilization under 30% (under 10% is best)","Keep old accounts open","Don't open many accounts at once"],
 "\"Autopay every bill and keep your card balance under $600 on a $2,000 limit.\"",
 ["FICO weights: payment history 35%, amounts owed 30%, length 15%, new credit 10%, mix 10% (myFICO)."],
 "Closing your oldest card can lower your score.",
 "Pie chart of FICO score factors.", [CFPB, ("myFICO", "https://www.myfico.com")])
dd("FI:072","Checking your credit history means reviewing your reports from all three bureaus, catching errors or fraud, and disputing mistakes for free.",
 ["Equifax, Experian, TransUnion","Free weekly reports at AnnualCreditReport.com","Fair Credit Reporting Act: bureaus generally investigate disputes within 30 days","Most negative items stay 7 years; bankruptcies up to 10"],
 "\"Pull all three reports tonight and dispute the account you don't recognize.\"",
 ["AnnualCreditReport.com is the official free source for all three reports (FTC)."],
 "Credit repair companies can't legally remove accurate negative information.",
 "Checklist: personal info, accounts, inquiries, negatives.", [ACR, CFPB])
dd("FI:568","Controlling debt means knowing what you owe, keeping payments affordable and paying down high-interest debt first.",
 ["Debt-to-income ratio (under about 36% is a common guideline)","Avalanche (highest rate first) vs snowball (smallest balance first)","Consolidation only if the rate is lower and spending stops","Call issuers to request lower rates"],
 "\"Minimums on everything, then every extra dollar to the 29% card.\"",
 ["Paying only minimums on high-APR cards can take many years; statements must show how long (CARD Act, 2009)."],
 "Avalanche saves the most interest; snowball builds motivation.",
 "Bar chart: balances by card, ordered by interest rate.", [CFPB])
dd("FI:782","The cost of credit includes interest and fees. APR shows the yearly cost so you can compare offers.",
 ["APR (cost of borrowing) vs APY (earnings on savings)","Finance charge = interest + fees","Longer terms lower payments but raise total interest","Truth in Lending Act requires disclosure"],
 "\"$16,500 at 24% costs about $330 a month in interest alone.\"",
 ["The Truth in Lending Act requires lenders to disclose the APR and finance charges (CFPB)."],
 "The finance charge includes fees, not just interest.",
 "Two bars: total paid on a 3-year vs 6-year car loan.", [CFPB])
dd("FI:073","Identity theft is when someone uses your personal information to open accounts or steal money. Prevention and fast response limit the damage.",
 ["Credit freezes are free at all three bureaus","Multifactor authentication, unique passwords","Phishing and imposter scams: banks never ask for codes","If it happens: IdentityTheft.gov, freeze credit, report to bank and police"],
 "\"Hang up and call the number on the back of your card. Your bank will never ask for a passcode.\"",
 ["People 60 and older reported losing about $4.9 billion to online fraud in 2024 (FBI IC3)."],
 "A credit freeze stops new accounts; it doesn't affect your existing cards.",
 "Flowchart: suspect fraud → freeze → report → monitor.", [FTC, CFPB])
dd("FI:572","Estate planning decides who gets your property and who cares for your children if you die, and who decides for you if you can't.",
 ["Will: property and guardian for minor children","Beneficiary designations on accounts and insurance override the will","Trusts; power of attorney; health care directive","Probate; federal estate tax applies only to very large estates"],
 "\"New parents need a will that names a guardian. Without one, a court decides.\"",
 ["The federal estate tax exemption is $15 million per person for 2026 under the 2025 tax law (IRS)."],
 "Beneficiary forms beat what the will says for those accounts.",
 "Diagram: assets flowing to heirs through will, beneficiary forms, trust.", [IRS])
dd("FI:562","Net worth is what you own minus what you owe. Tracking it shows whether your financial life is moving forward.",
 ["Assets: cash, investments, home, car","Liabilities: mortgage, loans, card balances","Net worth = assets − liabilities","Track yearly"],
 "\"Your net worth is $7,000 today. Paying off the card and investing $300 a month could push it past $20,000 in two years.\"",
 ["Net worth is the personal equivalent of a company's equity on the balance sheet."],
 "Net worth can be negative when debts exceed assets.",
 "Two-column balance sheet: assets vs liabilities.", [CFPB])
dd("FI:061","Income comes from work (wages, salary, tips, commissions) and from money working for you (interest, dividends, rent, capital gains). Benefits are part of compensation too.",
 ["Earned vs investment (passive) income","Gross vs net pay","Benefits: health insurance, 401(k) match, paid time off","Self-employment income"],
 "\"Your 4% 401(k) match is part of your pay. Not taking it is turning down a raise.\"",
 ["Employees pay 7.65% in FICA taxes: 6.2% Social Security (up to the wage base) plus 1.45% Medicare (SSA, IRS)."],
 "Interest and dividends are investment income, not earned income.",
 "Stacked bar: salary plus benefits = total compensation.", [IRS])
dd("FI:067","Taxes are paid on income, purchases, property and payroll. Understanding them helps you keep more of what you earn.",
 ["Progressive federal income tax brackets (10% to 37%)","Payroll (FICA), sales, property taxes","Deductions lower taxable income; credits lower tax directly","Withholding and refunds"],
 "\"A tax credit is worth more than a deduction of the same size because it cuts your tax dollar for dollar.\"",
 ["2026 standard deduction: $16,100 single, $32,200 married filing jointly (IRS).","The Social Security wage base is $184,500 for 2026 and $192,300 for 2027 (SSA)."],
 "A credit reduces tax owed; a deduction reduces taxable income.",
 "Staircase chart of tax brackets.", [IRS])
dd("FI:075","Financial-services providers include banks, credit unions, brokerages, insurers, financial planners, online banks and fintech apps, each with different services and protections.",
 ["Depository institutions vs non-depository","Online banks and fintech apps","Advisors: fee-only, commission, robo-advisors","Check insurance (FDIC/NCUA/SIPC) and licensing"],
 "\"Before trusting an app, know which bank holds the money. FDIC insurance covers a bank failure, not a fintech middleman failure.\"",
 ["Customers of several fintech apps had money frozen when middleman Synapse went bankrupt in 2024 (news coverage, FDIC guidance)."],
 "Credit unions are member-owned and not-for-profit.",
 "Comparison table of providers.", [FDIC])
dd("FI:076","Choosing a financial-services provider means comparing safety, fees, rates, convenience, services and trust.",
 ["Insurance coverage and regulation","Fees, rates, minimums","Branches, apps, ATM network, customer service","Reputation and complaint history (CFPB complaint database)"],
 "\"Compare three things: insured? fees? app and service? Then pick the one that fits how you bank.\"",
 ["The CFPB publishes a public consumer complaint database (CFPB)."],
 "The lowest fee isn't always best if service or safety is weak.",
 "Decision matrix: providers scored on criteria.", [CFPB])
dd("FI:579","Businesses and people need financial information to track performance, plan, borrow, invest and meet legal requirements. You can't manage what you don't measure.",
 ["Uses: decisions, budgets, loans, taxes, investor trust","Comparing forecast to actual = variance","Statements: income statement, balance sheet, cash flow","Lenders and investors require it"],
 "This was a 2025 district PI. \"The bank needs both partners' financial information to judge whether the business can repay.\"",
 ["Lenders evaluate borrowers with the five Cs of credit, all based on financial information."],
 "Financial information supports decisions; it can't guarantee profit.",
 "Flow: records → statements → decisions.", [SBA])
dd("FI:085","Accounting records, classifies, summarizes and interprets financial transactions. It's the language of business.",
 ["Accrual (when earned) vs cash basis","GAAP set by FASB; IFRS internationally","Assets = liabilities + equity","Bookkeeping vs accounting"],
 "\"Cloud accounting with bank feeds keeps your books current so you always know where you stand.\"",
 ["U.S. public companies must follow GAAP, set by FASB (SEC, FASB)."],
 "Accrual accounting records revenue when earned, not when paid.",
 "Accounting equation balance scale.", [FASB])
dd("FI:091","The cash flow statement shows cash coming in and going out from operating, investing and financing activities. Profit isn't cash.",
 ["Operating: customers, suppliers, wages","Investing: buying or selling equipment, investments","Financing: loans, owner money, dividends","Profitable businesses can still run out of cash"],
 "\"You're profitable, but customers pay in 60 days. Faster invoicing fixes the cash gap.\"",
 ["About 1 in 5 new businesses close within the first year (BLS Business Employment Dynamics); cash problems are a common cause."],
 "Buying equipment is investing; paying dividends is financing.",
 "Monthly bars of cash in vs out, with the winter gap shaded.", [SBA])
dd("FI:093","The balance sheet is a snapshot on one date of what a business owns, owes and what's left for the owners.",
 ["Assets = liabilities + owner's equity","Current vs long-term assets and liabilities","Current ratio = current assets ÷ current liabilities","Shows financial position, not profit"],
 "\"Your current ratio is 1.5, so you can cover short-term bills, but watch receivables.\"",
 ["Lenders review balance sheets to judge liquidity and leverage (SBA lending guidance)."],
 "Balance sheet = one date; income statement = a period.",
 "Two-column T: assets vs liabilities and equity.", [SBA])
dd("FI:094","The income statement shows revenue, expenses and profit or loss over a period.",
 ["Revenue − COGS = gross profit","Gross profit − operating expenses = operating income","Net income after interest and taxes","Also called the profit and loss statement"],
 "\"Revenue grew 20%, but expenses grew 30%, so profit fell. Let's find which costs jumped.\"",
 ["Public companies report income statements quarterly (10-Q) and annually (10-K) (SEC)."],
 "Cash on hand isn't on the income statement.",
 "Waterfall: revenue down to net income.", [EDGAR])
dd("FI:354","Finance in business means getting money, investing it wisely and managing day-to-day cash so the company can grow and pay its bills.",
 ["Raise funds: debt vs equity","Invest: capital budgeting","Manage working capital","Debt keeps control and interest is deductible; equity needs no repayment but shares ownership"],
 "This was a 2025 district PI (role of finance in business). \"For your bakery, finance means deciding how to pay for the oven, whether it pays off, and keeping enough cash for payroll.\"",
 ["Interest on business debt is generally tax-deductible, which lowers its after-tax cost (IRS)."],
 "Capital budgeting = long-term investment decisions.",
 "T-chart: debt vs equity pros and cons.", [SBA])
dd("FI:106","A budget is a financial plan for a future period. Businesses use it to set targets, control spending and measure results.",
 ["Static vs flexible budgets","Top-down vs bottom-up","Operating, cash and capital budgets","Compare to actual: variance analysis"],
 "This was a 2025 district PI. \"Your start-up budget covers the truck and permits; your monthly operating budget covers fuel, rent and pay.\"",
 ["Break-even units = fixed costs ÷ (price − variable cost per unit)."],
 "A static budget doesn't adjust when sales change.",
 "Pie chart of monthly operating costs, or best/expected/worst bars.", [SBA])
dd("FI:351","Ethics in accounting means accurate, objective, honest records, because owners, lenders, investors and tax authorities rely on them.",
 ["Objectivity, integrity, confidentiality","Follow GAAP","Resist pressure to manipulate","Auditors check the work"],
 "\"We'd record expenses in the right period even if it lowers this quarter's profit.\"",
 ["Sarbanes-Oxley created the PCAOB to oversee auditors of public companies (SEC)."],
 "Accountants must present objective information.",
 "Scale: pressure vs integrity.", [])
dd("FI:355","Ethics in finance means honesty, fairness and putting clients' interests first, because trust is the product finance sells.",
 ["Conflicts of interest disclosed","No misleading claims or guarantees","Confidentiality","Fair treatment of all clients"],
 "\"We'll never promise returns, and we disclose every fee in writing.\"",
 ["Wells Fargo's fake-accounts scandal led to a $3 billion settlement in 2020 (DOJ)."],
 "Guaranteeing investment returns is a red flag and unethical.",
 "Simple pledge box: three promises to the client.", [])
dd("FI:356","Finance has legal rules: disclosure for securities, consumer-credit laws, privacy laws and anti-fraud rules.",
 ["Securities must be registered and risks disclosed","Truth in Lending, Fair Credit Reporting, Equal Credit Opportunity","Gramm-Leach-Bliley privacy","Anti-fraud and anti-money-laundering"],
 "\"Before raising money from friends, talk to a lawyer. Selling ownership can be a securities offering.\"",
 ["The Securities Act of 1933 requires registration and disclosure for most securities offerings (SEC)."],
 "Companies selling securities must disclose the risks.",
 "Table: law, what it protects.", [INV])
dd("EN:039","Entrepreneurship is spotting an opportunity and taking the risk to build a business around it. Entrepreneurs accept risk for the chance at reward and independence.",
 ["Traits: initiative, risk tolerance, resilience, creativity","Risks: financial, personal, market","Small businesses create many new jobs and drive innovation","Planning: business plan, budget, financing"],
 "This was a 2025 district PI. \"Being an entrepreneur means you're the decision maker and the one carrying the risk, so a cash cushion is your safety net.\"",
 ["About half of new businesses survive five years (BLS Business Employment Dynamics)."],
 "An entrepreneur takes on the risk; an employee doesn't.",
 "Timeline: idea → plan → funding → launch → first year milestones.", [SBA])
dd("BL:003","Business ownership forms decide who owns the business, who's liable for debts, and how it's taxed.",
 ["Sole proprietorship: simplest, unlimited liability","Partnership: shared ownership; needs a written agreement","LLC: limited liability, pass-through taxes","S corp: pass-through, up to 100 shareholders; C corp: separate taxpayer, can sell stock"],
 "This was a 2025 district PI. \"For you and your friend, an LLC with an operating agreement protects your homes and spells out what happens if one of you leaves.\"",
 ["An EIN is free from the IRS; LLCs are formed with the state (IRS, SBA)."],
 "Sole proprietors and general partners have unlimited personal liability.",
 "Comparison table: liability, taxes, paperwork for each form.", [SBA, IRS])
dd("OP:024","Overhead (operating) costs are the ongoing costs of running a business that aren't tied to one product: rent, utilities, insurance, software, admin salaries.",
 ["Fixed vs variable overhead","Overhead affects pricing and break-even","Control: compare to budget monthly","Hidden costs: permits, fees, maintenance"],
 "This was a 2025 district PI. \"Working from a garage saves rent, but count insurance, utilities, permits and card fees.\"",
 ["Card processors typically charge a few percent per transaction (processor fee schedules)."],
 "Overhead isn't cost of goods sold.",
 "Pie chart of monthly overhead.", [SBA])
dd("SM:075","Risk management identifies what could go wrong and chooses to avoid, reduce, transfer or accept each risk.",
 ["Avoid, reduce (control), transfer (insurance, contracts), retain (accept)","Identify → assess → respond → monitor","Pure vs speculative risk","Business risks: economic, natural, human, market"],
 "This was a 2026 district case topic. \"For each risk we chose a response: insurance transfers the big ones, the emergency fund retains the small ones.\"",
 ["Insurance is the classic way to transfer risk (Insurance Information Institute)."],
 "Buying insurance = transferring risk.",
 "Risk matrix with responses written in each zone.", [III])
dd("EI:128","Trust is built by keeping promises, being honest and transparent, listening, and acting in the other person's interest over time.",
 ["Keep promises (the most important)","Transparency about fees and conflicts","Consistency and follow-through","Listening and empathy"],
 "In the 2026 case the client feared advisors serve the company. \"We'll put our fees in writing and you can verify us on BrokerCheck.\"",
 ["Advisors' licenses and disciplinary records are public on FINRA BrokerCheck (FINRA)."],
 "Keeping promises is the top way to build trust.",
 "Simple ladder: listen → explain → deliver → review.", [("FINRA BrokerCheck", "https://brokercheck.finra.org")])
dd("CR:007","Interpreting business policies means explaining the reason behind a rule in plain language and offering the customer options within it.",
 ["Explain why, not just what","Offer alternatives","Stay consistent and fair","Escalate when policy doesn't fit"],
 "This was a 2024 district PI. \"The CD has a penalty for early withdrawal because we pay a higher rate in exchange for keeping the money a full year.\"",
 ["Clear disclosure of account terms is required for deposit accounts under the Truth in Savings Act (CFPB)."],
 "\"That's our policy\" alone is poor service.",
 "Callout box: policy, reason, your options.", [CFPB])
dd("CO:039","An informational message shares facts clearly so the reader understands: short sentences, the key point first, and one call to action.",
 ["Purpose, audience, main point first","Plain language, short paragraphs, bullets","Visuals for numbers","Proofread"],
 "This was a 2024 district PI (a bank flyer). \"Headline, three benefits, one example with numbers, how to sign up.\"",
 ["Federal agencies must write public documents in plain language under the Plain Writing Act of 2010."],
 "A collection letter is persuasive, not informational.",
 "Flyer layout sketch: headline, chart, 3 bullets, call to action.", [("PlainLanguage.gov", "https://www.plainlanguage.gov")])
dd("CR:010","Handling complaints well can turn an upset customer into a loyal one: listen, empathize, solve within policy and follow up.",
 ["Listen without interrupting","Acknowledge feelings","Offer solutions within policy","Follow up"],
 "\"I understand why you're frustrated. Here's what I can do right now, and I'll call you Friday to confirm it's fixed.\"",
 ["The CFPB accepts consumer complaints about financial products and forwards them to companies for response (CFPB)."],
 "Start with listening, not explaining policy.",
 "Four-step flow: listen, empathize, solve, follow up.", [CFPB])
dd("FI:830","Managing online accounts means using banking apps and websites securely: strong logins, alerts and regular checks.",
 ["Multifactor authentication, unique passwords, password manager","Transaction alerts","Check accounts weekly","Secure networks; avoid public Wi-Fi for banking"],
 "The 2026 judge asked how often to examine accounts. \"Glance at your app weekly, review statements monthly, and do a full review yearly or after big life events.\"",
 ["Multifactor authentication blocks over 99% of automated account-compromise attacks (Microsoft)."],
 "Text-message codes are weaker than authenticator apps or passkeys.",
 "Calendar strip: weekly, monthly, yearly checks.", [CFPB])
dd("FI:063","Consumer financial products come with legal rights and responsibilities for both lenders and consumers.",
 ["Truth in Lending (disclose APR), Fair Credit Reporting, Fair Debt Collection Practices, Equal Credit Opportunity","CARD Act (2009) credit card protections","Electronic Fund Transfer Act / Regulation E for unauthorized transfers","Consumer responsibility: read terms, pay on time, report fraud quickly"],
 "\"Report an unauthorized transfer right away. Federal Regulation E limits your loss when you report quickly.\"",
 ["The CFPB enforces federal consumer financial laws (CFPB)."],
 "Lenders can't deny credit based on race, sex, religion or age (Equal Credit Opportunity Act).",
 "Table: law, your right.", [CFPB])
dd("EC:083","Inflation is a rise in the general price level. It reduces what money buys, raises business costs, and pushes interest rates up.",
 ["Measured by the CPI","Hurts savers in low-rate accounts and people on fixed incomes","Businesses face higher costs and may raise prices","The Fed raises rates to fight it; its target is 2%"],
 "\"Inflation near 3.7% means prices double in about 19 years, so your savings need to earn more than that.\"",
 ["CPI rose 3.7% over the 12 months through September 2026 (BLS)."],
 "Inflation lowers purchasing power; it doesn't raise it.",
 "Bar chart: what $100 buys today vs in 10 years at 3%.", [("BLS CPI", "https://www.bls.gov/cpi")])
dd("EC:084","Interest rates are the price of money. When they rise, borrowing costs more and saving pays more; when they fall, the reverse.",
 ["The Fed sets the federal funds target","Higher rates: costlier mortgages and loans, better savings yields, lower bond prices","Lower rates: cheaper borrowing, more spending","Fixed vs variable rates"],
 "\"With mortgage rates around 7%, improving your credit score before buying could save thousands.\"",
 ["The average 30-year mortgage rate was about 7.11% in mid-November 2026 (Freddie Mac)."],
 "Rising rates help savers and hurt borrowers.",
 "Seesaw: rates up, bond prices down.", [FED, ("Freddie Mac mortgage survey", "https://www.freddiemac.com/pmms")])
dd("EC:018","The business cycle is the economy's rise and fall: expansion, peak, contraction and trough. Each phase changes what businesses and households should do.",
 ["Expansion: hiring, spending, investment rise","Contraction/recession: output and jobs fall","Recessions are officially dated by the NBER","Plan for downturns: cash reserves, flexible costs"],
 "\"Build the cash reserve during the good years so a recession doesn't force you to sell or borrow.\"",
 ["U.S. GDP grew at a 3.4% annual rate in the third quarter of 2026, according to the first estimate as reported by Reuters."],
 "Heavy investment in new plants signals producers expect spending to rise.",
 "Wave line labeled with the four phases.", [("NBER business cycle dates", "https://www.nber.org/research/business-cycle-dating")])
