# Full FTDM cases (DECA format) and quick 30-second drills. All original.
CASES = []
def case(id, area, role, judge, situation, tasks, pis, questions, model):
    CASES.append(dict(id=id, area=area, role=role, judge=judge, situation=situation, tasks=tasks, pis=pis, questions=questions, model=model))

case("ridgeline-loan","Financial Analysis","financial consultants","owner of RIDGELINE CYCLES, a bike shop",
 "RIDGELINE CYCLES has grown sales 30% in two years and the owner (judge) wants to open a second location. A bank has asked for financial statements and a clear explanation of how the expansion will be paid for. The owner is unsure whether to take a bank loan or bring in a partner who would invest money for a 30% ownership share.",
 ["Explain what the bank will look for in the business's financial statements","Compare debt financing (the loan) with equity financing (the partner)","Recommend a financing choice and explain how the owner should monitor the business after expanding"],
 ["FI:579","FI:093","FI:354","FI:002","FI:574"],
 ["What happens if sales at the new location are slower than expected?","Which single number should I watch most closely each month?"],
 ["Open with the recommendation: a bank loan, if cash flow covers the payment with room to spare, so the owner keeps 100% control.",
  "Need for financial info: the bank uses statements to judge capacity to repay and collateral (five Cs).",
  "Balance sheet: show assets, liabilities, equity. The bank checks the current ratio and debt-to-equity.",
  "Role of finance: obtain funds (debt vs equity), invest them (new location), manage working capital.",
  "Debt: keep control, interest is tax-deductible, but a fixed payment is due even in slow months. Equity: no repayment, but you give up 30% of profits and decision-making forever.",
  "Economic conditions: rising interest rates raise the loan's cost. A slowdown could hurt sales, so stress-test a 20% sales drop.",
  "Plan: monthly cash flow review, keep 3 months of loan payments in reserve, keep the current ratio above 1.5, quarterly review with the banker.",
  "Judge Q1: build a cash reserve now, start with a smaller lease, and keep a line of credit as backup.",
  "Judge Q2: operating cash flow compared with the loan payment (debt service coverage)."])

case("summit-cu-convergence","Financial Analysis","consultants hired by the board","CEO of SUMMIT CREDIT UNION",
 "SUMMIT CREDIT UNION has 40,000 members. A regional insurance agency has offered to partner so Summit can sell auto and home insurance in its branches. The CEO (judge) wants to understand the trend of convergence and consolidation in financial services, how the partnership could affect members, and what risks to consider.",
 ["Explain convergence and consolidation in the financial industry","Describe how the partnership changes the role Summit plays for its members","Recommend whether to proceed and how to manage the risks"],
 ["FI:336","FI:573","FI:337","CR:012","RM:062"],
 ["How would we know in a year whether this was a good decision?","Why shouldn't we just merge with another credit union instead?"],
 ["Recommend proceeding with a pilot partnership (bancassurance) in 2 branches for 12 months.",
  "Role of financial institutions: Summit channels members' savings into loans. Insurance adds risk protection, so members get one-stop service.",
  "Convergence = different sectors combining (credit union + insurance). Consolidation = same sector (merging with another credit union).",
  "Financial markets: insurance market vs money and capital markets. Explain where each product fits.",
  "Client responsibilities: suitability, no pressure selling, disclose that Summit earns commissions, protect member data.",
  "ERM: list the risks in one integrated view. Reputational (bad insurer service), compliance (state insurance licensing), operational (staff training), strategic.",
  "KPIs: share of members with 2+ products, member satisfaction score, complaint rate, commission revenue.",
  "Judge Q2: consolidation adds scale but doesn't add new products. Convergence meets more member needs."])

