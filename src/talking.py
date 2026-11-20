# Real-world talking points for FTDM roleplays.
# Each point: topic, PIs it supports, a title, the fact, a line you can say to the judge, and where the fact
# comes from. Time-sensitive numbers carry an "asof" date: re-check them before each competition.
# Facts checked November 2026. Never present a forecast as a fact.
T = []
def t(topic, pis, title, fact, say, source, asof="", subs=None, answers=None):
    # subs: Finance Hub sub-topic ids; answers: judge questions this point helps you answer.
    T.append(dict(id=f"t{len(T)+1}", topic=topic, pis=pis, title=title, fact=fact, say=say, source=source, asof=asof,
                  subs=list(subs or []), answers=list(answers or [])))

# ---------------- Saving and investing ----------------
S = "Saving & investing"
t(S, ["FI:270","FI:077"], "Automatic investing at big brokerages",
  "Fidelity, Charles Schwab and Vanguard all let customers schedule automatic recurring investments into mutual funds or ETFs, and Fidelity and Schwab offer fractional shares, so even small amounts buy part of an S&P 500 fund.",
  "\"We'd automate it: a recurring transfer into an S&P 500 index fund at a brokerage like Fidelity the day after payday, so money that would sit idle starts working right away.\"",
  "Fidelity, Schwab and Vanguard account features")
t(S, ["FI:270","FI:574"], "What the S&P 500 has actually returned",
  "From 1928 through 2025 the S&P 500 compounded at roughly 10% a year including dividends, or about 7% after inflation. Single years swing widely: about -37% in 2008 and about -18% in 2022.",
  "\"Historically the S&P 500 has averaged about 10% a year since 1928. That's an average, not a promise: in 2008 it fell 37%, which is why this is money for five years or more.\"",
  "NYU Stern (Damodaran) historical returns data; S&P Dow Jones Indices")
t(S, ["FI:062","FI:270"], "Rule of 72",
  "Divide 72 by an annual return to estimate how many years money takes to double: at 8% about 9 years, at 4% about 18 years.",
  "\"By the Rule of 72, at 8% your money doubles about every 9 years, so starting at 22 instead of 31 gives you one extra doubling.\"",
  "Standard finance rule of thumb")
t(S, ["FI:062","FI:270"], "Starting early beats investing more later",
  "$200 a month from age 22 to 65 at an 8% average return grows to about $895,000. The same $200 a month started at 32 grows to about $387,000.",
  "\"Waiting ten years cuts the result by more than half. Time is the most valuable thing a young investor has.\"",
  "Future value of an annuity, calculated in this app")
t(S, ["FI:077"], "Index funds are cheap",
  "Broad index funds and ETFs from large providers commonly charge expense ratios under 0.10% a year, and Fidelity offers ZERO index funds with a 0% expense ratio. Many actively managed funds charge 0.5% to 1% or more.",
  "\"A low-cost index fund keeps more of the return in your pocket. A 1% fee can eat roughly a quarter of your money over 30 years.\"",
  "Fund provider fee disclosures; SEC Investor.gov fee calculator")
t(S, ["FI:077"], "Dollar-cost averaging",
  "Investing a fixed amount on a schedule buys more shares when prices fall and fewer when they rise, and removes the temptation to time the market.",
  "\"With dollar-cost averaging, a market dip becomes a sale: your same $300 buys more shares.\"",
  "SEC Investor.gov glossary")
t(S, ["FI:077","FI:569"], "Target-date funds",
  "Target-date funds hold a stock and bond mix that automatically becomes more conservative as the target year nears. They are the default investment in many 401(k) plans.",
  "\"If you want one decision and done, a 2070 target-date fund diversifies and rebalances for you.\"",
  "SEC Investor Bulletin on target date funds")
t(S, ["FI:270","FI:337"], "High-yield savings rates right now",
  "In mid-November 2026, top online high-yield savings accounts paid about 4.35% APY (some with balance minimums), while many big-bank basic savings accounts pay far less.",
  "\"Your emergency fund shouldn't earn almost nothing. Top online savings accounts pay around 4% right now and are still FDIC-insured.\"",
  "Bankrate best high-yield savings, rates as of 11/12/2026", "Nov 2026")
