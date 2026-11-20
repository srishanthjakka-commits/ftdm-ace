# More real-world talking points (added Nov 2026), plus Finance Hub tags for the original 79.
# build_data.py runs this file in the same namespace as talking.py, so t() and T already exist.
# Each new point lists the Finance Hub sub-topics it belongs to and the judge questions it helps you answer.

X = "Taxes"
t(X, ["FI:067","FI:074"], "2027 tax brackets and standard deduction",
  "For 2027 the standard deduction rises to $16,600 for single filers, $33,200 for married couples filing jointly and $24,925 for heads of household. The seven rates (10% to 37%) stay the same and bracket thresholds rise about 3.2% for inflation.",
  "\"For 2027 the first $16,600 of a single filer's income isn't taxed at all, thanks to the standard deduction.\"",
  "IRS Rev. Proc. 2026-35 (Nov. 2026)", "Nov 2026", ["income-tax","filing"],
  ["Will a raise push our client into a higher tax bracket?", "How much of our client's income is actually taxed?"])
t(X, ["FI:061","FI:067"], "No tax on tips and overtime (2025-2028)",
  "Under the 2025 tax law, workers can deduct up to $25,000 of qualified tips and up to $12,500 of overtime premium pay ($25,000 for joint filers) from federal income tax for 2025 through 2028, with phase-outs at higher incomes. Social Security and Medicare taxes still apply.",
  "\"Your tips are now deductible from federal income tax through 2028, but you still owe payroll tax on them, so we'll set that aside.\"",
  "IRS guidance on the 2025 tax law", "2026", ["income-paystub","income-tax"],
  ["How does our client's job income get taxed?", "How should a tipped worker budget?"])
t(X, ["FI:067","FI:569"], "Extra $6,000 senior deduction",
  "For 2025 through 2028, taxpayers 65 and older can claim an extra deduction of up to $6,000 each ($12,000 for a qualifying couple), phased out for higher incomes, on top of the regular standard deduction.",
  "\"Because you're over 65, you get an extra $6,000 deduction through 2028, which lowers the tax on your retirement withdrawals.\"",
  "IRS guidance on the 2025 tax law", "2026", ["income-tax","retire-income"],
  ["How can a retired client lower taxes on withdrawals?"])
t(X, ["FI:067"], "Child tax credit: $2,200 per child",
  "The 2025 tax law set the child tax credit at $2,200 per qualifying child and indexed it to inflation. A credit cuts the tax bill dollar for dollar.",
  "\"Your new baby brings a $2,200 tax credit each year, money we can send straight into the 529.\"",
  "IRS", "2026", ["income-tax","college-save"],
  ["What's the difference between a deduction and a credit?", "How can new parents find money to save?"])
t(X, ["FI:567","FI:067"], "Charity deduction without itemizing (from 2026)",
  "Starting in tax year 2026, people who take the standard deduction can still deduct up to $1,000 ($2,000 for married couples) of cash gifts to qualifying charities.",
  "\"Starting this year, your $1,000 of donations is deductible even though you don't itemize.\"",
  "IRS guidance on the 2025 tax law", "2026", ["giving","income-tax"],
  ["How can our client give to charity on a tight budget?"])
t(X, ["BL:134","FI:077"], "Long-term vs short-term capital gains",
  "Gains on assets held more than a year are taxed at 0%, 15% or 20%; gains on assets held a year or less are taxed as ordinary income, up to 37%. Losses can offset gains, plus up to $3,000 of other income a year.",
  "\"Waiting until you've held it over a year moves the gain from your 22% rate to 15%.\"",
  "IRS Topic 409", "", ["tax-investing-biz"],
  ["How do taxes affect when our client sells investments?"])
t(X, ["FI:625","FI:067"], "Car loan interest deduction (2025-2028)",
  "For 2025 through 2028, interest on a loan for a new vehicle assembled in the U.S. is deductible up to $10,000 a year, phased out at higher incomes.",
  "\"If you buy a new U.S.-assembled car, part of the loan interest is deductible through 2028, but a cheaper car still saves more.\"",
  "IRS guidance on the 2025 tax law", "2026", ["loans","income-tax"],
  ["Should our client finance a new car?"])

