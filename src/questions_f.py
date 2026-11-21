# Extra exam questions, part F: Finance-cluster (Tier 2) PIs, which made up 50% of the 2026 district exam.
# Written after tallying the PI behind every question on 11 past DECA Finance exams (2018-2026): each Tier 2 PI
# appears on nearly every exam, so each now has at least 8 practice questions here. Topics follow the concepts
# those exams tested; the questions, scenarios and wording are original.
# Format: (PI, stem, [correct answer FIRST, then 3 wrong answers], explanation).
Q = []
def q(pi, stem, opts, exp): Q.append((pi, stem, opts, exp))

# ---------------- Business law, compliance, technology in compliance ----------------
q("BL:133","A fraudster joins a church community, earns members' trust, then sells them a fake 'guaranteed' investment. This is an example of",
  ["affinity fraud","front-running","churning","a margin call"],
  "Affinity fraud targets members of an identifiable group, such as a religious, ethnic or professional community, using the trust within the group.")
q("BL:148","A bank requires that the employee who opens new vendor accounts can't also approve payments to vendors. This compliance control is called",
  ["segregation of duties","job enrichment","vertical integration","management by exception"],
  "Splitting key tasks among different people makes it harder for one person to commit and hide fraud.")
q("BL:148","Why does compliance matter so much in the finance industry?",
  ["It maintains public trust in the financial system","It guarantees every investment will make money","It replaces the need for internal audits","It lets firms avoid paying taxes"],
  "Finance runs on trust. Following laws and regulations protects customers and keeps the system stable.")
q("BL:148","A compliance review that finds problems after transactions have already happened, such as a monthly audit of wire transfers, is a(n)",
  ["detective control","preventive control","directive control","speculative control"],
  "Preventive controls stop problems before they happen; detective controls find problems that already occurred.")
q("BL:149","What is a main benefit of using technology for compliance work?",
  ["It completes monitoring faster and with fewer human errors","It removes all regulations a firm must follow","It eliminates the need for compliance staff entirely","It guarantees regulators will never audit the firm"],
  "Regulatory technology (RegTech) automates checks, which raises efficiency, lowers costs and reduces manual mistakes.")
q("BL:149","A bank uses software that scans every transaction overnight and flags patterns that could signal money laundering. This is an example of",
  ["automated transaction monitoring","manual sampling","a credit freeze","an exit interview"],
  "Compliance software can review 100% of transactions and spot patterns humans would miss.")
q("BL:149","Software that continuously reviews a firm's records and flags exceptions, so auditors don't have to check every document by hand, is sometimes called a",
  ["virtual auditor","general ledger","mutual fund","line of credit"],
  "Automated audit tools work like virtual auditors, testing large volumes of data quickly.")
q("BL:149","How does compliance technology usually affect a firm's costs over time?",
  ["It reduces costs by automating repetitive work","It raises costs because every task must be done twice","It has no effect on costs","It only affects marketing costs"],
  "After the upfront investment, automation lowers the cost of routine compliance tasks.")
q("BL:149","Which use of data analytics helps a finance company stay compliant?",
  ["Identifying unusual patterns and trends in transactions","Hiding losses from regulators","Choosing the company's logo colors","Setting employee vacation schedules"],
  "Analytics reveal trends and outliers that may signal fraud or rule violations.")
q("BL:149","Know-your-customer software that compares a customer's photo ID with a live selfie helps a bank",
  ["verify identity when opening accounts","calculate its income tax","set interest rates on CDs","choose branch locations"],
  "KYC rules require banks to verify identities; technology makes that faster and harder to fool.")
q("BL:134","Maria sold stock at a $2,000 loss this year and has $5,000 of gains on other stock. How can tax law help her?",
  ["She can use the loss to offset part of her gains","She must pay extra tax because of the loss","She can deduct the loss only if she buys the same stock the next day","Losses can never be used for taxes"],
  "Capital losses offset capital gains, lowering taxable gains. (Buying the same stock within 30 days triggers the wash-sale rule.)")
q("BL:134","Which accounts give tax advantages specifically to encourage saving for retirement and health costs?",
  ["401(k)s, IRAs and health savings accounts","Checking accounts and debit cards","Credit cards and personal loans","Car loans and leases"],
  "Congress uses tax breaks on 401(k)s, IRAs and HSAs to encourage long-term saving.")
q("BL:134","With a Roth IRA, contributions are made with after-tax money, so qualified withdrawals in retirement are",
  ["tax-free","taxed twice","taxed at a 50% penalty","added to the next year's income"],
  "Roth accounts are taxed going in, not coming out.")

# ---------------- Client services and CRM ----------------
q("CR:012","Before recommending any product, what should a financial advisor learn first?",
  ["The client's goals and expectations","The firm's sales targets for the month","Which product pays the highest commission","The client's favorite brands"],
  "Client service starts with understanding what the client wants to achieve and expects from the relationship.")
q("CR:012","An advisor would earn a bonus for selling one fund over another. To act responsibly, the advisor should first",
  ["disclose the conflict of interest to the client","hide the bonus to avoid confusing the client","only recommend that fund","refuse to work with the client"],
  "Professionals must disclose conflicts of interest and still recommend what fits the client best.")
q("CR:024","A CRM system's biggest advantage for a finance team is that it",
  ["keeps all customer data in one hub for organizing and analysis","replaces the need to talk with customers","automatically approves every loan","prints account statements faster"],
  "CRM software centralizes customer information so the whole team can serve clients consistently.")
q("CR:024","Finding and fixing outdated, duplicate or wrong customer records in a CRM database is called",
  ["data cleansing","data mining","phishing","benchmarking"],
  "Clean data makes CRM reports and personalized messages accurate.")
q("CR:024","A bank uses its CRM to estimate how much revenue a customer will bring in over the whole relationship. This measure is",
  ["customer lifetime value","return on equity","gross domestic product","the current ratio"],
  "Customer lifetime value helps firms decide how much to invest in keeping and serving each customer.")