t(S, ["FI:270"], "Emergency fund guideline",
  "Most planners recommend 3 to 6 months of essential expenses in cash before investing beyond an employer match; single-income or commission-based households often aim for 6 or more.",
  "\"Step one is protection: three to six months of expenses in high-yield savings, so a car repair never becomes credit card debt.\"",
  "CFPB and common financial-planning guidance")
t(S, ["FI:066","FI:065"], "50/30/20 budget",
  "A simple guideline: 50% of after-tax pay to needs, 30% to wants, 20% to savings and extra debt payments.",
  "\"We'd start with 50/30/20: it's simple enough to stick to and it guarantees 20% goes to your future.\"",
  "Popularized by Sen. Elizabeth Warren's book 'All Your Worth' (2005)")
t(S, ["FI:077","FI:337"], "CDs and Treasury bills for short-term goals",
  "CDs lock a fixed rate for a set term with a penalty for early withdrawal. Treasury bills are short-term U.S. government debt (4 to 52 weeks), sold at TreasuryDirect.gov or through brokerages, and their interest is exempt from state income tax.",
  "\"For your house down payment in two years, we'd use a CD ladder or Treasury bills: safe, predictable, and not exposed to a stock market drop right before you buy.\"",
  "TreasuryDirect.gov; FDIC")
t(S, ["FI:077"], "Stocks vs bonds in one line",
  "A stock is ownership in a company; a bond is a loan to a company or government that pays interest. Bonds are usually steadier; stocks have higher long-run returns and bigger swings.",
  "\"Stocks are for growth, bonds are for stability, and the mix depends on when you need the money.\"",
  "SEC Investor.gov")

# ---------------- Retirement ----------------
R = "Retirement"
t(R, ["FI:569"], "401(k) and IRA limits for 2026 and 2027",
  "2026: 401(k) employee limit $24,500; IRA $7,500. 2027 (IRS Notice 2026-66, Nov. 12, 2026): 401(k) $25,500, catch-up for 50+ $8,500, higher catch-up of $11,750 for ages 60-63; IRA stays $7,500 with a $1,100 catch-up.",
  "\"Next year you can put up to $25,500 into your 401(k), and if you're over 50 another $8,500 on top.\"",
  "IRS release IR-2026-136 / Notice 2026-66", "Nov 2026")
t(R, ["FI:569","FI:270"], "The employer match is free money",
  "A common match is 50% or 100% of contributions up to 3% to 6% of salary. Not contributing enough to get the full match leaves part of your pay on the table.",
  "\"If your company matches 4%, contributing 4% is an instant 100% return. Nothing else in finance does that.\"",
  "Typical plan design (Vanguard 'How America Saves' reports)")
t(R, ["FI:569","BL:134"], "Roth vs traditional",
  "Traditional 401(k)/IRA: tax break now, taxed at withdrawal. Roth: contributions after tax, qualified withdrawals tax-free. Roth tends to win when your tax rate is low now (young workers).",
  "\"You're in a low tax bracket now, so paying tax today with a Roth and withdrawing tax-free later is the smart trade.\"",
  "IRS Publication 590-A/590-B")
t(R, ["FI:569"], "Auto-enrollment under SECURE 2.0",
  "SECURE 2.0 (2022) requires most new 401(k) and 403(b) plans started after Dec. 29, 2022 to automatically enroll workers beginning with plan years after 2024, at 3% to 10% with automatic yearly increases.",
  "\"Congress made automatic saving the default in new plans because it works: people who are auto-enrolled stay enrolled.\"",
  "SECURE 2.0 Act of 2022, Section 101")
t(R, ["FI:569"], "Social Security timing",
  "You can claim Social Security from 62 to 70. Each year you wait past full retirement age (67 for anyone born 1960 or later) adds about 8% to your monthly benefit until 70.",
  "\"Delaying Social Security from 67 to 70 raises your check by roughly 24% for life.\"",
  "Social Security Administration (ssa.gov)")

# ---------------- Kids and college ----------------
K = "Kids & college"
t(K, ["FI:831","FI:062"], "529 plans",
  "529 plans grow tax-free when used for qualified education expenses (college costs, plus K-12 tuition up to an annual cap). Many states give a state income tax deduction for contributions.",
  "\"A 529 plan for your daughter grows tax-free for college, and many states give you a tax break when you put money in.\"",
  "IRS Publication 970; SEC Investor.gov on 529 plans")
