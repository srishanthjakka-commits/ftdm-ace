# Extra exam questions, part H: 100 more Finance-cluster (Tier 2) questions, bringing every Tier 2 PI to 11.
# Topics follow the concepts tested on 11 past DECA Finance exams (2018-2026); questions, scenarios and wording
# are original. Each explanation says why the right answer is correct, in detail.
# Format: (PI, stem, [correct answer FIRST, then 3 wrong answers], explanation).
Q = []
def q(pi, stem, opts, exp): Q.append((pi, stem, opts, exp))

# ---------------- BL:133, BL:134, BL:148, BL:149 ----------------
q("BL:133","An email that looks like it's from a client's bank asks him to 'confirm' his account number and PIN through a link. This scam is called",
  ["phishing","front-running","churning","a margin call"],
  "Phishing uses fake emails, texts or websites that imitate trusted companies to trick people into revealing account numbers, passwords or PINs. Real banks never ask for a PIN this way. Front-running and churning are broker abuses, and a margin call is a demand for more collateral in a brokerage account.")
q("BL:134","A freelance graphic designer buys a computer used only for her home-based business. How does tax law usually treat this purchase?",
  ["It can be deducted as a business expense, lowering taxable income","It must be taxed twice","It counts as personal income","It can never affect taxes"],
  "Ordinary and necessary business expenses, including equipment used only for the business, can be deducted (or depreciated) from business income on Schedule C. That lowers taxable profit. A personal-use computer wouldn't qualify, which is why business and personal use should be kept separate.")
q("BL:134","A taxpayer who itemizes donates $2,000 to a qualified 501(c)(3) charity. The main tax effect is that the gift",
  ["can be deducted, reducing taxable income","is added to taxable income","is subject to a luxury tax","must be repaid by the charity"],
  "Cash gifts to qualified charities are deductible for taxpayers who itemize, which lowers taxable income. Starting in 2026, people who take the standard deduction can also deduct up to $1,000 ($2,000 for couples). Keep a written receipt for any single gift of $250 or more.")
q("BL:148","A brokerage that failed to supervise its advisors is ordered by regulators to pay $5 million. This is an example of which consequence of noncompliance?",
  ["Paying a fine","Receiving a tax refund","Gaining market share","Lowering insurance costs"],
  "Regulators such as the SEC, FINRA and banking agencies punish compliance failures with fines, plus restrictions and required fixes. Fines are one of the most common consequences, and the public announcement also damages reputation and customer trust.")
q("BL:148","Bank regulators require banks to hold enough capital and follow lending rules mainly to",
  ["help financial institutions remain stable and prevent failures","guarantee every customer a profit","set the price of every stock","eliminate competition among banks"],
  "Capital requirements and lending rules make sure banks can absorb losses without failing, which protects depositors and the wider economy. Bank failures can spread panic, as in 2008 and 2023, so stability is a central goal of financial compliance.")
q("BL:148","A compliance officer designs approval steps, access limits and review procedures before a new product launches. She is",
  ["designing organizational controls to prevent violations","performing an external audit","marketing the product","setting interest rates for the Fed"],
  "A key part of compliance is designing controls, the policies, approvals and procedures that prevent violations before they happen. Building them in before launch is far cheaper than fixing problems later. External audits are done by independent firms after the fact.")
q("BL:149","Compliance software that automatically drives routine checks, such as screening every new customer against sanctions lists, is mainly used for",
  ["automating repetitive compliance tasks","replacing all laws","hiding data from regulators","setting product prices"],
  "Compliance technology drives or automates routine work, like sanctions screening, transaction monitoring and report generation, so it's done consistently for every customer. That frees compliance staff to investigate real red flags and make judgment calls.")
q("BL:149","How does compliance technology help a company reduce errors?",
  ["It applies the same rules consistently and removes manual data entry","It lets employees skip training","It removes the need for audits forever","It deletes records after each transaction"],
  "People get tired and make typing mistakes; software applies rules the same way every time and pulls data directly from systems. That consistency reduces human error in monitoring and reporting. Firms still need training, audits and record-keeping.")
q("BL:149","A bank's compliance dashboard shows that suspicious-activity alerts have doubled at one branch over three months. This shows how technology helps compliance by",
  ["identifying patterns and trends that need investigation","eliminating the branch","guaranteeing no fraud occurred","setting the branch's sales goals"],
  "Analytics and dashboards turn large volumes of data into visible trends, like a jump in alerts at one location, so compliance teams know where to look. Spotting patterns early can uncover fraud, weak controls or training gaps before they become major violations.")

# ---------------- CR:012, CR:024 ----------------
q("CR:012","A client says her last advisor rarely returned calls and never explained changes to her portfolio. The main problem in that relationship was",
  ["lack of communication","too much diversification","low interest rates","excessive transparency"],
  "Poor communication, like unreturned calls and unexplained changes, is one of the most common reasons clients leave advisors. Finance professionals are responsible for responding promptly and explaining what they do and why. Regular, clear communication builds trust.")