X = "Retirement"
t(X, ["FI:569","FI:068"], "Social Security for 2027",
  "Benefits rise 3.6% starting January 2027. The maximum wage subject to Social Security tax rises from $184,500 to $192,300; the 6.2% employee tax is capped at $11,922.60. Medicare's 1.45% has no cap.",
  "\"Social Security benefits rise 3.6% in January because of inflation. It's one of the few retirement incomes that keeps pace automatically.\"",
  "Social Security Administration (Oct. 14, 2026)", "Nov 2026", ["social-security","income-paystub"],
  ["Will Social Security keep up with inflation?", "Why is our client's paycheck smaller than expected?"])
t(X, ["FI:569"], "Saver's Match starts in 2027",
  "Under SECURE 2.0, starting in 2027 eligible lower- and moderate-income workers who contribute to a retirement account get a federal matching deposit of 50% of contributions, up to $1,000 a year.",
  "\"Starting in 2027, the government will match half of your retirement contributions, up to $1,000 a year, if you qualify.\"",
  "SECURE 2.0 Act; IRS", "2026", ["retire-accounts","tax-advantaged"],
  ["How can a lower-income client afford to save for retirement?"])
t(X, ["FI:569"], "Social Security's 2033 shortfall",
  "The 2025 Social Security Trustees Report projected the retirement trust fund would be depleted in 2033; after that, incoming payroll taxes could pay about 77% of scheduled benefits unless Congress acts.",
  "\"Social Security isn't going away, but it may pay about 77% after 2033 without changes, so we treat it as a base and build the rest ourselves.\"",
  "2025 Social Security Trustees Report", "2025", ["social-security"],
  ["Will Social Security be there for young people?"])
t(X, ["FI:569"], "The 4% rule",
  "Researcher William Bengen found in 1994 that withdrawing 4% of a portfolio in year one, then adjusting for inflation, historically lasted at least 30 years. $1 million supports about $40,000 a year.",
  "\"Using the 4% rule, $800,000 supports about $32,000 a year, and Social Security covers the rest.\"",
  "Bengen, Journal of Financial Planning (1994)", "", ["retire-income"],
  ["How much can our client safely spend in retirement?", "How do we make sure they don't run out of money?"])
t(X, ["FI:569","BL:134"], "Required minimum distributions at 73",
  "Owners of traditional IRAs and 401(k)s must start taking required minimum distributions at age 73 (75 for people born in 1960 or later). Roth IRAs have no RMDs for the original owner.",
  "\"A Roth IRA never forces you to withdraw, so it can keep growing tax-free for your heirs.\"",
  "IRS; SECURE 2.0 Act", "", ["retire-income","tax-advantaged"],
  ["Roth or traditional for a client thinking about heirs?"])

X = "Estate & legacy"
t(X, ["FI:572"], "Estate and gift limits for 2027",
  "The federal estate and lifetime gift exemption is $15 million per person for 2026 and $15.48 million for 2027. The annual gift exclusion rises from $19,000 to $20,000 per recipient in 2027.",
  "\"Very few families owe estate tax, but every family needs a will, a guardian and updated beneficiaries.\"",
  "IRS Rev. Proc. 2026-35 (Nov. 2026)", "Nov 2026", ["estate"],
  ["Do our clients need to worry about estate tax?", "Why do young parents need estate planning?"])
t(X, ["FI:572"], "Prince died without a will",
  "When Prince died in 2016 with no will, his estate took about six years and long court battles to settle. Aretha Franklin left handwritten wills, one found in her couch; a jury decided in 2023 which one counted.",
  "\"Prince's estate took six years to settle because he had no will. A simple will now spares your family that.\"",
  "Court records and news reports", "", ["estate"],
  ["What happens if someone dies without a will?"])

X = "Credit & debt"
t(X, ["FI:002","FI:568"], "Household debt hits $19.1 trillion",
  "U.S. household debt reached $19.1 trillion in the third quarter of 2026, and credit card balances hit a record $1.29 trillion, up $22 billion in three months.",
  "\"Americans owe a record $1.29 trillion on credit cards, so a plan that keeps you out of that statistic is worth a lot.\"",
  "New York Fed Household Debt and Credit Report (Nov. 10, 2026)", "Nov 2026", ["credit-basics","debt-control"],
  ["How serious is credit card debt for consumers?"])