t(K, ["FI:831","FI:569"], "529 to Roth IRA rollover",
  "Under SECURE 2.0, starting in 2024 unused 529 money can roll into the beneficiary's Roth IRA, up to $35,000 lifetime, if the 529 has been open at least 15 years, subject to annual Roth limits.",
  "\"If your child gets a scholarship, the money isn't stuck: up to $35,000 can roll into their Roth IRA.\"",
  "SECURE 2.0 Act, Section 126")
t(K, ["FI:831","FI:270","FI:077"], "Trump Accounts for newborns",
  "The 2025 tax law created Trump Accounts: children who are U.S. citizens born from 2025 through 2028 can get a one-time $1,000 federal seed deposit (claimed on IRS Form 4547). Contributions began July 4, 2026, up to $5,000 a year from family and others (employers up to $2,500 of that), invested in low-cost U.S. stock index funds. IRS rules were still proposed as of mid-2026.",
  "\"Because your baby was born this year, they qualify for a $1,000 government deposit in a Trump Account. We'd claim it right away and add to it every month.\"",
  "One Big Beautiful Bill Act (2025); IRS proposed regulations (May 2026); trumpaccounts.gov", "Nov 2026")
t(K, ["FI:831"], "FAFSA",
  "The Free Application for Federal Student Aid (studentaid.gov) unlocks federal grants, work-study and federal loans; many states and colleges use it for their own aid. File every year, as early as possible.",
  "\"Before borrowing a dollar, file the FAFSA: it's free and it's the key to grants you never repay.\"",
  "U.S. Department of Education, studentaid.gov")
t(K, ["FI:065","BL:134"], "Annual gift tax exclusion",
  "In 2026 a person can give up to $19,000 to any one person without filing a gift tax return; a married couple can give $38,000 per recipient. The limit rises to $20,000 ($40,000 per couple) in 2027. A 529 allows five years of gifts at once ($95,000 in 2026).",
  "\"Grandparents can each give $19,000 a year per grandchild with no gift tax paperwork, and a 529 lets them front-load five years.\"",
  "IRS annual exclusion for 2026; IRS Rev. Proc. 2026-35 for 2027", "Nov 2026")
t(K, ["FI:061","FI:569"], "Custodial Roth IRA for teens",
  "A teen with earned income (a part-time job) can have a custodial Roth IRA and contribute up to the lesser of their earnings or the annual limit.",
  "\"With your summer job income, you could open a custodial Roth IRA now and give that money 50 years to grow tax-free.\"",
  "IRS Publication 590-A")

# ---------------- Insurance and risk for families ----------------
I = "Insurance"
t(I, ["FI:571","FI:081"], "How much life insurance",
  "A common rule of thumb is coverage of 10 to 12 times annual income; the DIME method adds Debt, Income replacement, Mortgage and Education costs. Term life is far cheaper than whole life for the same coverage.",
  "\"For a new parent we'd look at term life of about 10 to 12 times income, a 20- or 30-year term to cover the years your child depends on you.\"",
  "Common planning guidelines (e.g., LIMRA consumer research, insurer calculators)")
t(I, ["FI:571"], "Disability insurance",
  "Long-term disability insurance usually replaces about 60% of income. The Social Security Administration estimates about 1 in 4 of today's 20-year-olds will become disabled before retirement age.",
  "\"Your ability to earn is your biggest asset. Disability coverage protects it: about 1 in 4 of today's 20-year-olds will face a disability before 67.\"",
  "Social Security Administration fact sheet")
t(I, ["FI:571","FI:081"], "Life events trigger a review",
  "Marriage, a new baby, buying a home, starting a business and a new job are the moments to review life, disability, health, property and liability coverage and update beneficiaries.",
  "\"A new baby is the number-one moment to review insurance and beneficiaries. We'd do it this month.\"",
  "Standard planning practice")
t(I, ["FI:571"], "Umbrella liability",
  "Umbrella policies add liability coverage (often $1 million or more) above home and auto limits and are relatively inexpensive.",
  "\"As your net worth grows, an umbrella policy protects it from a lawsuit for roughly the cost of a streaming subscription a month.\"",
  "Insurance Information Institute (iii.org)")