q("CR:012","Clients hire financial professionals largely because the professionals provide",
  ["expertise and access clients are unable to obtain by themselves","guaranteed investment returns","free money","a way to avoid all taxes"],
  "Clients pay for knowledge, experience and access, such as planning skills, tax strategies and investment options, that they can't easily get on their own. A professional's responsibility is to use that expertise in the client's interest. No one can guarantee returns or eliminate taxes.")
q("CR:024","A bank uses its CRM to chart how a customer's balances and product use have changed over five years to predict future needs. It is analyzing the customer's",
  ["trajectory","credit freeze","sunk costs","dividend yield"],
  "Looking at how a customer's relationship has moved over time, their trajectory, helps predict what they'll need next, such as a mortgage after years of rising savings. CRM systems store the history that makes this analysis possible.")

# ---------------- FI:274, FI:275 ----------------
q("FI:274","An investor wants to see a company's revenue, expenses and net income for the past year. Which part of the company's filings should she read?",
  ["The income statement","The balance sheet","The statement of changes in equity","The auditor's address list"],
  "The income statement reports revenue, expenses and net income (profit or loss) over a period. Investors use it to judge profitability and growth. The balance sheet shows assets, liabilities and equity at one date, and the equity statement explains changes in ownership.")
q("FI:274","Where can anyone read a U.S. public company's 10-K, 10-Q and 8-K filings for free?",
  ["SEC EDGAR","FDIC BankFind","IRS Free File","FINRA arbitration records"],
  "EDGAR, the SEC's Electronic Data Gathering, Analysis and Retrieval system, gives free public access to filings from every U.S. public company, the same primary sources professional analysts use. The other tools serve different purposes: bank lookup, tax filing and dispute records.")
q("FI:274","On a balance sheet, which section shows the owners' claim on the company's assets?",
  ["Shareholders' equity","Current liabilities","Accounts receivable","Cost of goods sold"],
  "Shareholders' equity equals assets minus liabilities, the owners' claim after creditors are paid. Investors watch it to see whether the company is building value. Liabilities are amounts owed to others, receivables are assets, and COGS is on the income statement.")
q("FI:275","A stock table lists: Close 62.50, Net Chg -1.25. Yesterday's closing price was",
  ["$63.75","$61.25","$62.50","$1.25"],
  "A negative net change means the stock fell from yesterday's close. Add the decline back to today's close: $62.50 + $1.25 = $63.75. Subtracting instead ($61.25) is the common mistake.")
q("FI:275","A stock trades at $48 and its earnings per share are $4. What is its price-earnings (P/E) ratio?",
  ["12","4","48","192"],
  "P/E = price / earnings per share = $48 / $4 = 12. Investors are paying $12 for every $1 of annual profit. Comparing P/E ratios with similar companies helps judge whether a stock is relatively cheap or expensive.")
q("FI:275","A company's stock jumps 15% in one day on heavy trading volume after it announces a major new contract. This most likely shows that",
  ["investors are reacting to news about the company","the stock no longer pays dividends","the SEC set a new price","the company's 52-week high was erased"],
  "Prices and volume in a securities table reflect investor reactions to new information. Good news, like a major contract, raises expected earnings, so buyers bid the price up and trading volume surges. The SEC never sets stock prices.")

# ---------------- FI:336, FI:337 ----------------
q("FI:336","When a bank's customer pays her credit card bill through online bill pay, the bank is performing which role of a financial institution?",
  ["Making payments on behalf of customers to creditors","Underwriting a stock offering","Setting monetary policy","Insuring the customer's life"],
  "One role of financial institutions is moving money: making payments for customers through checks, bill pay, ACH and wires. Underwriting is done by investment banks, monetary policy by the Federal Reserve and life insurance by insurers.")
q("FI:336","Before depositing a large sum, a business owner checks whether a bank is well capitalized and FDIC-insured. She is evaluating",
  ["how risky it is to provide the institution with funds","the bank's advertising budget","the bank's stock ticker","the bank's ATM colors"],
  "Depositors are lenders to their bank. Checking capital strength, insurance coverage and financial health shows how risky it is to entrust money to that institution, especially for balances above the $250,000 FDIC limit, as SVB depositors learned in 2023.")
q("FI:337","Which market lets companies and governments borrow by issuing debt, and lets investors earn interest by lending?",
  ["The bond (debt) market","The commodities market","The foreign exchange market","The art auction market"],
  "The bond market is where borrowing and lending happen through debt securities: issuers sell bonds to raise money and pay interest to investors. Commodities markets trade raw goods, and forex trades currencies.")
q("FI:337","An investor buys a contract that gives her the right, but not the obligation, to buy a stock at $50 within three months. She bought a(n)",
  ["option","bond","certificate of deposit","Treasury bill"],
  "An option gives its holder the right, but not the obligation, to buy (call) or sell (put) an asset at a set price before a deadline. Options are derivatives because their value depends on the underlying stock. Bonds, CDs and T-bills are debt instruments.")