case("harbor-fraud-controls","Risk Management","risk consultants","owner of HARBOR HOME SERVICES, a plumbing company with 25 employees",
 "HARBOR HOME SERVICES recently discovered that its office manager paid $38,000 over two years to a fake vendor she secretly set up. The office manager handled all invoices, payments and bank reconciliations alone. The owner (judge) wants to know how this happened and how to prevent it.",
 ["Explain why the fraud was possible","Recommend internal controls and technology to prevent and detect future fraud","Explain how risk management should work going forward"],
 ["RM:058","RM:042","FM:014","PD:214","RM:041"],
 ["We're a small company. Can we afford all of this?","How do I rebuild trust with my other employees?"],
 ["Root cause: no separation of duties. One person approved, paid and reconciled.",
  "Internal controls: split duties (one person enters invoices, the owner approves payments, an outside bookkeeper reconciles), dual signature over $2,500, an approved-vendor list.",
  "Technology: accounting software with user permissions and audit trails. Data matching of employee addresses against vendor addresses. Bank alerts for new payees.",
  "External controls: an annual external review by a CPA, and employee dishonesty (fidelity) insurance to transfer risk.",
  "Ethics in risk management: a written code of conduct, a confidential reporting channel, and handling the case fairly and legally.",
  "Risk process: identify, assess, control, monitor. Quarterly surprise reviews.",
  "Judge Q1: most controls are free (process changes). Software costs about $50 to $100 a month, far less than the $38,000 loss.",
  "Judge Q2: explain the controls protect everyone, keep things transparent, and avoid blame."])

case("pinecrest-governance","Professional Development","governance consultants","founder and CEO of PINECREST ORGANICS, a food company planning an IPO",
 "PINECREST ORGANICS, a family-owned food company with $80 million in sales, plans to go public in two years. Right now the founder (judge) makes nearly every decision, the board is made up of three family members, and there is no internal audit function. Investment bankers say investors will demand stronger corporate governance.",
 ["Explain what corporate governance is and why investors care","Describe the components of a well-governed public company","Recommend a two-year plan to prepare Pinecrest's governance for the IPO"],
 ["PD:213","PD:214","PD:302","PD:303","BL:148"],
 ["Won't adding outside directors slow down my decisions?","What is the first thing I should do next month?"],
 ["Governance = how a company is directed and controlled. Investors pay more for companies with accountability and transparency.",
  "Components: an independent board (majority outside directors), audit committee, internal audit, external audit, code of conduct, transparent reporting, written bylaws.",
  "Factors changing governance: going public brings SEC rules, Sarbanes-Oxley internal-control reporting and stock exchange listing standards.",
  "Impact on decisions: the board approves strategy and major moves. The CEO still runs daily operations.",
  "Compliance: build a compliance function, a record-retention policy and SOX-ready controls.",
  "Plan: months 0-6 add 2 independent directors and write a code of conduct. Months 6-12 form an audit committee and hire an internal auditor. Months 12-24 do a SOX readiness test and quarterly reporting dry runs.",
  "Judge Q1: some oversight slows decisions, but it lowers risk and raises the valuation investors will pay.",
  "Judge Q2: recruit the first independent director with financial expertise to chair the audit committee."])

case("lumen-budget","Financial Analysis","accounting associates","CFO of LUMEN SPORTS, a sporting-goods retailer",
 "Department managers at LUMEN SPORTS have gone over budget for three straight quarters. Budgets are set by the CFO (judge) at the start of the year and never change, even though sales swing a lot by season. Managers say the budgets are unrealistic. The CFO wants your recommendations.",
 ["Explain why the current budget process is failing","Describe how managerial accounting tools can improve budgeting and cost control","Recommend a new process and how to measure results"],
 ["FI:106","FI:661","FI:658","FI:663","FM:013"],
 ["How do I keep managers from padding their budgets?","How often should we review the numbers?"],
 ["Root cause: a static, top-down budget doesn't flex with seasonal volume, and managers have no ownership.",
  "Switch to a flexible budget: variable costs scale with sales, fixed costs stay fixed.",
  "Variance analysis monthly: split price vs volume variances, and investigate only significant ones (management by exception).",
  "Cost types: separate fixed vs variable and direct vs indirect. Judge managers only on costs they control.",
  "Cost allocation: allocate shared costs like rent and IT by square feet or sales, and show them separately from controllable costs.",
  "Budgeting software: what-if scenarios for peak and off-season.",
  "Bottom-up budgeting with CFO review, so managers own their numbers.",
  "KPIs: budget variance within ±5%, gross margin by department.",
  "Judge Q1: compare to prior-year actuals and benchmarks, and reward accuracy, not just staying under budget."])