t(I, ["FI:571","FI:081"], "HSA limits for 2026 and 2027",
  "With a high-deductible health plan, HSA contribution limits are $4,400 (self-only) and $8,750 (family) for 2026, rising to $4,500 and $9,000 for 2027. HSAs are triple tax-advantaged: deductible in, tax-free growth, tax-free out for medical costs.",
  "\"If you have a high-deductible plan, the HSA is the best tax deal in the code: money goes in tax-free and comes out tax-free for medical bills.\"",
  "IRS Rev. Proc. 2025-19 (2026) and Rev. Proc. 2026-24 (2027)", "Nov 2026")
t(I, ["SM:075","RM:058"], "Four ways to handle risk",
  "Avoid it (don't do the activity), reduce/control it (safety steps, internal controls), transfer it (insurance, contracts), or retain/accept it (self-insure small losses).",
  "\"For each risk we'd decide: avoid it, reduce it, transfer it with insurance, or accept it. Here's which we chose and why.\"",
  "Standard risk-management framework")
t(I, ["FI:571","EN:039"], "Small business insurance basics",
  "Common coverages: general liability, commercial property, a business owner's policy (BOP) bundling both, professional liability, commercial auto, cyber, and workers' compensation (required in nearly every state once you have employees).",
  "\"We'd start with a business owner's policy and add workers' comp the day you hire your first employee.\"",
  "U.S. Small Business Administration (sba.gov)")

# ---------------- Credit ----------------
C = "Credit & debt"
t(C, ["FI:071","FI:072"], "What makes up a FICO score",
  "Payment history 35%, amounts owed (utilization) 30%, length of credit history 15%, new credit 10%, credit mix 10%.",
  "\"The two biggest levers are paying on time, 35% of your score, and keeping balances low, 30%.\"",
  "myFICO.com")
t(C, ["FI:071"], "Utilization under 30%",
  "Using less than 30% of available credit is a widely cited guideline; people with the highest scores often use under 10%.",
  "\"Keep your card balance under 30% of the limit, and under 10% if you're about to apply for a mortgage.\"",
  "Experian, myFICO guidance")
t(C, ["FI:072","FI:073"], "Free credit reports and freezes",
  "AnnualCreditReport.com gives free weekly reports from Equifax, Experian and TransUnion (made permanent in 2023). Credit freezes have been free at all three bureaus since 2018.",
  "\"Check all three reports free every week at AnnualCreditReport.com, and freeze your credit for free so no one can open accounts in your name.\"",
  "FTC; Economic Growth, Regulatory Relief and Consumer Protection Act (2018)")
t(C, ["FI:782","FI:002"], "Credit card interest is expensive",
  "Average interest rates on credit card accounts that pay interest have been above 20% in recent years, according to Federal Reserve G.19 data.",
  "\"Carrying a balance at over 20% APR wipes out any investment return, so we pay the card in full every month on autopay.\"",
  "Federal Reserve G.19 Consumer Credit release")
t(C, ["FI:063","FI:071"], "CARD Act protections",
  "The Credit CARD Act of 2009 requires 45 days' notice of major rate changes, limits fees, and requires statements to show how long paying only the minimum will take.",
  "\"Look at the minimum-payment box on your statement: the CARD Act requires it to show how many years minimums would take.\"",
  "Credit CARD Act of 2009; CFPB")
t(C, ["FI:568"], "Avalanche vs snowball",
  "Avalanche pays the highest interest rate first (saves the most); snowball pays the smallest balance first (quick wins that build motivation).",
  "\"Mathematically, the avalanche saves you the most interest. If you need early wins to stay motivated, the snowball works too.\"",
  "CFPB debt guidance")
t(C, ["FI:002","FI:625"], "Five Cs of credit",
  "Lenders judge Character, Capacity (ability to repay), Capital, Collateral and Conditions.",
  "\"A lender looks at the five Cs, so we'd strengthen capacity by lowering your debt-to-income ratio before you apply.\"",
  "Standard lending framework")

# ---------------- Institutions, safety, payments ----------------
B = "Banks, safety & payments"
t(B, ["FI:336","RM:043"], "FDIC and NCUA insurance",
  "The FDIC insures deposits up to $250,000 per depositor, per insured bank, per ownership category; the NCUA gives credit union members the same coverage. No depositor has lost a penny of FDIC-insured funds since the FDIC began in 1934.",
  "\"Your deposits are FDIC-insured up to $250,000. Since 1934 no one has lost a penny of insured deposits.\"",
  "FDIC.gov; NCUA.gov")