t(X, ["FI:782"], "The average credit card rate is about 22%",
  "Banks charged an average of 22.36% on credit card accounts that paid interest in the third quarter of 2026. At that rate, a $5,000 balance costs about $1,100 a year in interest.",
  "\"Paying off a 22% card is a guaranteed 22% return, better than any investment we could recommend.\"",
  "Federal Reserve G.19 Consumer Credit (Nov. 2026)", "Nov 2026", ["cost-credit","debt-control"],
  ["Should our client pay off debt or invest first?", "How expensive is carrying a balance?"])

X = "Kids & college"
t(X, ["FI:831","FI:782"], "Student loan rates for 2026-27",
  "Federal Direct loans first disbursed from July 1, 2026 through June 30, 2027 carry fixed rates of 6.52% for undergraduates, 8.07% for graduate students and 9.07% for Parent PLUS.",
  "\"Federal undergraduate loans are fixed at 6.52% this year, cheaper and safer than most private loans.\"",
  "U.S. Department of Education", "2026-27", ["college-aid","cost-credit"],
  ["Federal or private student loans?", "How should a family pay for college?"])
t(X, ["FI:831"], "The 2027-28 FAFSA opened early; Grad PLUS ended",
  "The 2027-28 FAFSA opened in late September 2026, its earliest launch ever. Starting July 1, 2026, new Grad PLUS loans ended and new borrowing caps apply to graduate and Parent PLUS loans.",
  "\"File the FAFSA now. It's already open, and some aid is first come, first served.\"",
  "Federal Student Aid; U.S. Department of Education", "Nov 2026", ["college-aid"],
  ["When should a family apply for financial aid?"])

X = "Economy right now"
t(X, ["EC:017","EC:018"], "GDP grew 3.4% last quarter",
  "Real GDP grew at a 3.4% annual rate in the third quarter of 2026, up from 2.2% in the second quarter, according to the advance estimate.",
  "\"The economy is growing at 3.4%, a good time to build reserves before the next slowdown.\"",
  "BEA advance estimate (Oct. 29, 2026)", "Nov 2026", ["indicators-cycle"],
  ["How is the economy doing right now?", "How should the plan change if a recession hits?"])
t(X, ["EC:082"], "Unemployment is 4.1%",
  "Employers added 165,000 jobs in October 2026 and the unemployment rate fell to 4.1% from 4.2%.",
  "\"With unemployment at 4.1%, jobs are fairly secure now, which is exactly when to fill the emergency fund.\"",
  "BLS Employment Situation (Nov. 2026)", "Nov 2026", ["indicators-cycle"],
  ["Which economic indicator would you watch?"])
t(X, ["EC:083"], "Inflation peaked at 9.1% in 2022",
  "CPI inflation peaked at 9.1% in June 2022, the highest in about 40 years, which led the Fed to raise rates from near zero to 5.25%-5.50% by July 2023.",
  "\"In 2022 inflation hit 9.1%. Cash that earned nothing lost almost a tenth of its value in one year.\"",
  "BLS; Federal Reserve", "", ["inflation","fed-rates"],
  ["Why shouldn't our client keep everything in cash?"])
t(X, ["FI:575","EC:100"], "The $9.6 trillion-a-day currency market",
  "The foreign exchange market traded about $9.6 trillion a day in April 2025, and the U.S. dollar was on one side of about 89% of trades.",
  "\"Currency markets trade almost $10 trillion a day, so exchange rates move fast, which is why an exporter should hedge.\"",
  "Bank for International Settlements Triennial Survey (2025)", "2025", ["globalization","market-types"],
  ["How does a strong dollar affect a business that sells overseas?"])

X = "Banks, safety & payments"
t(X, ["FI:336","FI:573"], "4,238 FDIC-insured banks",
  "There were 4,238 FDIC-insured institutions in the second quarter of 2026, down 41 in the quarter, and more than 17,000 in 1984. U.S. banks earned $90.1 billion that quarter.",
  "\"There are about a quarter as many banks as in 1984, so a local institution that knows you is worth seeking out.\"",
  "FDIC Quarterly Banking Profile, Q2 2026", "2026", ["bank-how","consolidation"],
  ["How does consolidation affect customers?", "How do banks make money?"])