q("CR:024","Records of every call, email, meeting and website visit with a customer, stored in a CRM, are",
  ["interaction data","demographic data only","financial statements","securities tables"],
  "Interaction data shows how and when customers engage, which helps personalize service.")
q("CR:024","An advisor uses CRM data to send a client a note about 529 plans the week the client's baby is born. This shows how CRM helps firms",
  ["develop personalized messages","reduce product prices","avoid regulations","replace financial advisors"],
  "CRM data lets firms tailor communication to each customer's life events and needs.")
q("CR:024","CRM analytics that spot customers likely to need a mortgage soon help a bank identify",
  ["sales opportunities","tax deductions","regulatory fines","market indexes"],
  "Analyzing customer data reveals which products customers are likely to want next.")

# ---------------- Financial institutions, markets, convergence ----------------
q("FI:336","Banks, credit unions and savings institutions are called financial intermediaries because they",
  ["channel money from savers to borrowers","print the nation's currency","set federal tax rates","guarantee stock market returns"],
  "Intermediaries pool deposits and lend them out, connecting people with extra money to people who need it.")
q("FI:337","Commodities such as coffee, sugar and cotton, which are grown rather than mined, are known as",
  ["soft commodities","hard commodities","capital goods","money market instruments"],
  "Soft commodities are agricultural; hard commodities are mined or extracted, such as gold and oil.")
q("FI:573","When a bank, an insurance company and a brokerage combine their services so customers can bank, insure and invest in one place, the industry trend is called",
  ["convergence","deregulation","deflation","disintermediation"],
  "Convergence blurs the lines between types of financial firms and creates one-stop shopping.")
q("FI:573","The sale of insurance products through a bank's branches and customer relationships is known as",
  ["bancassurance","reinsurance","underwriting","securitization"],
  "Bancassurance is a form of convergence in which banks distribute insurance.")
q("FI:573","When two companies merge and both original companies cease to exist, forming a brand-new legal entity, this is a",
  ["consolidation","horizontal integration of departments","stock split","spin-off"],
  "In a consolidation, the old entities disappear and a new company is created; in a merger, one company usually survives.")
q("FI:573","A major reason financial firms consolidate is to",
  ["lower costs through economies of scale","increase the number of competitors","reduce the services they offer","avoid serving customers"],
  "Larger firms can spread technology, compliance and overhead costs over more customers.")

# ---------------- Economic conditions, globalization ----------------
q("FI:574","During an economic contraction, stocks in which sector tend to hold up best because people need them regardless of the economy?",
  ["Health care","Luxury travel","New home construction","High-end jewelry"],
  "Defensive sectors such as health care, utilities and groceries sell steadily in all phases of the business cycle.")
q("FI:574","Stock prices often start falling before a recession officially begins. That makes the stock market a",
  ["leading indicator","lagging indicator","coincident indicator","fixed indicator"],
  "Investors trade on expectations, so stock prices tend to turn before the economy does.")
q("FI:574","When investors expect company profits to drop in the coming year, stock prices generally",
  ["fall","rise sharply","stay exactly the same","become fixed by law"],
  "Stock prices reflect expected future earnings; lower expected profits lower prices.")
q("FI:575","A country moving from an agriculture-based economy toward industry, with growing but volatile financial markets, is often called a(n)",
  ["emerging market economy","command economy","mature market economy","barter economy"],
  "Emerging markets offer growth opportunities but higher risk and volatility.")
q("FI:575","Over recent decades, most major economies shifted from exchange rates set by governments to rates set by supply and demand. This was a move from",
  ["fixed to floating exchange rates","floating to fixed exchange rates","gold coins to paper money","stocks to bonds"],
  "Under floating rates, currency values change with market forces, which affects global investing and trade.")
q("FI:575","What is a key challenge when comparing companies from different countries?",
  ["Financial reporting requirements vary by country","All countries use exactly the same accounting rules","Foreign companies don't issue financial statements","Currency never changes in value"],
  "Different accounting standards and disclosure rules make cross-border comparisons harder.")
q("FI:575","Investing in a country whose stock market is unstable because it's moving from a government-controlled to a market economy carries extra",
  ["risk","guaranteed return","tax exemption","FDIC protection"],
  "Transitional and emerging economies can offer growth, but political and market instability adds risk.")

# ---------------- Securities information and tables ----------------
q("FI:274","Which document gives shareholders a company's audited financial statements, a letter from management and a review of the year?",
  ["The annual report","A securities table","A credit report","A pay stub"],
  "Public companies publish annual reports (and file 10-Ks with the SEC) so investors can judge performance.")
q("FI:274","A public company must file a Form 8-K with the SEC to",
  ["report a major event, such as a CEO resignation or a merger","report each employee's salary","apply for a business license","request a tax refund"],
  "8-Ks disclose significant events between regular quarterly and annual reports.")
q("FI:274","Which financial statement shows what a company owns and owes on a specific date, which investors use to judge its financial strength?",
  ["Balance sheet","Income statement","Statement of cash flows","Budget variance report"],
  "The balance sheet lists assets, liabilities and shareholders' equity at a point in time.")
q("FI:274","An investor wants independent ratings and research on mutual funds and stocks. Which source is best known for this?",
  ["Morningstar","The Federal Reserve","The IRS","FINRA BrokerCheck"],
  "Morningstar is a widely used independent research firm known for fund and stock ratings.")
q("FI:274","Where on a public company's website would an investor most likely find earnings releases, SEC filings and presentations?",
  ["The investor relations section","The careers page","The product catalog","The customer support chat"],
  "Investor relations pages collect information for current and potential shareholders.")
q("FI:274","Compared with 30 years ago, finding information about a stock today is",
  ["easier than ever, because of free online data and filings","impossible without a broker","only possible in newspapers","limited to large institutions"],
  "SEC EDGAR, company websites and financial sites make securities information widely available.")