t(B, ["FI:336"], "SIPC protection at brokerages",
  "SIPC protects customers up to $500,000 (including $250,000 cash) if a member brokerage fails and assets are missing. It does not protect against market losses.",
  "\"If the brokerage itself failed, SIPC covers up to $500,000. Market drops aren't covered, which is why we diversify.\"",
  "SIPC.org")
t(B, ["FI:336","RM:062"], "Silicon Valley Bank, 2023",
  "In March 2023 Silicon Valley Bank failed after depositors tried to withdraw about $42 billion in one day; most deposits were uninsured and the bank held long-term bonds that lost value when rates rose. Regulators protected all depositors.",
  "\"SVB shows two risks: keeping balances over the insurance limit, and a bank not managing interest-rate risk. We'd spread large balances across banks.\"",
  "Federal Reserve review of SVB (April 2023); FDIC")
t(B, ["FI:336","FI:830"], "Synapse fintech collapse, 2024",
  "When banking-as-a-service middleman Synapse filed for bankruptcy in 2024, customers of several fintech apps had their money frozen because records of who owned what didn't match. FDIC insurance protects you if the bank fails, not if a fintech middleman fails.",
  "\"Before you trust an app with your savings, know which bank actually holds the money and whether you're covered if the app itself fails.\"",
  "News coverage; FDIC consumer guidance on fintech")
t(B, ["FI:058","NF:003"], "Instant payments: FedNow and Zelle",
  "The Federal Reserve launched FedNow, an instant payment service for banks, in July 2023. Zelle, owned by seven large banks, moves money between U.S. bank accounts in minutes.",
  "\"Instant payments through FedNow and Zelle mean customers expect money to move in seconds, so the bank's app has to keep up.\"",
  "Federal Reserve; Early Warning Services")
t(B, ["FI:336","FI:076"], "Credit unions vs banks",
  "Credit unions are not-for-profit cooperatives owned by members; they often offer lower loan rates and fees. Banks are usually for-profit and owned by shareholders, with larger branch and ATM networks.",
  "\"A credit union returns profits to members through better rates; a big bank offers more locations and services. It depends on what you value.\"",
  "NCUA; FDIC")
t(B, ["FI:573"], "Fewer, bigger banks",
  "The number of FDIC-insured institutions has fallen from more than 14,000 in the mid-1980s to fewer than 4,500, mostly through mergers.",
  "\"Banking has consolidated dramatically: there are less than a third as many banks as in the 1980s.\"",
  "FDIC historical statistics on banking")
t(B, ["FI:573"], "Recent consolidation deals",
  "JPMorgan Chase bought First Republic Bank after it failed in May 2023. Capital One completed its acquisition of Discover Financial in May 2025, combining a big card issuer with a payment network.",
  "\"Capital One buying Discover is a great example: a lender buying a payment network to control more of the value chain.\"",
  "FDIC (2023); Capital One press release (May 2025)")
t(B, ["FI:573"], "Convergence: Citigroup and Gramm-Leach-Bliley",
  "Citicorp (a bank) merged with Travelers Group (insurance and brokerage) in 1998 to form Citigroup. The Gramm-Leach-Bliley Act of 1999 then legally allowed banks, securities firms and insurers to combine.",
  "\"Convergence means one company offering banking, investing and insurance, which became legal with Gramm-Leach-Bliley in 1999.\"",
  "Federal Reserve history; GLBA (1999)")

# ---------------- Economy and markets now ----------------
E = "Economy right now"
t(E, ["FI:574","EC:084"], "Federal funds rate",
  "The Fed raised its target range by 0.25 point to 3.75%-4.00% on Sept. 16, 2026 and held it there on Oct. 28, 2026 (10-2 vote; two members wanted another hike). The next meeting is Dec. 8-9, 2026.",
  "\"The Fed raised rates in September to fight inflation. That makes borrowing costlier but means savers can lock in about 4% safely right now.\"",
  "Federal Reserve FOMC statements, Sept. 16 and Oct. 28, 2026", "Nov 2026")
t(E, ["EC:083","FI:574"], "Inflation",
  "Consumer prices rose 3.7% in the 12 months through September 2026, above the Fed's 2% target, driven in part by energy (gasoline spiked above $4.50 a gallon in spring 2026). October CPI rose 0.4% for the month; no 12-month figure was published for October because 2025 data were missing.",
  "\"With inflation near 3.7%, money in a 0.25% savings account loses buying power every year.\"",
  "Bureau of Labor Statistics CPI releases, 2026", "Nov 2026")