t(X, ["FI:059","FI:060"], "Goodbye, penny",
  "The U.S. Mint struck its last pennies for circulation in November 2025 because each cost about 3.7 cents to make. Existing pennies remain legal tender.",
  "\"Even money itself changes: the penny cost almost four cents to make, so the government stopped producing it.\"",
  "U.S. Treasury; U.S. Mint", "2025", ["money-basics"],
  ["What is money, and how is it changing?"])
t(X, ["FI:058"], "Cash is now 1 in 7 payments",
  "Cash was used for about 14% of U.S. consumer payments in 2024, down from about 31% in 2016; cards and electronic payments make up most of the rest.",
  "\"Most payments are digital now, which is why online account security belongs in every plan.\"",
  "Federal Reserve Diary of Consumer Payment Choice", "2025", ["money-basics","payments"],
  ["How do people pay for things today?"])
t(X, ["FI:075","FI:076"], "5.6 million unbanked households",
  "About 4.2% of U.S. households (5.6 million) had no bank account in 2023. The top reason given was not having enough money to meet minimum balance requirements.",
  "\"A no-minimum checking account at a credit union gets you out of check-cashing fees, which can cost hundreds a year.\"",
  "FDIC National Survey of Unbanked and Underbanked Households (2023)", "2023", ["providers"],
  ["How would you help a client who doesn't have a bank account?"])
t(X, ["FI:830","FI:063"], "Report debit fraud within 2 days",
  "Under Regulation E, if you report an unauthorized debit card or electronic transfer within 2 business days, your loss is capped at $50; within 60 days, $500; after that it can be unlimited.",
  "\"Turn on instant alerts. If you report a fraudulent debit within two business days, the most you can lose is $50.\"",
  "CFPB, Regulation E", "", ["payments","consumer-law","identity"],
  ["How often should our client check their accounts?"])
t(X, ["FI:075","FI:782"], "Payday loans cost about 400% APR",
  "A typical two-week payday loan with a $15 fee per $100 borrowed equals an APR of almost 400%, and many borrowers roll loans over repeatedly.",
  "\"A $15 fee on $100 for two weeks sounds small, but it's about a 400% APR. A credit union small-dollar loan is far cheaper.\"",
  "CFPB", "", ["providers","cost-credit"],
  ["Why not use a payday loan in an emergency?"])

X = "Fraud & scams"
t(X, ["FI:073"], "FBI: $20.9 billion lost to internet crime",
  "The FBI's Internet Crime Complaint Center counted about $20.9 billion in reported losses for 2025, up about 26% from 2024. Investment fraud, much of it crypto-related, was the costliest category.",
  "\"Online fraud losses keep setting records, so we'd build scam protection into your plan from day one.\"",
  "FBI IC3 Internet Crime Report 2025", "2026", ["scams"],
  ["How big a problem is fraud?"])
t(X, ["FI:073","RM:042"], "A $25 million deepfake",
  "In 2024 an employee at engineering firm Arup's Hong Kong office sent about $25 million after a video call in which the 'executives' were AI deepfakes.",
  "\"AI can fake a voice or a face, so we'd set a family code word and a rule: verify any money request by calling a number you already know.\"",
  "News reports; Arup statement (2024)", "", ["scams","fintech-ai"],
  ["What are the risks of AI in finance?", "How would you protect a client from scams?"])
t(X, ["FI:073","FI:074"], "The IRS Identity Protection PIN",
  "Anyone who can verify their identity can get an IRS Identity Protection PIN, a six-digit number required to file a return in their name, which blocks fraudulent tax filings.",
  "\"An IRS IP PIN takes ten minutes to set up and stops anyone else from filing a tax return in your name.\"",
  "IRS", "", ["identity","filing"],
  ["Our client's identity was stolen. What now?"])
t(X, ["RM:058","FI:351"], "The $53 million small-town theft",
  "Rita Crundwell, comptroller of Dixon, Illinois, stole about $53 million over two decades through a secret account. She was caught when a coworker covering her vacation noticed it.",
  "\"Mandatory vacations sound minor, but that's how a $53 million theft was finally caught.\"",
  "U.S. Department of Justice (2012)", "", ["occ-fraud","erm-controls"],
  ["How would you prevent employee theft?"])