q("FI:275","A stock table shows: Last 41.80, Net Chg +0.45. What was the previous day's closing price?",
  ["$41.35","$42.25","$41.80","$0.45"],
  "Net change compares today's price with yesterday's close: 41.80 - 0.45 = 41.35.")
q("FI:275","A stock pays an annual dividend of $1.50 and trades at $50. What is its dividend yield?",
  ["3.0%","1.5%","5.0%","33.3%"],
  "Yield = annual dividend / price = 1.50 / 50 = 0.03, or 3%.")
q("FI:275","In a stock table, the dividend column is blank for a company. This most likely means the company",
  ["doesn't currently pay a dividend","pays the highest dividend in its industry","is bankrupt","is not publicly traded"],
  "A blank dividend means no regular dividend; many growth companies reinvest profits instead.")
q("FI:275","A stock's price swings widely from day to day compared with the overall market. Investors describe this as high",
  ["volatility","liquidity","dividend yield","par value"],
  "Volatility measures how much a price moves; high volatility means higher risk.")

# ---------------- Customer financial analysis, financial-information management ----------------
q("FM:009","A lender reviews an applicant's income, debt-to-income ratio and credit rating mainly to",
  ["judge how likely the applicant is to repay","decide the applicant's job title","set the applicant's tax bracket","choose a branch location"],
  "Analyzing customer financial information shows ability and willingness to repay.")
q("FM:009","Which ratio measures a company's ability to pay current liabilities using only its most liquid assets (excluding inventory)?",
  ["Acid-test (quick) ratio","Debt-to-equity ratio","Price-earnings ratio","Inventory turnover"],
  "Quick ratio = (cash + marketable securities + receivables) / current liabilities.")
q("FM:009","Expressing each line of a customer's income statement as a percentage of total revenue is",
  ["vertical analysis","horizontal analysis","marginal analysis","variance analysis"],
  "Vertical (common-size) analysis compares items within one period; horizontal analysis compares across periods.")
q("FM:002","A main purpose of the financial-information management function is to",
  ["guide decision-making with accurate financial data","design the company's products","hire all new employees","set prices for competitors"],
  "Financial-information management collects and reports data managers use to decide.")
q("FM:002","A company's financial-information system tracks how long customers take to pay. This helps the company",
  ["monitor aging accounts receivable","calculate payroll taxes only","choose advertising slogans","set CEO pay"],
  "An aging report shows overdue receivables so the firm can follow up and protect cash flow.")
q("FM:002","Financial-information management can support operations managers by",
  ["analyzing past resource usage to plan future needs","writing product warranties","handling customer complaints","designing store layouts"],
  "Historical cost and usage data help operations plan purchasing and staffing.")
q("FM:002","A challenge for many companies is that financial data are stored in separate, task-specific software. This makes the data",
  ["hard to access and combine","more secure from all threats","automatically accurate","unnecessary for decisions"],
  "Data silos slow analysis; integrated systems such as ERP help solve this.")
q("FM:003","Treating company financial data as something you must protect and use responsibly on behalf of others is known as",
  ["stewardship","speculation","leverage","arbitrage"],
  "Data stewardship means managing information ethically, accurately and securely.")
q("FM:003","A record that shows who entered or changed each financial transaction, and when, is called a(n)",
  ["audit trail","trial balance","balance sheet","dividend record"],
  "Audit trails make records traceable, which supports honesty and detects tampering.")
q("FM:003","An analyst learns that a company she's reviewing is owned by her brother. The ethical response is to",
  ["disclose the relationship and step away from the assignment","finish the review quickly without telling anyone","give the company a better rating","ask her brother for inside information"],
  "Disclosing conflicts and removing yourself protects the integrity of financial information.")
q("FM:011","Enterprise resource planning (ERP) software helps a company by",
  ["linking accounting, inventory, payroll and other data in one system","replacing all employees","eliminating the need for budgets","guaranteeing profits"],
  "ERP integrates data across departments so information is up to date and shared.")
q("FM:011","Which technology protects a company's financial network by blocking unauthorized access?",
  ["Firewall software","A spreadsheet macro","A digital camera","Presentation software"],
  "Firewalls filter network traffic to keep intruders out of financial systems.")
q("FM:011","Laws that recognize electronic records and signatures as legally binding have allowed companies to",
  ["store and sign financial documents digitally","stop keeping records","avoid audits","print more paper statements"],
  "The federal E-SIGN Act (2000) gave electronic signatures and records legal standing.")
q("FM:011","Automatically importing bank transactions into accounting software improves data accuracy because it",
  ["reduces manual entry errors","doubles every transaction","hides transactions from auditors","removes the need to reconcile ever"],
  "Automated data transfer cuts typing mistakes, though reconciliation is still good practice.")
q("FM:013","A budget that combines the sales, production, expense, cash and capital budgets into one plan is the",
  ["master budget","petty cash budget","static payroll","variance report"],
  "The master budget is the company's complete financial plan for the period.")
q("FM:013","What is the main weakness of a static budget?",
  ["It doesn't adjust for changes in activity levels","It can't include revenue","It is illegal for public companies","It requires no planning"],
  "A flexible budget adjusts to actual volume, which makes comparisons fairer.")
q("FM:013","Budgeting software that lets managers build unlimited 'what if' scenarios helps them",
  ["see the likely impact of decisions before making them","avoid all business risk","skip forecasting","eliminate taxes"],
  "Scenario modeling shows how changes in sales, costs or rates would affect results.")
q("FM:013","A company asks each department to build its own budget estimate, then combines them into the company budget. This is a",
  ["bottom-up approach","top-down approach","zero-sum approach","flat-rate approach"],
  "Bottom-up budgeting starts with the people closest to the work, which improves accuracy and buy-in.")
q("FM:014","Comparing a company's ratios with those of top competitors and industry averages is called",
  ["benchmarking","bootstrapping","factoring","hedging"],
  "Benchmarking shows where a firm is stronger or weaker than peers.")
