# (pi, question, [correct, wrong, wrong, wrong], explanation) -- correct answer first; the app shuffles.
Q = []
def q(pi, stem, opts, exp): Q.append((pi, stem, opts, exp))

# --- FIM core ---
q("FM:002","The main purpose of the financial-information management function is to",
 ["provide accurate financial information so managers can make sound decisions.","sell the company's products.","hire accounting staff.","replace the need for budgets."],
 "FIM gathers, processes and reports financial data to guide decisions such as budget allocation.")
q("FM:002","A company compares its profit margins and costs with those of its top competitors. This practice is called",
 ["benchmarking.","front-running.","normalization.","stewardship."],
 "Benchmarking compares performance to competitors or industry standards to find weaknesses and opportunities.")
q("FM:002","After two large companies merge, their accountants struggle because the companies' data structures don't match. This shows that",
 ["mergers and acquisitions can disrupt financial-information management systems.","mergers always simplify accounting.","data structures never matter.","only small businesses have data problems."],
 "Combining different systems, formats and charts of accounts is one of the hardest parts of a merger.")
q("FM:003","Almaz, a financial analyst, is assigned to review a vendor owned by her brother. What is the most ethical action?",
 ["Disclose the connection and remove herself from the assignment","Complete the review quickly","Give the vendor a favorable rating","Keep the relationship secret"],
 "This is a conflict of interest. The ethical response is to disclose it and step aside so the work stays impartial.")
q("FM:003","A record that tracks every step of a financial transaction from start to finish is a(n)",
 ["audit trail.","balance sheet.","stock table.","pro forma budget."],
 "Audit trails let accountants and auditors trace transactions and spot inconsistencies or fraud.")
q("FM:003","Ensuring a company's financial resources are used appropriately and ethically to fulfill its mission is called financial",
 ["stewardship.","leverage.","convergence.","normalization."],
 "Stewardship means responsibly managing resources that belong to others, such as shareholders and donors.")
q("FM:003","Why does ethical financial reporting matter to a company's financial health?",
 ["It builds trust with investors and makes it easier to raise money.","It always increases sales.","It removes the need for audits.","It lets the company skip taxes."],
 "Investors and lenders fund companies they trust. Misleading reports destroy that trust and raise the cost of capital.")
q("FM:011","A business moves its financial records to a cloud-based system. Which risk increases most?",
 ["The threat of a cybersecurity breach","The risk of paper records being lost in a fire","The cost of filing cabinets","Slower access for remote employees"],
 "Cloud systems are accessible anywhere, which also increases exposure to unauthorized access and attacks.")
q("FM:011","What is the main benefit of automated data collection in accounting?",
 ["It reduces manual entry errors such as typos.","It eliminates the need for any accountants.","It guarantees profit.","It makes data less secure."],
 "Automation cuts human errors like transposed numbers and frees staff to analyze data.")
q("FM:011","A program that blocks unauthorized users from accessing a company's network is a",
 ["firewall.","spreadsheet.","database query.","general ledger."],
 "Firewalls monitor and filter network traffic to keep out unauthorized users.")

# --- FIM analysis ---
q("FM:009","Which ratio shows whether a company can pay its immediate liabilities without selling inventory?",
 ["Acid-test ratio","Debt-to-equity ratio","Price-earnings ratio","Inventory turnover"],
 "Acid-test (quick) ratio = (current assets − inventory) ÷ current liabilities.")
q("FM:009","An analyst lists each income statement item as a percentage of total revenue. She is performing a",
 ["vertical analysis.","horizontal analysis.","variance analysis.","break-even analysis."],
 "Vertical (common-size) analysis compares each line to a base figure, allowing comparison of different-sized companies.")
q("FM:009","A supplier reviews a new business customer's credit report and financial ratios before allowing it to pay in 30 days. The supplier is",
 ["applying its credit standards.","front-running.","normalizing data.","budgeting bottom-up."],
 "Businesses set credit standards to decide which customers may buy on credit.")
q("FM:014","Why would an investor calculate a company's debt-to-equity ratio?",
 ["To assess how risky it is to invest in the company","To find the company's stock ticker","To measure customer satisfaction","To calculate employee turnover"],
 "D/E shows how much of the company is financed with debt. High leverage means higher financial risk.")