# ---------------- FI:663 cost allocation ----------------
q("FI:663","A firm's $90,000 of IT support costs is shared by three departments that use 50%, 30% and 20% of help-desk tickets. How much is allocated to the department using 30%?",
  ["$27,000","$30,000","$45,000","$18,000"],
  "Allocate the shared cost by the driver: 30% x $90,000 = $27,000. The department using 50% gets $45,000 and the one using 20% gets $18,000, which adds back to $90,000. Allocation divides the cost; it doesn't change the total.")
q("FI:663","Which is the best allocation base for dividing a building's rent among departments?",
  ["Square footage each department occupies","Number of products each sells","The manager's years of experience","Alphabetical order of department names"],
  "An allocation base should reflect what drives the cost. Rent is paid for space, so square footage is the logical base: a department using a quarter of the floor space bears a quarter of the rent. The other options have no connection to rent.")
q("FI:663","Why do managers allocate indirect costs to products even though the costs can't be traced directly?",
  ["To know each product's full cost for pricing and profitability decisions","To increase the company's total costs","To avoid paying the costs","Because tax law forbids direct costs"],
  "A product's full cost includes its share of overhead. Without allocation, products look more profitable than they are, and prices may not cover all costs. Allocation spreads the same total cost more realistically; it doesn't increase or avoid it.")

# ---------------- FM:002, FM:003, FM:009, FM:011, FM:013, FM:014, FM:016 ----------------
q("FM:002","A financial-information system shows a company's cash, debts and profitability at any moment. This helps managers know the company's",
  ["financial well-being at any given time","marketing slogans","employee birthdays","competitors' trade secrets"],
  "Up-to-date financial information gives managers a real-time picture of the company's financial health, such as cash position, obligations and profit, so they can act quickly. Waiting for year-end reports would be too late for many decisions.")
q("FM:002","A main job of financial-information management is to accurately record and report",
  ["financial transactions","customer complaints only","advertising impressions","employee vacation photos"],
  "Financial-information management starts with recording and reporting every financial transaction accurately: sales, purchases, payroll and payments. Everything else, including budgets, analysis and decisions, depends on that foundation of accurate data.")
q("FM:002","By analyzing cost data from each department, a manager discovers that one warehouse spends 40% more per order than the others. This shows that financial-information management",
  ["identifies operational weaknesses and opportunities for improvement","guarantees every department is efficient","replaces the need for warehouses","sets the company's stock price"],
  "Comparing financial data across units reveals where costs are out of line, pointing managers to problems to fix and savings to capture. That's one of the most valuable uses of financial information inside a company.")
q("FM:003","To protect customers' privacy, an ethical company limits which employees can view sensitive financial data. This control is about",
  ["access","advertising","pricing","depreciation"],
  "Limiting access means only employees who need certain data for their job can see it. That protects customer privacy, lowers the risk of identity theft and insider misuse, and is required by privacy and security rules.")
q("FM:003","A company decides how long to keep financial records, where to store them securely and when to destroy them properly. This is part of its",
  ["storage strategy for financial information","marketing plan","sales forecast","pricing strategy"],
  "Ethical financial-information management includes a storage strategy: keeping records as long as laws require, storing them securely and destroying them safely when no longer needed. Poor storage risks data loss, breaches and legal violations.")
q("FM:009","A bank analyzes a small business's working capital before approving a line of credit. Working capital shows",
  ["whether the business has enough short-term assets to cover short-term debts","the owner's personal credit score only","the business's advertising reach","the number of employees"],
  "Working capital = current assets - current liabilities. Positive working capital means the business can likely meet short-term obligations, a key factor for a lender deciding whether a credit line will be repaid.")
q("FM:009","A lender reviews an applicant's credit score mainly to judge the applicant's",
  ["history of repaying debt","future salary","job title","tax bracket"],
  "A credit score summarizes how a person has handled debt, especially payment history and amounts owed. Lenders use it to predict the likelihood of repayment and to set interest rates. Income and job details are checked separately.")
q("FM:011","A company scans its old paper financial records into searchable digital files. This mainly helps it",
  ["store, retrieve and share records quickly while saving space","eliminate the need to keep records","avoid all audits","increase paper costs"],
  "Digital scanning, including digital microfilm scanners for archives, turns paper into searchable files that can be found in seconds, shared securely and backed up. Records still must be kept as long as the law requires.")
q("FM:011","Cloud-based financial systems let a CFO and her team respond quickly to complex questions because they provide",
  ["up-to-date data that can be queried instantly","paper reports mailed monthly","fewer data sources","no security needs"],
  "Modern financial systems store current data in one place and let users run queries and reports instantly, so complex questions get answered in minutes instead of days. They still require strong security.")
q("FM:013","A company uses software to model how taking on a new $2 million loan would affect its future payments and cash flow. This budgeting application is",
  ["debt modeling","revenue recognition","inventory shrinkage","job costing"],
  "Debt modeling projects how borrowing affects interest, principal payments, cash flow and financial ratios over time. It helps managers decide whether the company can afford the loan before signing.")