q("FM:014","Comparing a company's revenue and expenses for 2024, 2025 and 2026 to spot trends is",
  ["horizontal analysis","vertical analysis","break-even analysis","regression to the mean"],
  "Horizontal (trend) analysis compares the same items across periods.")
q("FM:014","Investors analyze a company's financial statements before buying its stock mainly to",
  ["assess the risk and potential return of the investment","learn employees' home addresses","set the stock's price themselves","avoid paying taxes"],
  "Financial analysis shows profitability, stability and risk.")
q("FM:016","A report that shows how a company's operations affect the environment and society, alongside financial results, is a",
  ["sustainability report","10-Q","bank reconciliation","pro forma invoice"],
  "Sustainability reporting uses financial and non-financial data to show long-term impact.")
q("FM:016","Lean management uses financial information mainly to",
  ["find and eliminate waste","increase inventory levels","add extra process steps","raise prices automatically"],
  "Lean focuses on removing activities that don't add value for customers.")
q("FM:016","Activity-based costing gives a property company a more accurate view of each rental's profit because it",
  ["assigns overhead based on the activities each property actually uses","ignores indirect costs","spreads all costs equally","uses only revenue data"],
  "ABC traces indirect costs to the activities that cause them.")

# ---------------- Databases ----------------
q("NF:124","Organizing a database to remove duplicate data and improve its integrity is called",
  ["normalization","phishing","depreciation","benchmarking"],
  "Normalization structures tables so each fact is stored once, which reduces errors.")
q("NF:124","An auditor tests whether the first digits of a company's expense amounts follow the expected pattern, in which 1 appears most often. This uses",
  ["Benford's Law to detect possible fraud","the Rule of 72","the law of diminishing returns","the matching principle"],
  "In many real data sets, about 30% of numbers start with 1. Made-up numbers often don't follow this pattern.")

# ---------------- Careers and professional relationships ----------------
q("PD:152","A professional who evaluates whether a business or person is likely to repay a loan is a",
  ["credit analyst","claims adjuster","actuary","bank teller"],
  "Credit analysts study financial statements and credit histories to recommend lending decisions.")
q("PD:152","Many finance careers, such as stockbroker or insurance agent, require that a person",
  ["pass a licensing exam","own a business first","hold a law degree","work for the government"],
  "FINRA exams (like the SIE and Series 7) and state insurance exams license people to sell financial products.")
q("PD:153","A relationship in which both people share contacts, advice and referrals so both benefit is described as",
  ["reciprocal","one-sided","speculative","adversarial"],
  "Strong professional relationships give value both ways.")
q("PD:153","A new financial planner wants to meet other professionals and learn industry trends. A good step is to",
  ["join and actively participate in a local finance professional association","avoid all industry events","only email strangers asking for jobs","wait for clients to find her"],
  "Professional associations offer networking, education and credibility.")
q("PD:153","An experienced banker who advises a younger colleague on career growth is acting as a",
  ["mentor","competitor","regulator","auditor"],
  "Mentors share experience and open doors for less experienced professionals.")
q("PD:153","An advisor gives clients a small thank-you when they introduce friends who become clients. This is a",
  ["referral system","pyramid scheme","price-fixing agreement","conflict of interest"],
  "Referral programs build relationships and business through satisfied clients (within firm and regulatory rules).")

# ---------------- Corporate governance ----------------
q("PD:213","Corporate governance helps a company by",
  ["keeping any one person from having too much unchecked control","removing the board of directors","eliminating financial reporting","letting managers ignore shareholders"],
  "Governance creates checks and balances among owners, the board and managers.")
q("PD:213","A company with strong corporate governance usually finds it easier to",
  ["raise money from investors and lenders","avoid all taxes","skip audits","ignore regulations"],
  "Investors and lenders trust well-governed companies, which improves access to capital.")
q("PD:213","After a company's accounting scandal becomes public, what usually happens to investor confidence?",
  ["It decreases","It increases","It stays exactly the same","It becomes guaranteed"],
  "Governance failures damage trust, often lowering the stock price and raising borrowing costs.")
q("PD:214","Directors who have no business or family ties to the company's managers bring",
  ["independent thinking to board decisions","guaranteed profits","higher product prices","fewer financial reports"],
  "Independent directors can question management objectively.")
q("PD:214","Board members have a legal duty to act in the best interests of the company and its shareholders. This is a",
  ["fiduciary duty","warranty","lien","franchise"],
  "Fiduciary duties of care and loyalty apply to directors.")
q("PD:214","A main responsibility of a company's board of directors is to",
  ["set the organization's overall strategic direction and oversee management","run the cash register","answer every customer call","write the company's code in software"],
  "The board guides strategy and holds management accountable; managers run daily operations.")
q("PD:301","Which approach best helps employees support a company's governance objectives?",
  ["Involving employees in achieving the organization's objectives","Keeping objectives secret from employees","Punishing all questions","Removing the code of conduct"],
  "Employees who understand and help shape objectives are more likely to follow them.")
q("PD:301","A company links a share of its profits to every employee's pay when governance and performance goals are met. This is",
  ["profit-sharing","embezzlement","a sunk cost","a stock split"],
  "Profit-sharing aligns employees' interests with the company's success.")
q("PD:301","How does involving employees in governance objectives usually affect them?",
  ["It increases their sense of purpose and commitment","It makes them ignore company policy","It removes their responsibilities","It has no effect on behavior"],
  "Participation builds ownership of the goals.")
q("PD:301","Asking employees for feedback on governance policies helps the company",
  ["improve its objectives and how they're carried out","avoid ever changing policies","replace the board of directors","eliminate audits"],
  "Employees on the front lines often see problems leaders miss.")
q("PD:301","An employee notices a coworker falsifying expense reports. Supporting governance objectives, the employee should",
  ["report it through the company's proper channels, such as an ethics hotline","ignore it to avoid conflict","copy the coworker","post about it on social media first"],
  "Employees play a key role in governance by speaking up about misconduct.")