q("FM:014","An auditor compares employee home addresses with addresses of vendors in accounts payable. What is she most likely looking for?",
 ["Fake vendors or conflicts of interest","Customer complaints","Inventory shrinkage","Marketing opportunities"],
 "A match can reveal an employee paying a vendor they secretly own, a common fraud.")
q("FM:014","Comparing this year's sales to the last five years' sales to spot a trend is an example of",
 ["horizontal analysis.","vertical analysis.","cost allocation.","normalization."],
 "Horizontal (trend) analysis compares the same line item across periods.")
q("FM:013","A key benefit of budgeting software is the ability to",
 ["create many what-if scenarios to see the impact of decisions.","eliminate all expenses.","guarantee accurate forecasts.","avoid involving managers."],
 "Budgeting apps make it fast to model scenarios and compare budgets to actual results.")
q("FM:013","Which budget tracks the cash expected to come in and go out during a period?",
 ["Cash flow budget","Capital budget","Static marketing budget","Sales quota"],
 "A cash flow budget helps a business spot cash shortages before they happen.")
q("FM:013","A company asks each department manager to build a budget, then combines them into the company budget. This is",
 ["bottom-up budgeting.","top-down budgeting.","zero-based taxation.","incremental auditing."],
 "Bottom-up budgeting starts with the people closest to the work and gives them ownership of their numbers.")
q("FM:016","A quality method focused on maximizing customer value while eliminating waste is",
 ["lean.","Benford's Law.","front-running.","static budgeting."],
 "Lean removes anything that doesn't add value for the customer.")
q("FM:016","A rental company switches to activity-based costing. The main benefit is",
 ["a more accurate picture of each rental's profitability.","lower tax rates.","no need for cost data.","faster hiring."],
 "ABC assigns overhead by the activities each product actually uses, so profitability figures are more accurate.")
q("FM:016","A report on a company's environmental and social impact, including the costs of managing climate-related risks, is a(n)",
 ["sustainability report.","8-K.","stock table.","trial balance."],
 "Sustainability (ESG) reporting quantifies environmental, social and economic impact and related financial risks.")
q("FM:016","Six Sigma primarily helps a business",
 ["reduce defects and variation to improve quality.","increase the number of products it sells.","avoid paying overtime.","raise prices."],
 "Six Sigma uses data (DMAIC) to cut variation and defects, which lessens inefficiencies.")

# --- risk ---
q("RM:041","Which is an example of unethical risk management?",
 ["Hiding a product's safety flaws in the fine print of a contract","Buying liability insurance","Training employees on safety","Backing up data off-site"],
 "Deceiving customers to shift risk onto them is unethical, even if it reduces the company's liability on paper.")
q("RM:041","A manufacturer switches to cheaper, lower-quality materials. Which risk increases most?",
 ["Product safety problems and reputation damage","Interest-rate risk","Currency risk","Inflation risk"],
 "Cutting quality raises the risk of unsafe products, recalls, lawsuits and a damaged reputation.")
q("RM:042","A bank uses machine learning to review millions of transactions each day. The main purpose is to",
 ["flag unusual transactions that may be fraud.","replace all customer service.","set interest rates.","print account statements."],
 "Machine learning detects anomalies at a scale and speed human reviewers can't match.")
q("RM:042","Simulating many possible outcomes using historical data and probabilities to estimate risk exposure is called",
 ["risk modeling.","risk avoidance.","data entry.","benchmarking."],
 "Risk models quantify likely losses so managers can plan responses.")
q("RM:042","Which practice best protects a business from data losses caused by a fire or power outage?",
 ["Backing up data regularly and storing copies off-site","Using one shared password","Printing every file","Turning off antivirus software"],
 "Off-site backups mean a local disaster doesn't destroy the only copy.")
q("RM:043","A parent company forms its own insurance company to insure the parent's risks. This is called",
 ["captive insurance.","reinsurance fraud.","bancassurance.","self-dealing."],
 "Captive insurers are owned by the companies they insure and can lower costs and customize coverage.")