q("FM:013","Why does budgeting software increase management's confidence in budgets?",
  ["It reduces calculation errors and links budgets to actual data","It guarantees budgets will never change","It removes the need for managers","It hides unfavorable variances"],
  "Budgeting software automates calculations, pulls in actual results and keeps everyone working from the same numbers, so managers can trust the figures and see variances quickly. That reliability builds confidence in using the budget for decisions.")
q("FM:014","An auditor reviews accounts payable to see whether any vendor shares a phone number or address with an employee. This financial analysis application helps",
  ["detect fraud such as fake vendors","set product prices","forecast weather","plan marketing events"],
  "Matching employee data against vendor data in accounts payable is a standard fraud-detection test: a match may reveal an employee who created a fake vendor or secretly owns one. Analytics make it possible to check every vendor quickly.")
q("FM:014","Comparing a company's net profit margin, return on assets and return on equity mainly measures its",
  ["profitability","liquidity","inventory levels","number of shareholders"],
  "Net margin, ROA and ROE all measure how well a company turns sales, assets and owners' money into profit, so they're profitability ratios. Liquidity ratios, like the current ratio, measure ability to pay short-term bills.")
q("FM:016","A company tracks the costs of actions it takes to manage climate-related risks, such as flood-proofing facilities, in its reports. This is an example of",
  ["using financial information in sustainability reporting","calculating payroll taxes","preparing a trial balance","setting a stock split"],
  "Sustainability and climate-risk reporting quantify the financial side of environmental issues, such as the cost of protecting facilities or the potential losses from climate events. That's a non-traditional use of financial information.")
q("FM:016","A factory combines Lean methods with Six Sigma. Lean focuses on removing ___, while Six Sigma focuses on improving ___.",
  ["waste; quality","quality; waste","profits; taxes","employees; customers"],
  "Lean eliminates waste, steps and inventory that don't add value, while Six Sigma reduces defects and variation to improve quality. Many companies combine them as 'Lean Six Sigma,' using financial data to measure savings.")
q("FM:016","Financial information helps a manufacturer reduce wasted resources because it",
  ["shows the cost of scrap, rework and idle time so managers can target savings","hides costs from managers","requires more inventory","eliminates the need for measurement"],
  "Putting a dollar value on waste, like scrapped materials, rework hours and idle machines, shows managers where the biggest savings are. That's how financial information supports Lean and other efficiency programs.")

# ---------------- NF:124 databases ----------------
q("NF:124","A database automatically records the exact date and time each transaction is entered. This feature, called a date/time stamp, is especially useful for",
  ["tracking when changes were made and supporting audits","choosing fonts","increasing data entry errors","replacing passwords"],
  "Date/time stamps create a reliable record of when each entry or change happened. That supports audit trails, fraud investigations and reconstructing events. Combined with user IDs, it shows who did what and when.")
q("NF:124","An analyst screening thousands of stocks narrows the list by industry, then by country, then by analyst rating. She is using",
  ["data filtering in steps","normalization","Benford's Law","a pie chart"],
  "Applying filters one after another narrows a large data set to exactly the records that meet every condition. Filtering by industry, then country, then rating quickly produces a short list. Normalization restructures tables, and Benford's Law tests for fraud.")

# ---------------- PD:152, PD:153 ----------------
q("PD:152","Which finance professional investigates financial records to uncover fraud and may testify in court?",
  ["Forensic accountant","Bank teller","Insurance agent","Loan officer"],
  "Forensic accountants combine accounting and investigative skills to examine records, trace hidden money and uncover fraud, and often serve as expert witnesses. Tellers, agents and loan officers serve customers in day-to-day roles.")
q("PD:152","Besides technical knowledge, which skills do employers in finance say are extremely important?",
  ["Soft skills such as communication, teamwork and ethics","Only typing speed","Memorizing stock tickers","Avoiding client contact"],
  "Finance runs on trust and relationships, so employers value soft skills, like clear communication, listening, teamwork, ethics and problem solving, as highly as technical ability. Explaining complex ideas simply to clients is essential.")
q("PD:153","A CFO attends a national finance conference each year. The main professional benefit is that it",
  ["provides access to valuable industry information and new contacts","replaces the need for a team","guarantees higher profits","lets the company skip audits"],
  "National conferences bring together experts and peers, giving professionals access to new industry information, trends and best practices, and a chance to build relationships that lead to advice, partnerships and opportunities.")
q("PD:153","A financial advisor stays in touch with her network through regular emails and quick check-in calls, not just when she needs something. This shows that strong professional relationships depend on",
  ["consistent communication","one-time contact","avoiding follow-up","only social media likes"],
  "Professional relationships stay strong through consistent, genuine communication over time. Reaching out only when you want something makes relationships feel one-sided. Regular contact keeps you top of mind for referrals and opportunities.")
q("PD:153","Organizations such as the National Bankers Association and local financial planning societies mainly help finance professionals by",
  ["providing networking, education and professional support","setting interest rates","regulating stock prices","insuring deposits"],
  "Professional associations connect members through events, mentoring, continuing education and advocacy, which helps them build relationships and careers. They don't set rates, regulate prices or insure deposits; agencies like the Fed and FDIC do that.")