q("PD:301","A company sets aside money in its budget to train employees on its new code of conduct. This shows it is",
  ["allocating resources to achieve governance objectives","cutting governance costs","avoiding compliance","reducing transparency"],
  "Goals need resources such as time, money and training to succeed.")
q("PD:302","When a private company goes public by selling stock on an exchange, its governance structure usually",
  ["becomes more formal, with independent directors and public reporting","becomes less regulated","no longer needs a board","stops being audited"],
  "Public companies must meet SEC and stock exchange governance and disclosure rules.")
q("PD:302","Which factor most directly affects how complex a company's governance structure needs to be?",
  ["The number of owners","The color of its logo","The age of its building","The brand of its computers"],
  "A sole owner needs little formal governance; thousands of shareholders need boards, rules and reporting.")
q("PD:302","A company takes out a large bank loan with covenants that restrict new borrowing and require regular financial reports. This shows that",
  ["lenders can influence a company's governance","only shareholders affect governance","loans never affect management","governance applies only to nonprofits"],
  "Creditors are stakeholders whose contracts can shape decisions and reporting.")
q("PD:302","Government regulations such as the Sarbanes-Oxley Act affect governance structures by",
  ["requiring controls, independent audit committees and executive certification","banning boards of directors","eliminating shareholder rights","setting product prices"],
  "Laws set minimum governance standards for public companies.")
q("PD:302","Bylaws and governance policies help a company because they",
  ["outline decision-making processes and protect shareholder rights","guarantee higher sales","replace all managers","remove the need for audits"],
  "Clear rules define who decides what and how.")
q("PD:303","Which group has final authority to approve major decisions such as a merger or hiring a new CEO?",
  ["The board of directors","Front-line employees","Customers","The company's suppliers"],
  "Governance processes reserve major decisions for the board.")
q("PD:303","How do clear governance processes improve management?",
  ["They clearly define each person's responsibilities and decision rights","They remove all accountability","They let anyone approve any spending","They prevent planning"],
  "Defined roles reduce confusion and speed good decisions.")
q("PD:303","Requiring board approval for any purchase over $5 million affects management by",
  ["adding a check that slows big decisions but improves oversight","eliminating the need for budgets","letting managers spend without limits","removing the board's responsibility"],
  "Approval thresholds balance speed with control.")
q("PD:303","A board's audit committee reviews financial reports before they're released. This governance process mainly helps",
  ["ensure the accuracy and reliability of financial reporting","set employee schedules","choose product colors","negotiate supplier discounts"],
  "Audit committees oversee reporting, internal controls and auditors.")
q("PD:303","Directors who are also company executives (inside directors) usually",
  ["aren't paid extra for serving on the board","must be independent","can't vote on decisions","are always customers"],
  "Inside directors are typically compensated through their executive roles, not board fees.")
q("PD:303","Clear governance helps a company respond faster in a crisis because",
  ["everyone already knows who has authority to decide","no one is responsible","the board must be replaced first","all decisions require a shareholder vote"],
  "Defined decision rights prevent delays when quick action is needed.")

# ---------------- Ethics, technology, legal and ERM in risk management ----------------
q("RM:041","When applying for business insurance, why should a company fully disclose its past losses to the underwriter?",
  ["Honest disclosure is ethical and keeps the policy valid","Underwriters never check information","It always lowers the premium to zero","Disclosure is optional for businesses"],
  "Misrepresenting risk is unethical and can void coverage when a claim is filed.")
q("RM:041","An employee reports to regulators that her company is hiding product safety problems. She is a",
  ["whistleblower","underwriter","fiduciary","broker"],
  "Whistleblowers expose wrongdoing; many laws protect them from retaliation.")
q("RM:041","How are ethics and risk management related?",
  ["They rely on each other: unethical behavior creates risk","They have no connection","Ethics only matters in marketing","Risk management replaces the need for ethics"],
  "Unethical acts create legal, financial and reputational risks.")
q("RM:041","Hiding a product's safety flaws in the fine print of a contract to avoid liability is",
  ["unethical and increases legal and reputational risk","a recommended risk strategy","required by law","a form of diversification"],
  "Concealing dangers violates ethics and often law, and the eventual fallout can be severe.")
q("RM:041","Training employees on workplace ethics expectations helps a company",
  ["reduce the risk of misconduct","increase legal liability","avoid paying insurance","eliminate all risk"],
  "Clear expectations prevent many ethical lapses before they happen.")
q("RM:042","Software that watches a network and alerts staff to suspicious access attempts is a(n)",
  ["intrusion detection system","general ledger","word processor","point-of-sale scanner"],
  "Intrusion detection systems spot possible cyberattacks early.")
q("RM:042","Which simple practice protects a company from losing financial data in a cyberattack or system failure?",
  ["Performing regular backups","Sharing passwords among staff","Turning off antivirus software","Keeping one copy on one laptop"],
  "Regular, secure backups let the company restore data after an incident.")
q("RM:042","A screen that shows managers real-time charts of key risk measures, such as overdue loans and fraud alerts, is a",
  ["digital dashboard","trial balance","pay stub","mission statement"],
  "Dashboards make risk information visible at a glance.")
q("RM:042","A bank uses machine learning to flag unusual transactions as they happen. This technology helps",
  ["detect fraud quickly","increase fraud losses","eliminate all customer accounts","replace interest rates"],
  "AI models learn normal patterns and flag outliers for review.")
q("RM:043","A company creates its own insurance subsidiary to insure the parent company's risks. This is a",
  ["captive insurance company","mutual fund","credit union","reinsurance pool for the public"],
  "Captives let companies transfer risk to an insurer they own, often to save costs or cover unusual risks.")
q("RM:043","Which legal tool lets a business transfer certain risks to another party, such as a supplier agreeing to cover damages from its products?",
  ["A contract","A press release","A mission statement","An organizational chart"],
  "Contract clauses such as indemnification and hold-harmless agreements shift legal risk.")