case("evergreen-client","Customer Relations","financial advisors","new client, a 34-year-old nurse who just inherited $60,000",
 "A client (judge) just inherited $60,000 and has come to your advisory firm. She has $8,000 in credit card debt at 22% APR, no emergency fund, and contributes nothing to her employer's 401(k), which matches 4%. A coworker told her to put everything into a hot technology stock.",
 ["Explain your responsibilities to her as finance professionals","Explain how the time value of money and different investments apply to her situation","Recommend a plan for the $60,000"],
 ["CR:012","FI:238","FI:337","FI:575","EI:134"],
 ["Why shouldn't I just buy the stock my coworker recommended?","How will you keep my information private?"],
 ["Duties: suitability, fiduciary care, disclose all fees and conflicts, confidentiality, understand her goals and risk tolerance first.",
  "Step 1: pay off the 22% card. That's a guaranteed 22% 'return'.",
  "Step 2: build a 6-month emergency fund (about $15,000) in a high-yield savings or money market account.",
  "Step 3: contribute at least 4% to the 401(k) to capture the full match, which is free money.",
  "Step 4: invest the rest in diversified, low-cost index funds, including some international exposure to avoid home bias.",
  "TVM: $30,000 at 7% for 30 years grows to about $228,000 (FV = PV × 1.07^30, about 7.6×).",
  "Herd mentality: one hot stock means concentration risk. Diversify instead.",
  "Judge Q2: privacy policy under Gramm-Leach-Bliley, encryption, and sharing nothing without her consent."])

case("crescent-data","Information Management","financial-information consultants","controller of CRESCENT LOGISTICS",
 "CRESCENT LOGISTICS keeps customer, invoice and vendor records in separate spreadsheets maintained by different departments. Records are duplicated, numbers don't match across reports, and the controller (judge) spends days each month reconciling. An auditor also recommended testing the expense data for fraud.",
 ["Explain the role of financial-information management","Recommend how to organize the data and which tools to use","Explain how the company can use data analysis to detect fraud and improve decisions"],
 ["FM:002","NF:124","FM:011","FM:003","CR:024"],
 ["What's the biggest risk of moving everything to one system?","How will this help me make better decisions, not just faster reports?"],
 ["FIM: collect, store, analyze and report accurate data so leaders can decide.",
  "Normalize: one relational database or ERP with linked tables (customers, invoices, vendors) and unique keys, so each fact is stored once.",
  "Queries and filters replace manual reconciliation.",
  "Fraud tests: Benford's Law on expense amounts (measured data), and match employee addresses against vendor addresses.",
  "Technology: automated data collection reduces entry errors. Cloud ERP brings cybersecurity risk, so use firewalls, multi-factor authentication, access permissions and backups.",
  "Ethics: audit trails, confidentiality, record-retention schedule.",
  "CRM link: customer data in one hub reveals profitable customers.",
  "Judge Q1: a data migration error or security breach. Reduce it by testing, running old and new systems in parallel for a month, and training staff."])

case("atlas-ethics","Business Law","compliance consultants","managing director of ATLAS WEALTH PARTNERS, an investment firm",
 "A junior broker at ATLAS WEALTH PARTNERS was caught buying shares for his own account minutes before executing large client orders in the same stock. A second advisor has been heavily promoting a small, unknown stock in online forums. The managing director (judge) wants to understand the legal exposure and build a stronger compliance program.",
 ["Identify the illegal or unethical practices involved","Explain legal considerations and the role of compliance in finance","Recommend a compliance program, including technology"],
 ["BL:133","BL:148","BL:149","FI:355","PD:213"],
 ["What should I tell our clients?","How do we make sure this never happens again?"],
 ["Practice 1 = front-running (illegal). Practice 2 may be a pump and dump, depending on whether he owns and sells the stock.",
  "Legal: SEC and FINRA rules, Securities Exchange Act of 1934. Possible fines, bans and lawsuits.",
  "Compliance: prevent, detect, correct. Chief compliance officer, written policies, annual training.",
  "Technology: trade surveillance software flags employee trades near client orders, and social media monitoring.",
  "Ethics in finance: trust is the product. Violations hurt clients and markets.",
  "Governance: board-level compliance reporting, code of conduct, whistleblower hotline.",
  "Judge Q1: be transparent, explain the corrective actions, and compensate any harmed clients."])