t(E, ["FI:574","EC:084"], "Mortgage rates",
  "The average 30-year fixed mortgage rate was about 7.11% in Freddie Mac's survey for the week of Nov. 12, 2026 (15-year about 6.45%).",
  "\"Mortgage rates are around 7%, so improving your credit score before you buy could save you a lot over 30 years.\"",
  "Freddie Mac Primary Mortgage Market Survey", "Nov 2026")
t(E, ["FI:574"], "Bull, bear and correction",
  "A correction is a drop of about 10% from a recent high; a bear market is a drop of 20% or more; a bull market is a long rise. Recessions are officially dated by the National Bureau of Economic Research.",
  "\"Corrections of 10% happen often. Long-term investors plan for them instead of reacting to them.\"",
  "SEC Investor.gov; NBER")
t(E, ["FI:574"], "Rates and bond prices move opposite",
  "When interest rates rise, prices of existing bonds fall, and long-term bonds fall the most. This is exactly what hurt Silicon Valley Bank in 2023.",
  "\"Because rates rose, we'd favor shorter-term bonds and CDs so the client isn't locked into low rates.\"",
  "SEC Investor.gov on interest rate risk")
t(E, ["FI:575","EC:100"], "Global investing and currency risk",
  "U.S. companies make up roughly 60% of global stock market value, so a U.S.-only portfolio skips a large part of the world. Foreign investments add currency risk: a stronger dollar lowers the value of foreign returns.",
  "\"Owning some international funds adds diversification, but returns move with exchange rates too.\"",
  "MSCI All Country World Index country weights")

# ---------------- Client service, ethics, regulation ----------------
P = "Client trust & regulation"
t(P, ["CR:012","EI:128"], "Fiduciary vs best interest",
  "Registered investment advisers owe clients a fiduciary duty under the Investment Advisers Act of 1940. Broker-dealers must follow Regulation Best Interest (effective June 2020) when recommending investments to retail customers. CFP professionals must act as fiduciaries when giving financial advice.",
  "\"We act in your best interest, we disclose how we're paid, and we put every recommendation and its reasons in writing.\"",
  "SEC (Advisers Act; Reg BI); CFP Board Code of Ethics")
t(P, ["CR:012","BL:133"], "Check any advisor yourself",
  "FINRA BrokerCheck and the SEC's Investment Adviser Public Disclosure site show licenses, employment history and disciplinary records. Investor.gov links to both.",
  "\"Don't take our word for it: look us up on FINRA BrokerCheck tonight and see our licenses and record.\"",
  "FINRA.org; SEC Investor.gov")
t(P, ["CR:012","OP:441"], "Client privacy",
  "The Gramm-Leach-Bliley Act requires financial institutions to explain how they share customer information and to safeguard it (the Safeguards Rule).",
  "\"Your information is protected by federal privacy law, and we'll explain exactly who can see it.\"",
  "FTC Gramm-Leach-Bliley Act guidance")
t(P, ["BL:133","PD:214"], "Sarbanes-Oxley",
  "Passed in 2002 after Enron and WorldCom, Sarbanes-Oxley requires CEOs and CFOs to certify financial reports (Section 302), requires internal-control reporting and auditor attestation (Section 404), and created the PCAOB to oversee auditors.",
  "\"After Enron, Sarbanes-Oxley made executives personally sign off on the numbers. That's the standard we'd hold this company to.\"",
  "Sarbanes-Oxley Act of 2002")
t(P, ["BL:133","FI:063"], "Dodd-Frank and the CFPB",
  "The Dodd-Frank Act (2010), the response to the 2008 crisis, created the Consumer Financial Protection Bureau, the Financial Stability Oversight Council, stress tests for large banks, and the Volcker Rule.",
  "\"After 2008, Dodd-Frank created the CFPB so consumers have a regulator focused only on them.\"",
  "Dodd-Frank Wall Street Reform and Consumer Protection Act")
t(P, ["BL:133","EI:131"], "Wells Fargo fake accounts",
  "Wells Fargo employees opened millions of unauthorized accounts under aggressive sales goals (revealed in 2016). The bank paid $3 billion to settle criminal and civil cases in 2020 and $3.7 billion to the CFPB in 2022.",
  "\"Wells Fargo shows what happens when sales goals reward the wrong behavior. We'd measure client outcomes, not just products sold.\"",
  "U.S. Department of Justice (2020); CFPB (2022)")