q("RM:043","Destroying documents to keep them from investigators can lead to charges of",
  ["obstruction of justice","copyright infringement","price discrimination","fair use"],
  "Sarbanes-Oxley added stiff penalties for destroying records to impede investigations.")
q("RM:043","A manufacturer adds clear warning labels and instructions to its products mainly to reduce",
  ["product liability lawsuits","sales","taxes","employee pay"],
  "Inadequate warnings are a common basis for product liability claims.")
q("RM:043","Following safety and employment laws is part of risk management because it helps a business avoid",
  ["negligence lawsuits and fines","all competition","paying suppliers","filing taxes"],
  "Compliance reduces liability exposure.")
q("RM:058","A company agrees with its bank to swap its variable-rate loan payments for fixed-rate payments. This controls",
  ["interest rate risk","fire risk","theft risk","employee turnover"],
  "An interest rate swap protects against rising rates, an external economic risk.")
q("RM:058","Changes in inflation and tax rates are examples of risks that are",
  ["external and economic","internal and controllable","only personal","always insurable"],
  "External risks come from outside the company; firms can respond but can't control them.")
q("RM:058","A credit union says no single employee may release a wire over $10,000 without a second sign-off. This is an example of",
  ["an internal risk control","an external risk","a speculative risk","a market risk"],
  "Dual authorization is a classic internal control against fraud and errors.")
q("RM:062","How does enterprise risk management differ from traditional risk management?",
  ["ERM looks at the combined impact of all risks across the organization","ERM ignores financial risks","ERM manages only insurance","ERM is used only by small businesses"],
  "ERM views risk organization-wide and connects it to strategy.")
q("RM:062","A complete list of the risks an organization faces, used as a starting point for ERM, is a",
  ["risk inventory","balance sheet","sales forecast","stock table"],
  "Identifying risks comes first; the inventory is then assessed and prioritized.")

# ---------------- Statement of changes in equity ----------------
q("FI:630","Which item reduces retained earnings on a statement of changes in equity?",
  ["Dividends paid to shareholders","Net income","New stock issued","Owner investments"],
  "Retained earnings = beginning balance + net income - dividends.")
q("FI:630","On a statement of owner's equity for a sole proprietorship, new money the owner puts into the business",
  ["increases owner's equity","decreases owner's equity","appears only on the income statement","is recorded as revenue"],
  "Owner investments raise equity; withdrawals lower it.")
q("FI:630","Who relies most on the statement of changes in equity to see how their ownership stake changed?",
  ["Investors and shareholders","Customers buying products","Delivery drivers","Competitors' suppliers"],
  "It explains how net income, dividends and stock transactions changed equity.")
q("FI:630","The two main parts of shareholders' equity for a corporation are",
  ["capital stock and retained earnings","accounts payable and wages payable","cash and inventory","revenue and expenses"],
  "Contributed capital (stock) plus retained earnings make up most of equity.")
q("FI:630","A company had beginning retained earnings of $80,000, net income of $30,000 and paid $10,000 in dividends. Ending retained earnings are",
  ["$100,000","$120,000","$110,000","$60,000"],
  "80,000 + 30,000 - 10,000 = 100,000.")
q("FI:630","A profitable company that chooses not to pay dividends will usually",
  ["reinvest its retained earnings in the business","lose all its equity","have to close","report a net loss"],
  "Retained earnings stay in the company to fund growth.")

# ---------------- Time value of money ----------------
q("FI:238","Lena deposits $5,000 at 4% interest compounded annually. About how much will she have after 3 years?",
  ["$5,624","$5,600","$5,200","$6,000"],
  "5,000 x 1.04 x 1.04 x 1.04 = 5,624.32. Simple interest would give only $5,600.")
q("FI:238","Which change would increase the future value of an investment the most, all else equal?",
  ["A higher interest rate over more years","A lower interest rate","Fewer years invested","Withdrawing interest each year"],
  "Future value grows with both the rate and the number of compounding periods.")

# ---------------- Managerial accounting ----------------
q("FI:658","A company spent $40,000 on market research last year. That cost can't be recovered no matter what it decides now. It is a",
  ["sunk cost","variable cost","differential cost","opportunity cost"],
  "Sunk costs are already spent and shouldn't affect future decisions.")
q("FI:658","By choosing to work at his family's shop, Ty gives up a $1,500-a-month job offer. The $1,500 is an example of",
  ["an opportunity cost","a sunk cost","a direct cost","a fixed asset"],
  "Opportunity cost is the value of the next best alternative given up.")
q("FI:658","The lumber used to build a specific table is a ___ cost of that table.",
  ["direct","sunk","indirect","period"],
  "Direct costs trace straight to a product; shared costs like rent are indirect.")
q("FI:658","A factory's building insurance is shared by all the products made there. For each product, it's a(n)",
  ["indirect cost","direct cost","sunk cost","marginal revenue"],
  "Shared costs must be allocated to products because they can't be traced directly.")
q("FI:658","When choosing between two suppliers, a manager compares only the costs that differ between them. These are",
  ["differential costs","sunk costs","fixed costs that don't change","historical costs"],
  "Differential (incremental) costs are the ones that matter in choosing between alternatives.")
q("FI:659","A bakery should keep increasing production as long as each additional batch brings",
  ["marginal revenue equal to or greater than its marginal cost","any revenue at all","higher total fixed costs","lower prices for every batch"],
  "Profit rises while marginal revenue is at least marginal cost.")
q("FI:659","Looking at the extra cost and extra revenue of producing one more unit is called",
  ["marginal analysis","horizontal analysis","ratio analysis","SWOT analysis"],
  "Marginal analysis focuses on the effect of one more unit or decision.")
q("FI:659","Besides the numbers, marginal analysis of a decision should also consider",
  ["qualitative factors, such as customer goodwill and employee morale","only last year's sales","the CEO's favorite option","nothing else"],
  "Some important effects can't be measured precisely but still matter.")