# ---------------- PD:213, PD:214 ----------------
q("PD:213","Corporate governance aligns the interests of",
  ["individuals, corporations and society","only the CEO and competitors","suppliers and regulators against shareholders","no one in particular"],
  "Good governance balances the interests of shareholders, managers, employees, customers and the wider community, so the company pursues profit in ways that are responsible and sustainable. That alignment is the core purpose of corporate governance.")
q("PD:213","A company's board adopts strong governance practices mainly to",
  ["mitigate risk and avoid problems before they occur","increase executive bonuses","avoid all regulation","limit what shareholders know"],
  "Governance puts checks in place, including independent oversight, controls and transparency, that reduce the risk of fraud, mismanagement and costly mistakes. Preventing problems is far cheaper than recovering from scandals.")
q("PD:214","In a well-governed company, the board oversees ___ on behalf of ___.",
  ["management; stakeholders","customers; competitors","suppliers; employees","regulators; managers"],
  "The board of directors oversees management on behalf of shareholders and other stakeholders. Directors hire, evaluate and, if needed, replace executives, and approve major decisions. That separation is central to good governance.")
q("PD:214","Policies such as approval limits, reconciliations and segregation of duties that keep a company's operations and reporting reliable are",
  ["internal control mechanisms","external audits","marketing tactics","stock options"],
  "Internal control mechanisms are the policies and procedures a company builds to safeguard assets, ensure accurate reporting and follow laws. They're a core component of a well-governed company. External audits are performed by independent outside firms.")

# ---------------- RM:042, RM:043 ----------------
q("RM:042","A bank uses predictive models that analyze economic data to estimate how many loans might default next year. This shows how technology helps risk management by",
  ["anticipating risk exposure before losses occur","eliminating all loan defaults","replacing loan officers' ethics","setting the Fed's interest rate"],
  "Predictive risk models use historical and current data to estimate future losses, so the bank can set aside reserves, tighten lending standards or adjust prices before problems hit. They improve planning but can't eliminate risk.")
q("RM:042","Which technology risk increases as a company moves more of its operations online?",
  ["Security risks such as hacking and data breaches","The risk of paper records yellowing","The risk of slower calculations","The risk of fewer customers online"],
  "Digital operations create new security risks: hackers, ransomware and data breaches. That's why companies invest in firewalls, intrusion detection, encryption, backups and employee training as part of risk management.")
q("RM:042","After installing intrusion detection and multifactor authentication, a company's number of successful cyberattacks will most likely",
  ["decrease","increase","stay exactly the same","double"],
  "Security technology adds layers that block or detect attacks, so successful breaches should decrease. No system eliminates all risk, but layered defenses make attacks much harder and catch intruders faster.")
q("RM:043","In a captive insurance arrangement, the insurance company's policyholders are usually",
  ["also the owners (stockholders) of the insurance company","random members of the public","government regulators","the company's competitors"],
  "A captive insurer is owned by the business or businesses it insures, so the policyholders are also its stockholders. That lets them control coverage and keep underwriting profits, while transferring risk away from operating budgets.")
q("RM:043","A company's liability exposure refers to",
  ["its potential legal responsibility for losses or injuries to others","the amount of cash in its bank account","the number of products it sells","its advertising reach"],
  "Liability exposure is the risk of being held legally responsible for harm to others, such as injuries, damaged property or financial losses. Managing it through safety practices, contracts, warnings and insurance is a key part of legal risk management.")
q("RM:043","Why is staying in compliance with laws and regulations part of managing legal risk?",
  ["It reduces the chance of fines, lawsuits and sanctions","It guarantees higher sales","It removes all business risk","It lets the company skip insurance"],
  "Violating laws exposes a company to fines, lawsuits, sanctions and reputational damage. Compliance prevents many of those legal risks, which is why compliance and risk management work closely together.")

# ---------------- FI:238, FI:573, FI:574, FI:575, FI:630 ----------------
q("FI:238","You invest $2,000 at 6% compounded annually. About how much will you have after 2 years?",
  ["$2,247","$2,240","$2,120","$2,360"],
  "Year 1: $2,000 x 1.06 = $2,120. Year 2: $2,120 x 1.06 = $2,247.20. Simple interest would give $2,240, so the extra $7.20 is interest earned on the first year's interest. Multiply by (1 + rate) once for each year.")
q("FI:238","How much must you invest today at 5% compounded annually to have $11,025 in two years?",
  ["$10,000","$10,500","$11,025","$9,500"],
  "Present value = FV / (1 + i)^n = $11,025 / (1.05 x 1.05) = $11,025 / 1.1025 = $10,000. Check forward: $10,000 grows to $10,500 after year 1 and $11,025 after year 2.")
q("FI:573","A large financial company that offers banking, insurance, investing and financial planning under one roof is called a",
  ["fully integrated financial services provider","credit union","single-line insurer","pawnshop"],
  "A fully integrated financial services provider offers many types of financial products through one company, the result of convergence. Customers get one-stop shopping, and the firm earns more revenue from each relationship.")