t(P, ["BL:133","RM:041"], "FTX fraud",
  "Crypto exchange FTX collapsed in November 2022 after customer funds were secretly used by an affiliated trading firm. Founder Sam Bankman-Fried was convicted of fraud in 2023 and sentenced to 25 years in 2024.",
  "\"FTX had no real board, no controls and customer money mixed with company money. Governance and segregation of funds matter.\"",
  "U.S. Department of Justice")
t(P, ["BL:133"], "Ponzi warning signs",
  "Bernard Madoff's Ponzi scheme, exposed in 2008, involved about $65 billion in reported (fictitious) account value. Red flags: guaranteed or unusually steady high returns, secrecy, unregistered sellers, pressure to act fast.",
  "\"Anyone promising guaranteed high returns is a red flag. Madoff's steady returns were the tell.\"",
  "SEC; U.S. Department of Justice")
t(P, ["BL:133"], "Insider trading case",
  "Galleon Group founder Raj Rajaratnam was sentenced in 2011 to 11 years in prison for insider trading, one of the longest sentences for the crime.",
  "\"Trading on information the public doesn't have is illegal. Rajaratnam got 11 years.\"",
  "U.S. Department of Justice (2011)")
t(P, ["BL:148"], "Anti-money-laundering rules",
  "Under the Bank Secrecy Act, banks file Currency Transaction Reports for cash transactions over $10,000 and Suspicious Activity Reports, and must verify customer identity (KYC).",
  "\"Compliance isn't red tape: KYC and transaction monitoring keep criminals out and protect the bank's reputation.\"",
  "FinCEN")

# ---------------- Fraud and scams ----------------
F = "Fraud & scams"
t(F, ["FI:073","RM:042"], "Consumer fraud losses",
  "Consumers reported losing a record $15.9 billion to fraud in 2025, up about 25% from 2024, according to the FTC. Investment scams were the largest category at about $7.9 billion, nearly half the total.",
  "\"Fraud is growing fast: the FTC counted a record $15.9 billion in reported losses in 2025, so scam protection belongs in every plan.\"",
  "FTC Consumer Sentinel data (2026)", "2026")
t(F, ["FI:073","EI:030"], "Older adults are top targets",
  "The FBI's Internet Crime Complaint Center reported that people 60 and older lost about $4.9 billion to online fraud in 2024.",
  "\"Older clients are targeted most, so we'd add a trusted contact to your account and a verbal password with the bank.\"",
  "FBI IC3 Elder Fraud Report 2024")
t(F, ["RM:058","FM:014"], "Occupational fraud",
  "The Association of Certified Fraud Examiners estimates organizations lose about 5% of revenue to fraud each year; tips are the most common way fraud is detected, and small businesses suffer high median losses.",
  "\"Fraud costs the typical organization about 5% of revenue. A tip line and separation of duties are the cheapest defenses.\"",
  "ACFE Occupational Fraud Report to the Nations")
t(F, ["FI:830","OP:064"], "Multifactor authentication",
  "Microsoft has reported that multifactor authentication blocks more than 99% of automated account-compromise attacks. Authenticator apps or passkeys are stronger than text-message codes.",
  "\"Turning on multifactor authentication stops almost all automated account takeovers.\"",
  "Microsoft security research")
t(F, ["NF:124","FM:014"], "Benford's Law",
  "In many naturally occurring financial data sets, about 30% of numbers start with 1 and fewer than 5% start with 9. Auditors use this to spot made-up numbers.",
  "\"We'd run a Benford's Law test on expense data: fabricated numbers rarely follow the natural pattern.\"",
  "Nigrini, Benford's Law (forensic accounting)")

# ---------------- Business finance and small business ----------------
SB = "Small business"
t(SB, ["EN:039","FI:579"], "How many new businesses survive",
  "About 1 in 5 new U.S. businesses close within their first year and roughly half within five years.",
  "\"About half of new businesses don't reach year five, usually because of cash flow, so we'd build a cash budget before you open.\"",
  "Bureau of Labor Statistics Business Employment Dynamics")
t(SB, ["FI:002","EN:039"], "SBA loans",
  "SBA 7(a) loans go up to $5 million; SBA microloans go up to $50,000 through nonprofit intermediaries. The SBA guarantees part of the loan, making lenders more willing to lend.",
  "\"An SBA microloan of up to $50,000 fits a start-up like yours, and the government guarantee helps a new business qualify.\"",
  "U.S. Small Business Administration (sba.gov)")