q("RM:043","Which law requires public companies to establish and report on internal controls over financial reporting?",
 ["Sarbanes-Oxley Act","Truth in Lending Act","Clean Air Act","Fair Labor Standards Act"],
 "SOX (2002) followed accounting scandals like Enron and requires internal-control reporting and executive certification.")
q("RM:058","Requiring two employees to approve any payment over $10,000 is an example of",
 ["an internal control.","an external risk.","risk avoidance.","a speculative risk."],
 "Dual approval is an internal control that prevents and detects errors and fraud.")
q("RM:058","Which risk is external and largely uncontrollable by a business?",
 ["A change in the inflation rate","Employee theft","Poor safety training","Weak password policies"],
 "Inflation is a macroeconomic factor outside the firm's control. The others can be reduced with internal controls.")
q("RM:058","A company that implements and monitors safety policies in its warehouse is practicing",
 ["risk control.","risk transfer.","speculative risk.","risk retention."],
 "Risk control reduces how often and how badly losses occur.")
q("RM:062","What makes enterprise risk management (ERM) different from traditional risk management?",
 ["It manages all risks together across the entire organization.","It focuses on one department at a time.","It ignores strategic risks.","It is used only by insurance companies."],
 "ERM gives an integrated, organization-wide view of risk instead of handling risks in separate silos.")
q("RM:062","A listing of all of an organization's critical enterprise-wide risks is called a",
 ["risk inventory.","trial balance.","risk premium.","stock table."],
 "A risk inventory (or register) lists risks with their owners, ratings and planned responses.")
q("RM:062","A competitor launches a superior product that threatens a company's long-term market position. This is a(n)",
 ["strategic risk.","operational risk.","hazard risk.","pure risk."],
 "Strategic risk relates to competition, positioning and long-term goals. Operational risk comes from daily processes.")
q("RM:062","A limitation of enterprise risk management is that it",
 ["relies heavily on management's estimates and inputs.","covers too few risks.","is required for every small business.","eliminates all risk."],
 "ERM is only as good as the judgments and data managers feed into it.")

# --- law & compliance ---
q("BL:133","A broker learns a major client is about to buy a huge block of a stock, so the broker buys the stock first for his own account. This illegal practice is",
 ["front-running.","diversification.","hedging.","dollar-cost averaging."],
 "Front-running exploits advance knowledge of client orders to profit from the price move.")
q("BL:133","Scammers promote a cheap stock on social media to drive up its price, then sell their shares before it collapses. This is a",
 ["pump and dump.","Ponzi scheme.","bear market.","stock split."],
 "Pump-and-dump schemes inflate a price with hype, then the promoters sell at the top.")
q("BL:133","An 'investment manager' pays early investors 'returns' using money from new investors rather than profits. This is a",
 ["Ponzi scheme.","mutual fund.","pyramid scheme.","stock dividend."],
 "A Ponzi scheme pays old investors with new investors' money. In a pyramid scheme, members earn mainly by recruiting.")
q("BL:133","A scammer joins a church and convinces members to invest in a fake fund because 'we look out for our own.' This is",
 ["affinity fraud.","insider trading.","front-running.","a pump and dump."],
 "Affinity fraud exploits the trust within a group the scammer belongs to or claims to belong to.")
q("BL:133","A company director sells her shares after learning, before the public, that earnings will be terrible. This is",
 ["illegal insider trading.","legal portfolio rebalancing.","front-running.","a capital loss."],
 "Trading on material, non-public information is insider trading.")
q("BL:134","An investor sells one stock at a $3,000 loss and another at a $5,000 gain in the same year. How does the loss help him?",
 ["It offsets part of the gain, reducing taxable capital gains.","It doubles his taxes.","It has no tax effect.","It must be paid to the SEC."],
 "Capital losses can offset capital gains, so only the net gain of $2,000 is taxed.")
q("BL:134","Taxes on expensive, nonessential items such as yachts and jewelry are called",
 ["luxury taxes.","payroll taxes.","property taxes.","estate taxes."],
 "Luxury taxes raise government revenue from high-end, nonessential purchases.")
q("BL:134","Why might a corporation prefer borrowing over issuing new stock?",
 ["Interest paid on debt is tax-deductible.","Dividends are tax-deductible.","Debt never has to be repaid.","Stockholders charge interest."],
 "Interest is deductible, which lowers the after-tax cost of debt. Dividends are paid from after-tax profits.")