q("FI:659","A factory has idle capacity. A customer offers to buy 1,000 units at $9 each. Each unit costs $6 in variable costs, and fixed costs won't change. Accepting the order would",
  ["increase profit by $3,000","decrease profit by $3,000","have no effect on profit","increase fixed costs by $9,000"],
  "Contribution per unit = 9 - 6 = $3; 1,000 x $3 = $3,000 more profit.")
q("FI:659","A manager uses marginal analysis to decide whether to",
  ["add a second shift","choose a company name","write a mission statement","pick an accounting year"],
  "Marginal analysis fits incremental decisions such as adding output, staff or hours.")
q("FI:659","The cost of producing one additional unit is the",
  ["marginal cost","average fixed cost","sunk cost","total revenue"],
  "Marginal cost is the change in total cost from one more unit.")
q("FI:659","Because of diminishing returns, as a business keeps adding workers to the same equipment, the marginal output of each new worker eventually",
  ["decreases","increases forever","stays constant forever","becomes negative right away"],
  "Each extra input adds less output once fixed resources are stretched.")
q("FI:660","How is managerial accounting different from financial accounting?",
  ["It takes a future-focused approach for internal decisions","It reports only to the IRS","It must follow GAAP formats","It is published for outside investors"],
  "Managerial accounting looks forward and serves internal users.")
q("FI:660","A marketing manager compares the relevant costs of a TV campaign and a social media campaign before choosing. This is an application of",
  ["managerial accounting","external auditing","tax accounting","payroll accounting"],
  "Managerial accounting supports internal decisions like choosing between options.")
q("FI:660","Managerial accounting reports are prepared mainly for",
  ["managers inside the company","government regulators","the general public","competitors"],
  "They help insiders plan, control and decide.")
q("FI:660","Classifying costs by whether a department manager can influence them helps evaluate managers fairly. This is classification by",
  ["controllability","alphabetical order","tax status","customer type"],
  "Managers should be judged on costs they control.")
q("FI:660","Managerial accountants accumulate data on the costs and profits of each product line so managers can",
  ["decide which products to expand or drop","file the company's tax return","print annual reports","set the national interest rate"],
  "Product profitability analysis is a core managerial accounting task.")
q("FI:660","Managerial accounting both ___ financial data and ___ it for decision-makers.",
  ["records; interprets","hides; deletes","sells; buys","ignores; publishes"],
  "Managerial accountants gather the data and explain what it means.")
q("FI:661","A store's storage costs were budgeted at $5,000 but actually came to $6,200. This difference is a(n)",
  ["unfavorable variance of $1,200","favorable variance of $1,200","sunk cost of $6,200","profit of $1,200"],
  "Actual costs above budget create an unfavorable variance.")
q("FI:661","A company paid more per pound for raw materials than its standard cost. Which variance does this create?",
  ["Purchase price variance","Labor efficiency variance","Sales volume variance","Overhead allocation variance"],
  "Price variance = (actual price - standard price) x quantity purchased.")
q("FI:661","Variance analysis compares ___ results with ___ results.",
  ["planned; actual","last year's; competitors'","gross; net","taxable; nontaxable"],
  "Variance = actual minus budgeted (planned).")
q("FI:661","After finding a large labor variance on a project, a manager should",
  ["investigate the cause and make appropriate adjustments","ignore it","fire the whole team immediately","delete the budget"],
  "The point of variance analysis is to understand causes and correct course.")
q("FI:661","A marketing budget shows a favorable variance because planned email campaigns were never sent. This shows that",
  ["a favorable variance can still signal a problem","favorable variances are always good","budgets are useless","emails cost nothing"],
  "Spending less because work wasn't done can hurt future sales.")
q("FI:661","Tracking variances regularly helps managers",
  ["maintain budgetary control","avoid making plans","raise all prices","eliminate fixed costs"],
  "Regular comparison keeps spending and results on track.")
q("FI:662","Cost accounting budgets help managers mainly by serving as a",
  ["financial control tool to compare and evaluate performance","replacement for financial statements","tax return","marketing plan"],
  "Budgets set standards that actual costs are measured against.")
q("FI:662","In the management functions, using a cost budget to tell departments how much they can spend is part of",
  ["directing","recruiting","advertising","forecasting weather"],
  "Budgets direct activity by assigning resources and limits.")
q("FI:662","A production budget that shows total costs of making goods, including materials, labor and overhead, helps management",
  ["consider the business's total cost of production","set competitors' prices","avoid paying suppliers","calculate dividends only"],
  "Cost budgets bring together all production costs for planning.")
q("FI:662","A cost that rises and falls in direct proportion to production, such as packaging, is a ___ cost in a cost budget.",
  ["variable","fixed","sunk","capital"],
  "Variable costs change with volume; fixed costs don't in the short run.")
q("FI:662","Comparing actual production costs to the cost budget helps a company",
  ["identify variances and improve efficiency","avoid all costs","stop producing goods","raise the minimum wage"],
  "Cost budgets reveal where spending differs from plan.")
q("FI:662","Cost budgets help define roles because they",
  ["assign spending responsibility to specific managers","remove accountability","let anyone spend freely","replace job descriptions"],
  "Each budget line has an owner who is responsible for it.")
q("FI:662","Using a cost budget to judge how well a production manager controlled costs is an example of using budgets to",
  ["evaluate performance","advertise products","hire suppliers","issue stock"],
  "Budgets provide a benchmark for performance evaluation.")
q("FI:663","Assigning a share of the building's electricity bill to each department based on square footage is an example of",
  ["cost allocation","direct costing","depreciation","variance analysis"],
  "Allocation spreads indirect, shared costs across the units that benefit.")
q("FI:663","Which cost is most likely to be allocated among departments rather than traced directly?",
  ["Electricity for the whole building","Raw materials for one product","A sales commission on one sale","Hourly wages of one product's assembler"],
  "Utilities serve everyone and must be allocated.")
q("FI:663","Costs are allocated when",
  ["a cost isn't controlled by or traceable to a single department","a cost belongs to one product only","the cost is a dividend","the cost has already been refunded"],
  "Shared costs need an allocation base to divide them fairly.")