t(SB, ["BL:003"], "Business structures",
  "Sole proprietorship: simplest, unlimited personal liability. Partnership: shared ownership, needs a partnership agreement. LLC: limited liability with pass-through taxes. S corp: pass-through taxation, up to 100 shareholders. C corp: separate taxpayer, can raise money by selling stock.",
  "\"For you and your friend, an LLC with a written operating agreement protects your personal assets and spells out what happens if one of you leaves.\"",
  "IRS business structures guidance; SBA")
t(SB, ["FI:091","FI:106"], "Profit is not cash",
  "A business can be profitable on its income statement and still run out of cash if customers pay late, inventory piles up or loan payments are due. That's why a cash flow budget matters.",
  "\"Profit is an opinion, cash is a fact: we'd build a 13-week cash forecast so you see a crunch before it hits.\"",
  "Standard financial management principle")
t(SB, ["FM:013","FI:352"], "Small business finance tools",
  "Cloud accounting software such as QuickBooks Online and Xero connects to bank accounts, automates bookkeeping and produces income statements, balance sheets and cash flow reports; payroll tools like Gusto handle tax withholding.",
  "\"With QuickBooks or Xero linked to your bank, your financial statements update themselves and your accountant sees the same numbers you do.\"",
  "Vendor product information")
t(SB, ["FI:093","FM:009"], "Ratios lenders check",
  "Current ratio (current assets ÷ current liabilities; above 1.5 is generally healthy), debt-to-equity, net profit margin, and debt service coverage (operating cash flow ÷ debt payments; lenders often look for 1.25 or more).",
  "\"Banks want to see your cash flow cover loan payments at least 1.25 times, so we'd show them that number up front.\"",
  "Common commercial lending standards")

# ---------------- Governance, risk and technology in the industry ----------------
G = "Governance & industry trends"
t(G, ["PD:213","PD:214"], "Board independence",
  "NYSE and Nasdaq listing rules require a majority of independent directors and a fully independent audit committee. Separating the CEO and board chair roles adds oversight.",
  "\"Investors want an independent board and audit committee; that's a listing requirement and it raises what investors will pay.\"",
  "NYSE Listed Company Manual 303A; Nasdaq Rule 5605")
t(G, ["PD:213","PD:302"], "WeWork's failed 2019 IPO",
  "WeWork withdrew its 2019 IPO after investors objected to governance problems, including the founder's outsized voting control and conflicts of interest; the company later filed for bankruptcy in 2023.",
  "\"WeWork proves governance affects value: investors walked away from the IPO because one person controlled everything.\"",
  "SEC filings; news coverage")
t(G, ["RM:062","RM:058"], "COSO frameworks",
  "COSO's Internal Control-Integrated Framework (2013) and Enterprise Risk Management framework (2017) are the most widely used standards for internal control and ERM.",
  "\"We'd follow the COSO framework so risks are managed across the whole company, not in silos.\"",
  "COSO.org")
t(G, ["RM:042","FM:011"], "AI in financial services",
  "Banks and card networks use machine learning to score transactions for fraud in real time, and many firms use AI to answer customer questions and summarize documents, with human review for decisions.",
  "\"AI can flag suspicious transactions in milliseconds, but a person should review any decision that affects a customer.\"",
  "Industry practice; company disclosures")
t(G, ["FM:016","PD:213"], "Sustainability reporting",
  "The International Sustainability Standards Board issued IFRS S1 and S2 in 2023 as a global baseline for sustainability and climate-related disclosures, and several countries are adopting them.",
  "\"Investors increasingly ask for sustainability data next to financial results, so we'd report a few key measures now.\"",
  "IFRS Foundation (ISSB)")
t(G, ["PD:152"], "Finance careers and credentials",
  "CFP (financial planning), CPA (accounting), CFA (investment analysis), and FINRA licenses such as the Series 7 and 66 for brokers and advisers. Personal financial advisors earned a median of roughly $100,000 a year in recent BLS data.",
  "\"Our team would include a CFP for planning and a CPA for tax questions, so every part of your plan is covered.\"",
  "Bureau of Labor Statistics Occupational Outlook Handbook; CFP Board; FINRA")