X = "Client trust & regulation"
t(X, ["BL:148","BL:133"], "TD Bank's $3 billion guilty plea",
  "In October 2024 TD Bank pleaded guilty to Bank Secrecy Act violations and agreed to pay about $3 billion, the largest such penalty against a U.S. bank; most of its transactions had gone unmonitored for years.",
  "\"Compliance isn't optional. TD Bank paid about $3 billion because it didn't monitor transactions.\"",
  "U.S. Department of Justice (Oct. 2024)", "", ["compliance","laws-regulators"],
  ["Isn't regulation just extra cost?", "How do banks stop money laundering?"])
t(X, ["BL:149","BL:148"], "The $2 billion texting crackdown",
  "From 2021 to 2024 the SEC and CFTC fined dozens of financial firms more than $2 billion combined because employees used unapproved apps like WhatsApp for business and the messages weren't kept.",
  "\"Every business message must be recorded, which is why our firm uses approved, archived channels only.\"",
  "SEC and CFTC enforcement announcements", "", ["compliance"],
  ["How can technology help a firm stay compliant?"])
t(X, ["BL:133","FI:077"], "The GENIUS Act for stablecoins",
  "The GENIUS Act, signed in July 2025, created the first federal rules for payment stablecoins, including 1-to-1 reserves in cash or short-term Treasuries and regular disclosures.",
  "\"Stablecoins now have federal rules, but they're still not FDIC-insured deposits, so we treat them differently from a bank account.\"",
  "GENIUS Act (2025)", "2025", ["laws-regulators","fintech-ai"],
  ["Is crypto regulated?", "Should our client invest in crypto?"])
t(X, ["CR:012"], "Form CRS: the plain-English summary",
  "Since June 30, 2020, brokers and investment advisers must give retail clients Form CRS, a short summary of services, fees, conflicts of interest and disciplinary history.",
  "\"Here's our Form CRS: two pages showing every fee and conflict, so you know exactly how we're paid.\"",
  "SEC", "", ["client-duty","ethics"],
  ["What are your responsibilities to us?", "How can we trust you?"])

X = "Small business"
t(X, ["SM:075","RM:042"], "The CrowdStrike outage",
  "In July 2024 a faulty CrowdStrike software update crashed about 8.5 million Windows computers, grounding flights; Delta said the outage cost it about $500 million.",
  "\"One vendor's bad update shut down airlines, so we'd plan for technology failure with backups and business interruption coverage.\"",
  "Microsoft; Delta Air Lines statements (2024)", "", ["business-insurance","erm-controls","risk-process"],
  ["What's the biggest risk to this business?", "How would you manage third-party risk?"])
t(X, ["FI:659"], "Break-even for a food truck",
  "With $6,000 of monthly fixed costs, a $12 average meal and $5 of variable cost, each meal contributes $7, so break-even is about 857 meals a month, roughly 29 a day.",
  "\"You break even at about 29 meals a day. Everything after that is profit.\"",
  "Break-even formula: fixed costs / contribution margin", "", ["breakeven-marginal"],
  ["How many sales does the business need to break even?"])
t(X, ["FI:354"], "Toys R Us and too much debt",
  "Toys R Us was bought in a 2005 leveraged buyout that left it with about $5 billion of debt. Interest payments starved it of money to modernize, and it filed for bankruptcy in 2017.",
  "\"Debt has to be repaid in good months and bad. Toys R Us showed what happens when a business borrows too much.\"",
  "Court filings; news reports", "", ["biz-funding","finance-role"],
  ["Should the business take a loan or an investor?", "Is all debt bad?"])
t(X, ["EN:039","FI:354"], "Spanx: started with $5,000",
  "Sara Blakely started Spanx with $5,000 of her own savings and kept full ownership for years by bootstrapping, before selling a majority stake in 2021 at a $1.2 billion valuation.",
  "\"Bootstrapping kept 100% of Spanx with its founder. Growing on your own revenue first keeps your options open.\"",
  "Company history; news reports", "", ["biz-funding","entrepreneur"],
  ["How should this business raise money?", "What makes a successful entrepreneur?"])