case("brightside-statements","Financial Analysis","financial consultants","owner of BRIGHTSIDE DOG GROOMING, open one year",
 "BRIGHTSIDE DOG GROOMING made a profit in its first year according to its income statement, yet the owner (judge) often struggles to pay suppliers on time and nearly missed payroll twice. Many customers are businesses (kennels) that pay 60 days after service. The owner wants to understand what's going on.",
 ["Explain how the income statement, balance sheet and cash flow statement each tell part of the story","Explain why a profitable business can run short of cash","Recommend actions to improve cash flow"],
 ["FI:094","FI:093","FI:091","FI:579","FI:354"],
 ["Should I just get a bigger loan?","How often should I look at each statement?"],
 ["Income statement = profit over a period, using accrual revenue (earned, not yet collected).",
  "Balance sheet: large accounts receivable mean cash is tied up in unpaid kennel invoices.",
  "Cash flow statement: operating cash flow is low even though net income is positive.",
  "Need for info: the statements show the gap. Track AR days (365 ÷ AR turnover).",
  "Role of finance: working capital management.",
  "Actions: shorten terms to 30 days, offer a 2% discount for paying in 10 days, require deposits, send invoices immediately, add a small line of credit for gaps.",
  "Judge Q1: a loan treats the symptom. Fix collections first, then use a line of credit as a safety net.",
  "Judge Q2: cash weekly, income statement and cash flow monthly, balance sheet monthly or quarterly."])

case("northwind-global","Financial Analysis","investment analysts","investment committee chair of NORTHWIND COMMUNITY FOUNDATION",
 "NORTHWIND COMMUNITY FOUNDATION has a $5 million endowment invested 100% in U.S. large-company stocks. Interest rates and inflation have been volatile, and the committee chair (judge) is worried about a recession. Some board members want to add international and emerging-market investments; others think that's too risky.",
 ["Explain how economic conditions affect financial markets","Explain financial globalization and the case for international diversification","Recommend an allocation approach and how to read the information needed to monitor it"],
 ["FI:574","FI:575","FI:274","FI:275","RM:062"],
 ["Isn't investing overseas just gambling?","What reports should our committee review each quarter?"],
 ["Economy and markets: in contractions stocks fall. Rising rates lower bond prices. Defensive sectors hold up better.",
  "Home bias: 100% domestic concentration ignores diversification benefits.",
  "Globalization: international markets don't move in lockstep with the US, so they can lower overall volatility. Emerging markets add growth but more instability and currency risk.",
  "Recommend: diversified mix, for example 50% US stocks, 15% developed international, 5% emerging, 25% bonds, 5% cash, rebalanced yearly. Not personal advice; set by an investment policy statement.",
  "Monitoring sources: fund annual reports, 10-K and 10-Q filings, stock tables (52-week range, yield, P/E), relative strength.",
  "ERM: the board's risk appetite, documented in an investment policy statement.",
  "Judge Q1: it isn't gambling. Diversification reduces risk, and the position is a modest, measured slice."])

DRILLS = []
def drill(id, scenario, pis, model):
    DRILLS.append(dict(id=id, scenario=scenario, pis=pis, model=model))

drill("d-overbudget","You are an accounting associate at a sporting-goods retailer whose department managers keep going over budget. The CFO (judge) wants your recommendations.",["FI:661","FI:106"],
 "The root problem is a fixed budget that ignores seasonal swings, and managers who don't own their numbers. First, variance analysis: each month compare budget to actual, split into price and volume, and dig into only the big gaps. Second, switch to a flexible budget that scales variable costs with sales, built bottom-up with each manager. We'd target variances within 5%, starting next quarter.")