q("FI:573","Why do financial companies often earn more after convergence and consolidation?",
  ["They sell more products to each customer and cut duplicate costs","They stop paying taxes","They eliminate all competition by law","They no longer need regulators"],
  "Combined firms can cross-sell, offering a bank customer insurance and investments, and eliminate duplicate costs like overlapping branches and systems. Higher revenue per customer plus lower costs often raises earnings.")
q("FI:574","When inflation rises, the purchasing power of money",
  ["decreases","increases","stays the same","doubles"],
  "Inflation means prices are rising, so each dollar buys less. That decrease in purchasing power is why investors seek returns above inflation and why rising inflation often leads to higher interest rates that affect financial markets.")
q("FI:574","Strong economic growth, with rising employment and consumer spending, usually affects company earnings and stock prices by",
  ["increasing them","decreasing them","stopping all trading","fixing them at current levels"],
  "In an expanding economy, people earn and spend more, so company sales and profits grow. Higher expected earnings push stock prices up, which is why bull markets usually occur during economic expansions.")
q("FI:575","Compared with investing only at home, investing internationally usually involves",
  ["higher risk from currency, political and economic differences","guaranteed higher returns","no risk at all","FDIC insurance on foreign stocks"],
  "International investing adds currency risk, political risk and differences in regulation and economic stability. It also adds diversification benefits. Foreign investments aren't FDIC-insured and returns aren't guaranteed.")
q("FI:575","Financial globalization has increased the use of complex instruments, such as currency swaps and futures, that companies use to manage international risk. These instruments are",
  ["derivatives","savings bonds","checking accounts","common stock"],
  "Derivatives get their value from an underlying asset, rate or index, such as an exchange rate. Multinational companies use currency derivatives to hedge against exchange-rate swings as they do business around the world.")
q("FI:630","A corporation issues $500,000 of new common stock. On the statement of changes in equity, this",
  ["increases contributed capital (capital stock)","decreases retained earnings","appears as revenue","is recorded as a dividend"],
  "Money raised by selling new shares increases contributed capital, the capital stock part of equity. It isn't revenue because it comes from owners, not customers, and it doesn't affect retained earnings, which change with net income and dividends.")
q("FI:630","A sole proprietor withdraws $8,000 from the business for personal use. On the statement of owner's equity, the withdrawal",
  ["reduces owner's equity","increases owner's equity","is recorded as a business expense","increases revenue"],
  "Owner withdrawals (drawings) take value out of the business, so they reduce owner's equity. They aren't business expenses and don't appear on the income statement, because they're distributions to the owner.")
q("FI:630","The statement of changes in equity connects the income statement and the balance sheet because",
  ["net income from the income statement flows into retained earnings on the balance sheet","it lists every customer's purchases","it replaces the cash flow statement","it records only liabilities"],
  "Net income for the period is added to retained earnings on the statement of changes in equity, and the ending equity balance then appears on the balance sheet. That's how the financial statements tie together.")

# ---------------- FI:662, PD:302, RM:041, RM:062, FI:661, RM:058 ----------------
q("FI:662","A manager sets an ambitious but realistic cost target in the production budget so employees have a clear goal to work toward. This shows that cost budgets can",
  ["motivate employees by providing goals","eliminate all costs","replace accounting","set the company's stock price"],
  "Budgets aren't only control tools. They also set targets that motivate employees to work efficiently. Goals that are challenging but achievable work best; impossible targets can push people to cut corners.")
q("FI:662","A cost budget that tells the purchasing department exactly how much it may spend on materials each month is primarily a tool for",
  ["controlling finances","advertising products","hiring employees","issuing stock"],
  "Cost budgets set spending limits for each area, and comparing actual spending against them keeps finances under control. Overspending shows up quickly as a variance that managers can investigate.")
q("FI:662","When preparing a cost budget, management should consider",
  ["the business's total cost of production, including materials, labor and overhead","only raw materials","only advertising","competitors' salaries"],
  "A complete cost budget includes direct materials, direct labor and manufacturing overhead, so management sees the full cost of production. Leaving out overhead would understate costs and lead to poor pricing decisions.")
q("PD:302","The chief executive officer can strongly influence a company's governance structure because the CEO",
  ["leads management and often shapes how decisions are made and reported","writes the nation's securities laws","owns all shareholders' stock","audits the company's financial statements"],
  "As the top executive, the CEO shapes company culture, decision-making and how information flows to the board. Whether the CEO also chairs the board is a key governance question. Laws come from Congress and regulators, and audits from independent firms.")
q("PD:302","After a major accounting fraud is discovered, a company is most likely to change its governance structure by",
  ["adding independent directors and stronger controls","eliminating its board","stopping financial reporting","reducing audits"],
  "Accounting fraud exposes governance weaknesses, so companies usually respond by strengthening oversight with more independent directors, a stronger audit committee, better internal controls and more transparent reporting. Laws like Sarbanes-Oxley came from this kind of response.")