t(X, ["EN:039"], "Record new business applications",
  "Americans have filed more than 5 million new business applications each year since 2021, well above pre-pandemic levels.",
  "\"Entrepreneurship is booming, which also means more competition, so your plan needs a clear edge.\"",
  "U.S. Census Bureau Business Formation Statistics", "2025", ["entrepreneur"],
  ["Is now a good time to start a business?"])
t(X, ["SM:075","FI:830"], "A data breach costs $4.4 million",
  "The average cost of a data breach was about $4.4 million globally in 2025.",
  "\"If you store customer data, cyber insurance and two-factor logins aren't optional. One breach can cost more than the business is worth.\"",
  "IBM Cost of a Data Breach Report 2025", "2025", ["business-insurance","identity"],
  ["What insurance should this business buy?"])
t(X, ["FI:661"], "Egg prices and the price variance",
  "Repeated bird-flu outbreaks from 2022 to 2025 pushed wholesale egg prices to records, giving bakeries and restaurants large unfavorable materials price variances. Many responded with menu changes or surcharges.",
  "\"Your food costs are over budget because of egg prices, a price variance, so the fix is the supplier or the menu, not the staff.\"",
  "USDA and BLS price data; news reports", "", ["variance","inflation"],
  ["How would you track whether the business sticks to its budget?"])
t(X, ["FI:093","FI:353"], "WorldCom's $3.8 billion trick",
  "WorldCom recorded about $3.8 billion of ordinary expenses as assets to inflate profit. The fraud, uncovered in 2002, helped bring about the Sarbanes-Oxley Act.",
  "\"WorldCom shows why profit alone can mislead. We'd read all four statements, not just the income statement.\"",
  "SEC (2002)", "", ["statements","accounting-law","ethics"],
  ["Which financial statement matters most?", "What would you do if asked to make the numbers look better?"])

X = "Insurance"
t(X, ["FI:571"], "Flood isn't in your homeowners policy",
  "Standard homeowners policies don't cover flood damage. Flood coverage comes from the National Flood Insurance Program or private insurers. Hurricane Helene in 2024 flooded inland areas where few homeowners had it.",
  "\"Your home policy won't pay for a flood. A separate flood policy is cheap where risk seems low, which is exactly where Helene hit.\"",
  "FEMA; news reports (2024)", "", ["personal-insurance","insurance-basics"],
  ["What insurance does a homeowner need?"])
t(X, ["FI:081"], "Insurers retreat from wildfire zones",
  "Allstate (2022) and State Farm (2023) stopped writing new home policies in California, and the January 2025 Los Angeles wildfires were among the costliest disasters in U.S. history.",
  "\"Insurance gets harder to buy where risk is rising, so we'd review coverage limits every year and price that into the home decision.\"",
  "Company statements; Insurance Information Institute", "2025", ["insurance-basics","risk-process"],
  ["How does climate risk affect insurance?"])

X = "Saving & investing"
t(X, ["FI:077"], "Most active funds trail the index",
  "Roughly 9 in 10 actively managed U.S. large-cap stock funds trailed the S&P 500 over 15 years, according to S&P's SPIVA scorecard.",
  "\"Even professionals rarely beat the index for long, so a low-cost index fund puts the odds on your side.\"",
  "S&P Dow Jones Indices SPIVA U.S. Scorecard", "", ["inv-types","risk-diversify"],
  ["Why an index fund instead of picking stocks?"])
t(X, ["FI:077","FI:574"], "2022: stocks and bonds fell together",
  "In 2022 the S&P 500 lost about 18% and the Bloomberg U.S. Aggregate Bond Index about 13%, a rare year when bonds didn't cushion stock losses, because rising rates hit both.",
  "\"Even bonds can fall when rates jump, which is why we match investments to your timeline, not just mix stocks and bonds.\"",
  "S&P Dow Jones Indices; Bloomberg", "", ["risk-diversify","fed-rates"],
  ["Why do bond prices fall when rates rise?", "How do you decide how much risk the client takes?"])
t(X, ["FI:077"], "Spot bitcoin ETFs",
  "The SEC approved the first spot bitcoin ETFs in January 2024, letting investors hold bitcoin exposure in ordinary brokerage accounts. Bitcoin's price still fell more than 60% in 2022.",
  "\"If you want crypto, a regulated bitcoin ETF capped at about 5% of your investments limits the damage if it crashes.\"",
  "SEC (Jan. 2024)", "", ["inv-types","fintech-ai"],
  ["Should our client invest in crypto?"])