drill("d-bank-or-cu","You are a financial advisor. A young client (judge) wants to open her first checking account and asks whether to choose a bank or a credit union.",["FI:336","CR:012"],
 "Both are safe if insured: FDIC for banks, NCUA for credit unions, up to $250,000. A credit union is member-owned and not-for-profit, so it usually has lower fees and better loan rates. A big bank may offer more branches and better apps. My job is to match your needs, so for low fees and a future car loan I'd start with a credit union. Let's compare monthly fees and ATM access before you open it.")
drill("d-convergence","You are an analyst. Your bank's president (judge) asks what 'convergence' means and whether the bank should start selling insurance.",["FI:573","FI:337"],
 "Convergence is when firms from different financial sectors combine, like banks and insurers. Consolidation is same-sector mergers. Selling insurance through our branches, called bancassurance, adds fee income and one-stop service for customers already in the insurance market. I'd pilot it in a few branches with a licensed partner, train staff on suitability, and track products per customer and complaints for 12 months.")
drill("d-tvm","A client (judge) asks why she should start investing $2,000 now instead of waiting ten years.",["FI:238","FI:062"],
 "It's the time value of money: a dollar today can earn returns that compound. At 7%, $2,000 grows to about $3,934 in 10 years and about $7,740 in 20. Wait ten years and you lose that whole first decade of compounding. Start now with a low-cost index fund, add a set amount every month, and we'll review it each year.")
drill("d-erm","You are a risk analyst. The CEO (judge) asks how enterprise risk management differs from what the company does now: each department handles its own risks.",["RM:062","RM:058"],
 "Right now risks sit in silos, so no one sees how a cyberattack, a key supplier failure and a recession could hit at once. ERM pulls every risk into one risk inventory, rated by likelihood and impact, with an owner for each. Internal controls handle what we can control. Insurance and contingency plans cover external risks like inflation. I'd start a quarterly risk committee reporting to the board.")
drill("d-governance","You are a consultant. A startup founder (judge) asks why investors keep asking about 'corporate governance.'",["PD:213","PD:214"],
 "Governance is how a company is directed and controlled, and investors see it as protection for their money. Strong governance means an independent board, an audit committee, internal and external audits, a code of conduct and transparent reporting. That lowers the risk of fraud and mismanagement, which raises the valuation. Your first step: add one independent director with finance experience in the next 90 days.")
drill("d-frontrun","You are a compliance officer. Your managing director (judge) asks why a broker buying a stock right before a client's big order is a problem.",["BL:133","BL:148"],
 "That's front-running. It's illegal because the broker profits from confidential client information at the client's expense. It breaks fiduciary duty and SEC/FINRA rules, and it can bring fines, bans and lost trust. Compliance should prevent, detect and correct: trade surveillance software that flags employee trades near client orders, pre-clearance of personal trades, and annual training.")
drill("d-crm","You are a client-services manager at an investment firm. The firm's president (judge) asks whether CRM software is worth the cost.",["CR:024","CR:012"],
 "Yes. CRM puts every client's data and interactions in one hub, so advisors give consistent, personal service. It reveals sales opportunities, like a client who just bought a home and needs insurance, and flags clients at risk of leaving. People still have to judge which data matters and protect client confidentiality. We'd track client retention and products per client after six months.")
drill("d-benford","You are an internal auditor. The controller (judge) asks how to check expense reports for fraud without reviewing all 40,000.",["NF:124","FM:014"],
 "Use data analysis instead of reading everything. Benford's Law says that in real, measured amounts, the leading digit 1 shows up about 30% of the time. Made-up numbers usually break that pattern, so we test the data and flag outliers. Then we filter by employee and by just-under-approval-limit amounts, and match employee addresses against vendor addresses. We review only the flagged items, which saves weeks.")