q("PD:302","Who elects a corporation's board of directors, giving them influence over its governance structure?",
  ["Stockholders","Customers","Suppliers","Front-line employees"],
  "Stockholders (shareholders) own the corporation and vote to elect the board of directors, which then oversees management. Shareholder voting is a key way owners influence governance. Large investors can push for changes through their votes.")
q("RM:041","A manager hires her unqualified relative for a key finance role. Which risk does this unethical choice create?",
  ["Poor performance, errors and damaged trust among employees","Lower interest rates","Guaranteed higher profits","Reduced cybersecurity threats"],
  "Nepotism, hiring a family member who lacks the skills, creates operational risk from mistakes and poor decisions, and damages morale and trust among other employees. Ethical hiring based on qualifications is part of good risk management.")
q("RM:041","A company that uses questionable tactics to boost short-term profits most likely increases its",
  ["legal and reputational risk","customer trust","employee loyalty","credit rating"],
  "Unethical shortcuts, like misleading customers or cutting safety corners, may raise profits briefly, but they create legal risk (lawsuits and fines) and reputational risk (lost customers and investors) that can far exceed the short-term gain.")
q("RM:041","An employee provides incomplete data to auditors to hide a problem. This is unethical because it",
  ["prevents the company from seeing and managing a real risk","speeds up the audit","reduces the company's taxes legally","improves data quality"],
  "Audits help a company find and fix risks. Hiding information defeats that purpose, lets problems grow and can be illegal. Ethical risk management depends on complete, honest information.")
q("RM:062","A risk that comes from failures in a company's daily processes, systems or people, such as a payment system outage, is a(n)",
  ["operational risk","strategic risk","speculative market gain","financial windfall"],
  "Operational risk arises from breakdowns in internal processes, people or systems, like outages, errors or fraud. Strategic risk relates to competition and long-term direction. ERM tracks both types in one organization-wide view.")
q("RM:062","A company focuses its ERM program on cutting how much a loss costs when it happens, for example by installing sprinklers. This approach is",
  ["loss reduction","risk avoidance","risk acceptance only","speculation"],
  "Loss reduction lowers the severity of a loss when it occurs; sprinklers limit fire damage. Loss prevention lowers how often losses happen. Risk avoidance means not doing the activity at all.")
q("FI:661","A project's variance report shows labor hours 25% over budget for three months in a row. Variance analysis like this helps managers",
  ["identify trends in the data and correct the cause","ignore budgets","eliminate all labor costs","raise prices automatically"],
  "Tracking variances over several periods reveals trends: a one-time spike may be noise, but three straight months over budget signals a real problem, like underestimated hours, that managers should fix.")
q("FI:661","A favorable materials price variance occurs when a company",
  ["pays less per unit for materials than the standard price","uses more materials than planned","pays more per unit than the standard","sells fewer products than planned"],
  "Price variance compares actual price with standard price. Paying less per unit than standard creates a favorable variance, which helps profit. It's still worth checking that cheaper materials didn't lower quality.")
q("FI:661","Managers analyze variances mainly so they can",
  ["make appropriate adjustments to operations and future budgets","punish employees for every difference","stop budgeting","avoid comparing plans with results"],
  "The point of variance analysis is learning: understanding why results differed from plan, then adjusting operations, prices or future budgets. Blame-focused variance analysis discourages honest reporting.")
q("RM:058","Using PIN-based debit transactions and chip cards to protect customers' payments is an example of",
  ["a risk control that reduces fraud","risk avoidance by closing accounts","a speculative risk","an external economic risk"],
  "PINs and chip technology make it much harder for criminals to use stolen card information, reducing fraud losses. That's a risk control: it reduces the likelihood of loss without avoiding the activity of card payments.")
q("RM:058","Encryption and secure websites (https) that protect online banking sessions mainly",
  ["protect online transactions from interception","increase interest rates","eliminate the need for passwords","speed up loan approvals"],
  "Encryption scrambles data traveling between a customer and the bank, so hackers who intercept it can't read it. Secure connections are a basic risk control for online transactions. Passwords and multifactor authentication are still needed.")

# ---------------- FI:658, FI:659, FI:660 ----------------
q("FI:658","A company's annual building insurance stays the same no matter how many units it produces. In managerial accounting, this is a",
  ["fixed cost","variable cost","sunk cost","marginal cost"],
  "Fixed costs, like insurance, rent and salaries, stay the same in total regardless of production volume in the short run. Variable costs, like materials, rise and fall with volume. Knowing which is which is essential for budgeting and break-even analysis.")
q("FI:658","A manager is choosing between keeping an old machine or buying a new one. Which cost should NOT affect the decision?",
  ["The price paid for the old machine years ago","The new machine's purchase price","Future repair costs of the old machine","Future energy savings from the new machine"],
  "The price paid for the old machine is a sunk cost, already spent and unrecoverable whatever happens now. Only future costs and benefits that differ between options, like the new price, future repairs and energy savings, should drive the decision.")