q("FI:663","A bank divides its call center costs among branches based on how many customers each branch serves. The allocation base is",
  ["the number of customers","the branch's paint color","the CEO's salary","the number of parking spaces"],
  "An allocation base should reflect what drives the cost.")
q("FI:663","Allocation moves ___ costs to departments or products so they can be added to ___ costs for a full cost picture.",
  ["indirect; direct","sunk; future","fixed; marginal","personal; business"],
  "Full cost = direct costs + allocated indirect costs.")
q("FI:663","Why does cost allocation matter for pricing?",
  ["Without it, a product's price might not cover its full share of overhead","It always lowers prices to zero","It applies only to nonprofits","It replaces the income statement"],
  "Allocated overhead helps managers set prices that cover all costs.")

# ---------------- Additional coverage for frequently tested Tier 2 PIs ----------------
q("FI:574","As the economy moves from recession into recovery, investors tend to",
  ["buy stocks, expecting profits to rise","sell all stocks","stop investing completely","move everything into cash permanently"],
  "Investors often sell in contractions and buy in recoveries, anticipating higher earnings.")
q("FI:336","Which institution lends to developing countries for projects like roads and schools to reduce poverty?",
  ["The World Bank Group","The FDIC","A local credit union","A brokerage firm"],
  "The World Bank provides loans and grants to lower-income countries' governments.")
q("FI:337","Stocks of small companies that aren't listed on a major exchange often trade",
  ["over the counter (OTC)","only at the Federal Reserve","in the money market","on the commodities floor"],
  "OTC markets let dealers trade securities directly, outside formal exchanges.")
q("PD:152","Which finance career focuses on evaluating risks and deciding whether to issue an insurance policy and at what price?",
  ["Underwriter","Teller","Financial planner","Loan collector"],
  "Underwriters assess risk for insurers (and for securities issues at investment banks).")
q("CR:012","A client is confused by a fund's prospectus. A responsible advisor should",
  ["explain the benefits and drawbacks in simple terms","tell the client not to worry about it","only explain the benefits","refuse to discuss it"],
  "Clear, balanced explanations help clients make informed decisions.")
q("NF:124","An analyst needs a list of only clients in Springfield with balances over $250,000. The fastest database tool is",
  ["a query with filters","retyping every record","a pie chart","a word-processing template"],
  "Queries and filters pinpoint exactly the records you need.")
q("FM:014","Which ratio type shows how efficiently a company uses its assets to generate sales?",
  ["Asset utilization (turnover)","Liquidity","Dividend payout","Price-earnings"],
  "Asset turnover = sales / total assets.")
q("FM:009","A bank compares the debt-to-income ratios of loan applicants with its credit standards. If an applicant's DTI is 52% and the limit is 43%, the bank will most likely",
  ["decline or restructure the loan","approve a larger loan","ignore the DTI","lower its standards for everyone"],
  "A DTI above the bank's standard signals too much existing debt.")
q("FI:575","Financial globalization has been driven partly by",
  ["internet-based financial transactions and fewer capital controls","banning international trade","fixing all exchange rates","closing stock exchanges"],
  "Technology and deregulation let money move across borders quickly.")
q("RM:062","Under ERM, organizations are encouraged to view some risks as",
  ["opportunities that can create value","always negative and to be avoided","irrelevant to strategy","only the insurance department's concern"],
  "ERM considers upside risk, such as entering a new market, not just losses.")
q("RM:058","Installing security cameras in a bank branch is a form of",
  ["risk control to reduce theft losses","risk retention","speculative risk","risk transfer to an insurer"],
  "Cameras deter and help detect theft, reducing loss likelihood.")
q("FM:003","Why does ethical financial-information management make a company more attractive to investors?",
  ["Accurate, honest data builds trust, which makes it easier to raise money","Investors prefer hidden losses","It guarantees a higher stock price","It removes all business risk"],
  "Trustworthy reporting lowers perceived risk for investors.")
q("BL:134","An estate passing directly to a surviving spouse is generally",
  ["not subject to federal estate tax because of the unlimited marital deduction","taxed at 100%","taxed twice","subject to sales tax"],
  "The unlimited marital deduction lets spouses transfer assets to each other free of federal estate tax.")
q("PD:213","Who benefits from good corporate governance?",
  ["All stakeholders: shareholders, employees, customers and communities","Only the CEO","Only competitors","No one"],
  "Governance balances the interests of many stakeholders.")
q("PD:214","An internal audit function in a well-governed company mainly",
  ["tests internal controls and checks that policies are followed","sets product prices","designs advertising","hires the external auditor's staff"],
  "Internal auditors give the board independent assurance about controls and risk.")
q("FM:011","A major risk that comes with storing financial data online is",
  ["a cybersecurity breach","faster reporting","lower printing costs","easier collaboration"],
  "Digital systems need strong security to protect sensitive data.")
q("FM:013","A business owner tracks actual spending against the budget every month using software. This step of budgeting is",
  ["tracking (monitoring)","forecasting only","auditing the IRS","issuing dividends"],
  "Budgets only work when actual results are tracked and compared.")
q("FI:238","Getting a paycheck deposited a week earlier and investing it right away helps because",
  ["the money can start earning interest sooner","interest rates are higher on Mondays","it avoids all taxes","compounding stops after a week"],
  "Time is a key driver of the time value of money.")
q("FI:573","Combining the financial statements of a parent company and its subsidiaries into one set of statements is called",
  ["consolidated financial statements","a statement of changes in equity only","a trial balance","a budget variance report"],
  "Consolidated statements combine all assets, liabilities, revenue and expenses of the group.")
q("BL:149","Software that reads new regulations, flags which ones apply to a bank and assigns tasks to update its policies is used for",
  ["regulatory change management","inventory control","customer acquisition","tax preparation for employees"],
  "Rules change often; technology helps firms track and apply new requirements quickly.")