q("BL:148","A key responsibility of a financial institution's compliance department is",
 ["preventing violations of laws and regulations.","maximizing sales commissions.","choosing advertising agencies.","setting stock prices."],
 "Compliance prevents, detects and corrects violations. Prevention is the first priority.")
q("BL:148","Which is a likely consequence of noncompliance with financial regulations?",
 ["Audits, fines and a damaged reputation","Guaranteed higher profits","Lower insurance costs","Automatic tax refunds"],
 "Regulators can investigate, fine and sanction firms, and customers lose trust.")
q("BL:148","Financial compliance helps the overall economy because it",
 ["builds and maintains public trust in the financial system.","eliminates all investment risk.","sets every company's prices.","ends the business cycle."],
 "Rules and enforcement keep markets fair and institutions stable, so people are willing to save and invest.")
q("BL:149","A main advantage of using technology for compliance is that it",
 ["reduces compliance costs by automating monitoring and reporting.","removes the need to follow laws.","hides transactions from regulators.","replaces the board of directors."],
 "Regtech automates routine checks, cuts costs and identifies patterns and trends.")

# --- governance ---
q("PD:213","Which group is responsible for approving and reviewing a corporation's governance policies?",
 ["Board of directors","Customers","Suppliers","Entry-level employees"],
 "The board oversees management and sets governance policy on behalf of shareholders.")
q("PD:213","What is the main goal of a good corporate governance system?",
 ["To minimize unethical behavior, reduce risk and prevent mismanagement","To maximize executive bonuses","To avoid all regulation","To keep shareholders uninformed"],
 "Governance creates accountability so the company is run responsibly for its owners and stakeholders.")
q("PD:213","When a company has poor corporate governance, investors' confidence most likely",
 ["decreases.","increases.","stays the same.","doubles."],
 "Weak governance signals higher risk of fraud and mismanagement, so investors become wary.")
q("PD:213","Which action most directly establishes ethical standards for all employees?",
 ["Implementing a formal code of conduct","Raising prices","Opening a new location","Lowering the dividend"],
 "A written code of conduct sets clear expectations and builds a culture of integrity.")
q("PD:214","Which body sets a corporation's overall strategic direction and protects shareholders' investment?",
 ["Board of directors","Marketing department","External auditors","Customer service team"],
 "The board governs the corporation as a fiduciary for shareholders.")
q("PD:214","An external audit focuses on",
 ["verifying the accuracy of the financial statements.","designing new products.","setting employee schedules.","choosing the CEO's assistant."],
 "Independent external auditors give an opinion on whether statements are fairly presented.")
q("PD:214","Why are internal audits an important part of corporate governance?",
 ["They check that governance practices are sound and issues are addressed.","They replace external audits entirely.","They are required only for nonprofits.","They set the stock price."],
 "Internal audit independently tests controls and reports problems to management and the audit committee.")
q("PD:302","Which is an external mechanism that influences a company's governance?",
 ["Government regulations","The company's bylaws","The internal audit department","The code of conduct"],
 "External mechanisms come from outside the company: regulators, laws, auditors and stock exchange rules.")
q("PD:302","A corporation's internal rulebook that defines how it operates and how decisions are made is its",
 ["bylaws.","prospectus.","8-K.","income statement."],
 "Bylaws outline decision-making procedures and protect shareholder rights.")
q("PD:302","Which change would most likely force a company to strengthen its governance structure?",
 ["Going from a private company to a publicly traded one","Hiring a new receptionist","Changing its logo","Opening a break room"],
 "Public companies face SEC rules, SOX and high transparency demands.")
q("PD:303","A board of directors reviews a CEO's plan to acquire a competitor before it can proceed. This shows that governance",
 ["adds oversight to major management decisions.","removes all decision-making from managers.","has no effect on decisions.","is only about marketing."],
 "Governance processes add checks and approvals, which improves accountability.")
q("PD:301","When employees understand how their work supports organizational goals, they are most likely to feel",
 ["an increased sense of purpose.","less accountable.","confused about their roles.","that governance doesn't apply to them."],
 "Connecting individual work to company objectives increases engagement and supports governance goals.")