X = "Governance & industry trends"
t(X, ["PD:213","PD:302"], "OpenAI's five-day board crisis",
  "In November 2023 OpenAI's nonprofit board fired CEO Sam Altman, then reinstated him within days after employees and investors pushed back, a case study in how governance structure shapes control.",
  "\"Who controls the board decides who controls the company, which is why we'd set clear governance before taking on investors.\"",
  "Company statements; news reports (2023)", "", ["governance"],
  ["Why does corporate governance matter?"])
t(X, ["CR:016","CR:024"], "Keeping clients pays",
  "Bain & Company research found that raising customer retention by 5% can raise profits by 25% to 95%, because loyal customers buy more, cost less to serve and refer others.",
  "\"Keeping a client is far cheaper than finding a new one, so our CRM schedules a check-in before every big date in your life.\"",
  "Bain & Company (Frederick Reichheld)", "", ["crm"],
  ["How would you keep this client relationship strong?"])

# ---------- Finance Hub tags and judge questions for the original 79 points ----------
TAGS = {
 't1': (['why-invest','goals'], ["How will our client stick with the plan?", "How can our client start investing with little money?"]),
 't2': (['why-invest','risk-diversify'], ["What return can our client expect?", "What if the market crashes right after they invest?"]),
 't3': (['tvm','why-invest'], ["How fast will this money grow?", "Why invest now instead of later?"]),
 't4': (['tvm','why-invest'], ["Why should a young client invest now?"]),
 't5': (['inv-types','risk-diversify'], ["Why an index fund instead of picking stocks?", "How much do fees really matter?"]),
 't6': (['why-invest','risk-diversify'], ["Should our client invest all at once or spread it out?", "What if the market drops right after they invest?"]),
 't7': (['inv-types','retire-accounts'], ["What's the simplest investment for a beginner?"]),
 't8': (['why-invest','providers','fed-rates'], ["Where should the emergency fund go?", "Why not just keep savings at a big bank?"]),
 't9': (['budget','goals'], ["How much should our client keep in savings?", "What should our client do first?"]),
 't10': (['budget'], ["How should our client build a budget?"]),
 't11': (['inv-types','market-types'], ["Where should money for a short-term goal go?"]),
 't12': (['inv-types','risk-diversify'], ["What's the difference between a stock and a bond?"]),
 't13': (['retire-accounts','tax-advantaged'], ["How much can our client put in a 401(k) or IRA?"]),
 't14': (['retire-accounts','income-paystub'], ["What should our client do first with their paycheck?", "Which job offer is better?"]),
 't15': (['tax-advantaged','retire-accounts'], ["Roth or traditional?"]),
 't16': (['retire-accounts','laws-regulators'], ["How can a business help employees save?"]),
 't17': (['social-security'], ["When should our client claim Social Security?"]),
 't18': (['college-save'], ["How should parents save for college?"]),
 't19': (['college-save','tax-advantaged'], ["What if the child doesn't go to college?"]),
 't20': (['college-save','tax-advantaged'], ["What accounts can new parents open for their baby?"]),
 't21': (['college-aid'], ["How can our client pay for college?"]),
 't22': (['estate','college-save'], ["How can grandparents help without tax problems?"]),
 't23': (['tax-advantaged','why-invest'], ["How can a teenager start investing?"]),
 't24': (['personal-insurance'], ["How much life insurance does our client need?"]),
 't25': (['personal-insurance'], ["What insurance does a young worker need?"]),
 't26': (['personal-insurance','client-duty'], ["How often should the client review their plan?"]),
 't27': (['personal-insurance','risk-process'], ["How can a wealthier client protect against lawsuits?"]),
 't28': (['tax-advantaged','personal-insurance'], ["How can our client save on health costs?"]),
 't29': (['risk-process','insurance-basics'], ["What's the biggest risk and how would you handle it?"]),
 't30': (['business-insurance'], ["What insurance should this business buy?"]),
 't31': (['credit-score'], ["How can our client improve their credit score?"]),
 't32': (['credit-score','credit-basics'], ["How should our client use credit cards responsibly?"]),
 't33': (['credit-score','identity'], ["How does our client check their credit?", "How do we protect against identity theft?"]),
 't34': (['cost-credit','debt-control'], ["Should our client pay off debt or invest first?"]),
 't35': (['consumer-law','credit-basics'], ["What protections does a cardholder have?"]),
 't36': (['debt-control'], ["How should our client pay off debt?"]),
 't37': (['credit-basics','loans','ratios'], ["What does a lender look at?"]),
 't38': (['deposit-safety'], ["Is our client's money safe at the bank?"]),
 't39': (['deposit-safety','inv-types'], ["What happens if a brokerage firm fails?"]),
 't40': (['deposit-safety','bank-how'], ["Why do banks fail?", "How do we protect a large balance?"]),
 't41': (['deposit-safety','fintech-ai'], ["Is money in a payment app insured?"]),
 't42': (['payments','fintech-ai'], ["How should our client send money safely?"]),
 't43': (['providers'], ["Bank or credit union?"]),
 't44': (['consolidation'], ["How does consolidation affect customers?"]),
 't45': (['consolidation'], ["Why do banks merge?"]),
 't46': (['consolidation','laws-regulators'], ["What is convergence in the finance industry?"]),
 't47': (['fed-rates'], ["How do the Fed's decisions affect our client?"]),
 't48': (['inflation'], ["How does inflation change your recommendation?"]),
 't49': (['loans','fed-rates'], ["Should our client buy a house now?"]),
 't50': (['market-types','risk-diversify','difficult-clients'], ["What if the market drops 20%?"]),
 't51': (['fed-rates','inv-types'], ["Why do bond prices fall when rates rise?"]),
 't52': (['globalization'], ["Should our client invest internationally?"]),
 't53': (['client-duty','ethics'], ["What are your responsibilities to us?"]),
 't54': (['client-duty','laws-regulators'], ["How can the client trust you?"]),
 't55': (['client-duty','crm','consumer-law'], ["How will you protect my information?"]),
 't56': (['accounting-law','governance'], ["How do laws keep company reports honest?"]),
 't57': (['laws-regulators'], ["How do regulations protect consumers?"]),
 't58': (['ethics','erm-controls','governance'], ["Why does ethics matter in finance?"]),
 't59': (['laws-regulators','ethics','inv-types'], ["Should our client invest in crypto?"]),
 't60': (['scams','laws-regulators'], ["How can a client spot investment fraud?"]),
 't61': (['laws-regulators','ethics'], ["What's illegal in securities trading?"]),
 't62': (['compliance','laws-regulators'], ["How do banks stop money laundering?"]),
 't63': (['scams'], ["How big a problem is fraud?"]),
 't64': (['scams','client-duty'], ["How would you protect an older client?"]),
 't65': (['occ-fraud','erm-controls'], ["How would you prevent employee theft?"]),
 't66': (['identity','payments'], ["How should our client secure online accounts?"]),
 't67': (['occ-fraud','fintech-ai'], ["How can data analysis catch fraud?"]),
 't68': (['entrepreneur','biz-budget-cash'], ["What's the biggest risk for this new business?"]),
 't69': (['biz-funding'], ["How should this business get funding?"]),
 't70': (['ownership'], ["What form of ownership do you recommend?"]),
 't71': (['statements','biz-budget-cash'], ["Why is a profitable business short on cash?"]),
 't72': (['finance-role','accounting-law'], ["How would you use technology to manage the business's money?"]),
 't73': (['ratios','biz-funding'], ["How do you know if the business is healthy?"]),
 't74': (['governance'], ["What makes a well-governed company?"]),
 't75': (['governance'], ["Why does governance matter to investors?"]),
 't76': (['erm-controls','governance'], ["What is enterprise risk management?"]),
 't77': (['fintech-ai'], ["What are the risks of banks using AI?"]),
 't78': (['allocation-abc'], ["How can financial information be used beyond accounting?"]),
 't79': (['careers'], ["What finance career interests you, and why?"]),
}
for x in T:
    if x['id'] in TAGS and not x['subs']:
        x['subs'], x['answers'] = TAGS[x['id']][0], TAGS[x['id']][1]