q("FI:658","A business can rent its spare office space for $1,500 a month but uses it for storage instead. The $1,500 a month is",
  ["an opportunity cost of using the space for storage","a sunk cost","a direct material cost","revenue earned"],
  "Opportunity cost is the value of the best alternative given up. By using the space for storage, the business gives up $1,500 of monthly rent it could have earned. That cost doesn't appear in the accounting records but matters for decisions.")
q("FI:659","A store considers adding one more cashier on Saturdays. Marginal analysis would compare",
  ["the extra sales and customer benefits with the cashier's extra wages","total annual revenue with total rent","last year's profit with this year's taxes","the store's age with its location"],
  "Marginal analysis looks only at the change a decision causes: the additional revenue (and benefits like shorter lines) from one more cashier versus the additional cost of their wages. If the marginal benefit exceeds the marginal cost, add the cashier.")
q("FI:659","Producing the 101st unit adds $14 to total cost and $20 to total revenue. Should the company produce it?",
  ["Yes, because marginal revenue exceeds marginal cost","No, because any added cost lowers profit","Yes, but only if fixed costs rise","No, because revenue is too low"],
  "The 101st unit adds $20 of revenue and $14 of cost, so profit rises by $6. As long as marginal revenue is at least marginal cost, producing more increases profit.")
q("FI:659","Marginal analysis is most useful for decisions about",
  ["whether to increase or decrease an activity by a small amount","writing a company's history","choosing a company's legal name","recording past transactions"],
  "Marginal analysis evaluates incremental changes, like a bit more production, one more employee, an extra hour or a small price change, by comparing their extra benefits and costs. It isn't for recording history or naming a business.")
q("FI:660","Managerial accounting differs from financial accounting because managerial reports",
  ["can be prepared in any format that helps managers decide","must follow GAAP exactly","are filed with the SEC","are published in the annual report"],
  "Managerial reports are for internal use, so they can use any format, level of detail or time period that helps managers decide. Financial accounting reports for outsiders must follow GAAP, and public companies file them with the SEC.")
q("FI:660","A manager asks for a weekly report of each store's labor cost as a percentage of sales. This request is best handled by",
  ["managerial accounting","external auditing","tax accounting","securities law"],
  "A custom internal report used to manage operations, like weekly labor cost by store, is a managerial accounting task. Managerial accounting provides timely, detailed information for planning and control.")
q("FI:660","Which question is a managerial accountant most likely to help answer?",
  ["Should we make this part ourselves or buy it from a supplier?","What was our audited net income last year for investors?","How much tax do we owe the IRS?","What is the national inflation rate?"],
  "Make-or-buy decisions are classic managerial accounting questions: they compare the relevant costs of each option to support an internal decision. Audited results for investors are financial accounting, and taxes are tax accounting.")

# ---------------- PD:301, PD:303 ----------------
q("PD:301","Inviting employee representatives to share input at certain board meetings helps achieve governance objectives by",
  ["giving the board front-line insight and building employee commitment","replacing the board","removing management's responsibilities","eliminating the need for policies"],
  "Employees see how policies work day to day. Hearing from them gives directors practical insight, and including employees builds commitment to governance goals. The board still makes the decisions.")
q("PD:301","An employee who follows the code of conduct, keeps accurate records and completes compliance training is",
  ["supporting the company's governance objectives","only helping marketing","undermining the board","creating a conflict of interest"],
  "Governance isn't only the board's job. Every employee supports it by following policies, keeping honest records and staying trained. Those daily actions are what make governance objectives real.")
q("PD:301","Why should employees understand the company's governance objectives?",
  ["So they know how their actions support ethical, well-run operations","So they can ignore management","So they can avoid all training","So they can set the stock price"],
  "When employees understand the purpose behind policies, they're more likely to follow them and to speak up when something seems wrong. Understanding connects individual actions to the company's goals.")
q("PD:303","A board's compensation committee ties executive bonuses to long-term results instead of quarterly profit. This governance process affects management by",
  ["encouraging decisions that support long-term company health","removing executives' authority","guaranteeing higher stock prices","eliminating the need for a CEO"],
  "Governance processes shape management behavior. Tying pay to long-term results discourages risky short-term moves, like cutting research or inflating quarterly numbers, and aligns executives with shareholders' long-term interests.")
q("PD:303","Clear governance processes make management decisions more effective because they",
  ["define who must approve what, so accountability is clear","let anyone approve anything","remove all oversight","prevent the board from meeting"],
  "When governance spells out decision rights and approval limits, everyone knows who is responsible for each decision. That speeds routine choices, adds oversight to major ones and makes it clear who's accountable for results.")
q("PD:303","A company's governance policy requires major risks to be reported to the board's risk committee each quarter. This mainly helps the board",
  ["oversee risk and guide management's decisions","run daily operations","set employee schedules","approve every small purchase"],
  "Regular risk reporting lets the board oversee the biggest risks and challenge management's plans to handle them. The board guides and oversees; daily operations remain management's job.")