drill("d-statements","A new bakery owner (judge) asks why she needs three different financial statements.",["FI:579","FI:094"],
 "Each statement answers a different question. The income statement shows whether you made a profit over a period: sales minus costs. The balance sheet shows what you own and owe on one date. The cash flow statement shows whether cash is actually coming in, because you can be profitable and still run out of cash. Review cash weekly and the full set monthly so you catch problems early.")
drill("d-sunk","A manager (judge) wants to keep funding a failing project because 'we've already spent $200,000 on it.'",["FI:658","FI:659"],
 "That $200,000 is a sunk cost. It's gone whatever we decide, so it shouldn't drive the decision. Use marginal analysis: compare the additional cost to finish with the additional benefit we expect. If the next $80,000 brings in less than $80,000 in value, stop and redirect the money to the best alternative, which is the opportunity cost.")
drill("d-careers","A student intern (judge) asks your advice on how to build a network in the finance industry.",["PD:153","PD:152"],
 "Start with professional associations: join a student chapter of a group like the CFA Society or a local finance association, and volunteer for a committee. Go to conferences and seminars and follow up within 48 hours. Ask for informational interviews. And keep in touch with contacts by sharing useful articles. Set a goal of three new professional contacts a month.")
drill("d-cloud","You are an IT-finance analyst. The CFO (judge) asks whether moving the accounting system to the cloud is a good idea.",["FM:011","RM:042"],
 "Cloud accounting gives anywhere access, automatic updates and automated data collection that cuts entry errors. The main risk is a cybersecurity breach, so require multi-factor authentication, encryption, role-based access and a vendor with strong security audits. Keep off-site backups. I'd pilot it for one quarter alongside the current system before switching fully.")
drill("d-equity-statement","An investor (judge) asks what the statement of changes in equity tells her that the other statements don't.",["FI:630","FI:274"],
 "It shows exactly why the owners' stake changed during the period: starting equity, plus net income and new stock issued, minus dividends and buybacks, equals ending equity. That tells you how much profit the company kept to reinvest versus paid out. You'll find it in the annual report and the 10-K. Read it alongside the income statement each year.")
drill("d-taxes","A client (judge) sold stocks this year with $9,000 in gains and wants to know how to reduce the tax.",["BL:134","CR:012"],
 "Capital losses offset capital gains, so selling losing positions this year (tax-loss harvesting) could cut the taxable gain. Gains on assets held over one year get lower long-term rates than short-term gains. Charitable donations of appreciated stock can also help. I'm not your CPA, so we'd confirm with your tax preparer before December 31.")

# Model answers for judge questions that were missing (added in the content review).
_EXTRA = {
 "summit-cu-convergence": "Judge Q1: set targets before the pilot starts: share of members with 2 or more products, member satisfaction above the current score, complaints per 1,000 policies, and commission revenue covering staff and training costs within 12 months.",
 "lumen-budget": "Judge Q2: weekly sales and cash checks, a monthly variance review with each manager, a quarterly re-forecast for the rest of the year, and a full review at year end.",
 "evergreen-client": "Judge Q1: one stock is concentration risk. If that company stumbles, a big share of your inheritance goes with it. A coworker's tip isn't research, and following the crowd is herd mentality. A diversified index fund owns hundreds of companies, so no single one can sink you.",
 "crescent-data": "Judge Q2: one clean database lets you build dashboards that compare actual results to budget in real time, rank customers by profitability, and test what-if scenarios, so decisions rest on current numbers instead of last month's spreadsheets.",
 "atlas-ethics": "Judge Q2: a clear written policy (no personal trades near client orders, pre-clearance for employee trades), trade-surveillance software, annual training with sign-off, a whistleblower hotline, and real consequences that are applied consistently.",
 "northwind-global": "Judge Q2: performance versus a benchmark, the asset mix versus the investment policy statement's targets, fees and expenses, the largest holdings and any concentration, and a short note on market and economic conditions.",
}
for _c in CASES:
    if _c["id"] in _EXTRA:
        _c["model"].append(_EXTRA[_c["id"]])
        _j = sorted([m for m in _c["model"] if m.startswith("Judge Q")])
        _c["model"] = [m for m in _c["model"] if not m.startswith("Judge Q")] + _j
