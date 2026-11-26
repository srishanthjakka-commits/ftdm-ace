# Economics talking points for the Econ Lab (added Nov 2026; the regional FTDM roleplay focuses on Economics).
# build_data.py runs this file in the same namespace as talking.py and talking_b.py, so t() and T already exist.
# Each point lists Finance Hub sub-topics and the judge questions it helps answer. Facts checked Nov 2026.
E = "Economics"

# ---- Indicators and the cycle ----
t(E, ["EC:013","EC:083"], "Productivity jumped 3.6%",
  "U.S. nonfarm business productivity rose at a 3.6% annual rate in the third quarter of 2026 and 2.1% over the past year, while unit labor costs fell 0.7%.",
  "\"Productivity grew 3.6% last quarter, so businesses are getting more done per hour. That lets them raise pay without raising prices, which is good news for inflation.\"",
  "BLS Productivity and Costs, preliminary (Nov. 5, 2026)", "Nov 2026", ["indicators-cycle"],
  ["How could this business get more done without hiring?", "Why does productivity matter for the whole economy?"])
t(E, ["EC:081"], "Consumer sentiment is recovering from a record low",
  "The University of Michigan's consumer sentiment index rose to a preliminary 51.0 in November 2026 from 48.0 in October. It hit a record low of 44.8 in May 2026 as gasoline prices climbed. Year-ahead inflation expectations eased to 4.3%.",
  "\"Consumers are still gloomy, with sentiment at 51 compared with a record low of 44.8 in May, so we'd plan for cautious spending rather than a boom.\"",
  "University of Michigan Surveys of Consumers (preliminary, Nov. 2026)", "Nov 2026", ["indicators-cycle"],
  ["Consumers say they feel gloomy but keep spending. Which should a business believe?", "What would falling consumer spending mean for this retailer's loan?"])
t(E, ["EC:081","EC:083"], "Spending up, but not after inflation",
  "In September 2026, consumer spending rose 0.5%, but after adjusting for inflation real spending grew less than 0.1%. The personal saving rate was 3.8%, and the PCE price index was up 3.6% from a year earlier (core 3.1%).",
  "\"People spent 0.5% more in September, but prices rose almost as much, so they bought about the same amount. With savings at just 3.8% of income, families have a thin cushion.\"",
  "BEA Personal Income and Outlays (Oct. 29, 2026)", "Nov 2026", ["indicators-cycle","inflation"],
  ["What would falling consumer spending mean for this retailer's loan?", "Should this business raise prices because of inflation?"])
t(E, ["EC:084"], "The prime rate is about 7%",
  "Most banks set the prime rate at the top of the Fed's target range plus 3 percentage points. With the Fed's range at 3.75%-4.00% after Sept. 16, 2026, prime is about 7.00%. Credit cards, home equity lines and many business lines of credit are priced above prime.",
  "\"With prime around 7%, a business line of credit at prime plus 2 costs about 9%. That's why we'd move this long-term balance into a fixed-rate loan.\"",
  "Federal Reserve FOMC statement (Sept. 16, 2026); prime rate convention", "Nov 2026", ["fed-rates","loans"],
  ["Should this business borrow now or wait for rates to fall?", "How do rising rates help or hurt our client?"])
t(E, ["EC:018"], "Recessions vary a lot in length",
  "The Great Recession lasted 18 months (December 2007 to June 2009). The 2020 recession lasted just two months (February to April 2020), the shortest on record. The National Bureau of Economic Research officially dates U.S. recessions.",
  "\"Recessions are normal and they end: the 2020 one lasted two months, the 2008 one 18. A business that holds six months of cash can ride out either.\"",
  "National Bureau of Economic Research business cycle dates", "", ["indicators-cycle"],
  ["How should this business prepare for the next recession?", "Which phase of the business cycle are we in right now, and why does it matter?"])
t(E, ["EC:082"], "Unemployment hit 14.8% in 2020",
  "The unemployment rate jumped to 14.8% in April 2020, the highest since the BLS began tracking in 1948, then fell back below 4% within about two years.",
  "\"In April 2020 unemployment hit 14.8% almost overnight. Nobody plans to lose their job, which is why we start every plan with an emergency fund.\"",
  "BLS Current Population Survey", "", ["indicators-cycle","budget"],
  ["If our client lost their job tomorrow, what would protect them?"])

# ---- Trade and globalization ----
t(E, ["EC:016"], "Trade deficit: $105 billion in September",
  "The U.S. goods and services trade deficit was $105.0 billion in September 2026. Exports rose to $321.5 billion and imports reached a record $426.6 billion. Through the first nine months of 2026 the deficit was 12.2% smaller than a year earlier.",
  "\"The U.S. bought $105 billion more from the world than it sold in September. Imports hit a record, so import costs matter for this business.\"",
  "U.S. Census Bureau and BEA, U.S. International Trade in Goods and Services (Nov. 4, 2026)", "Nov 2026", ["globalization"],
  ["Is a trade deficit bad for the U.S.?", "How do tariffs affect this importer's costs and its customers?"])
t(E, ["EC:016","EC:008","EC:113"], "The Supreme Court tariff ruling",
  "On Feb. 20, 2026, the Supreme Court ruled 6-3 in Learning Resources v. Trump that the International Emergency Economic Powers Act (IEEPA) does not authorize tariffs. Tariffs under other laws, such as Section 232 (national security) and Section 301 (unfair trade), stayed in place, and refunds were left to the Court of International Trade.",
  "\"Trade rules have changed fast this year: the Supreme Court struck down tariffs under one emergency law in February, but others remain. That uncertainty is why we'd add a second supplier.\"",
  "U.S. Supreme Court, Learning Resources, Inc. v. Trump (2026); Congressional Research Service", "2026", ["globalization","laws-regulators"],
  ["How do tariffs affect this importer's costs and its customers?", "What happens to this business if a trade agreement changes?"])
t(E, ["EC:016","EC:010"], "The average tariff rate",
  "The average effective U.S. tariff rate, meaning tariff revenue as a share of import value, was about 6.7% in July 2026. China faced the highest effective rate, about 22.8%.",
  "\"On average, imports now carry about a 6.7% tariff, and goods from China about 23%. For a shop buying parts from China, that cost goes straight into the price or out of the profit.\"",
  "Penn Wharton Budget Model, Effective Tariff Rates and Revenues (Sept. 9, 2026)", "Sept 2026", ["globalization","biz-risk-profit"],
  ["How do tariffs affect this importer's costs and its customers?", "How can this business raise profit without raising prices?"])
t(E, ["EC:112","EC:105"], "USMCA now faces annual reviews",
  "At USMCA's first joint review on July 1, 2026, the U.S. declined to renew the agreement in its current form. That triggers annual reviews. The agreement remains fully in force and runs to July 1, 2036 unless the countries extend it.",
  "\"USMCA still lets qualifying goods cross the border tariff-free, but it now gets reviewed every year, so we'd plan for the rules to change.\"",
  "USTR statement (July 2026); White & Case analysis", "July 2026", ["globalization"],
  ["How does USMCA help this business that buys parts from Mexico?", "What happens to this business if a trade agreement changes?"])
t(E, ["EC:100"], "The strong dollar",
  "In mid-November 2026, one dollar bought about 159 Japanese yen, near the 160 level where Japan has intervened before, and the euro had fallen about 5% against the dollar since late August as markets expected higher U.S. rates.",
  "\"The dollar is strong right now, so American products cost more for foreign buyers. An exporter should consider locking in exchange rates with a forward contract.\"",
  "Reuters (Nov. 17, 2026); FXStreet; Trading Economics (Nov. 2026)", "Nov 2026", ["globalization"],
  ["How would a stronger dollar affect this company that sells overseas?", "Should our client worry about currency risk in an international fund?"])
t(E, ["EC:109"], "Apple moves iPhone production to India",
  "Apple said a majority of iPhones sold in the U.S. in the June 2025 quarter came from India, as it shifted production away from China to reduce tariff and concentration risk.",
  "\"Even Apple doesn't rely on one country: it moved most U.S. iPhone production to India. This business should have a second supplier too.\"",
  "Apple earnings call (May 2025)", "2025", ["globalization"],
  ["Should this business buy from overseas suppliers?", "What is the biggest risk to this business, and how would you manage it?"])
t(E, ["EC:114","EC:083"], "The Strait of Hormuz and gas prices",
  "About one-fifth of the world's oil consumption passes through the Strait of Hormuz. Supply disruptions there in 2026 pushed U.S. gasoline above $4.50 a gallon in the spring, and consumer sentiment fell to a record low in May.",
  "\"About 20% of the world's oil passes through one strait. When shipping there was disrupted this year, gas topped $4.50, which is why a flexible budget matters.\"",
  "U.S. Energy Information Administration; BLS CPI; University of Michigan (2026)", "2026", ["inflation","globalization"],
  ["Why did gas prices jump when shipping in the Middle East was disrupted?", "How could geography affect this business's supply chain?"])
t(E, ["EC:114","EC:109"], "Red Sea shipping detours",
  "After attacks on ships in the Red Sea in 2023-24, many shipping lines rerouted around Africa's Cape of Good Hope, adding about 10 days to Asia-Europe voyages and raising freight costs. In 2023, drought also forced the Panama Canal to cut daily ship crossings.",
  "\"When ships had to go around Africa, trips took about 10 days longer. For this importer, that means holding extra inventory and quoting longer lead times.\"",
  "Shipping industry reports; Panama Canal Authority", "", ["globalization"],
  ["How could geography affect this business's supply chain?"])
t(E, ["EC:112"], "Bulgaria joined the euro; ASEAN grew",
  "Bulgaria adopted the euro on Jan. 1, 2026, making it the 21st euro-area country among the EU's 27 members. Timor-Leste became ASEAN's 11th member on Oct. 26, 2025, the bloc's first expansion since 1999.",
  "\"Trade blocs keep growing: Bulgaria became the 21st country on the euro this year, which removes currency costs for businesses trading with it.\"",
  "European Central Bank (Jan. 2026); ASEAN (Oct. 2025)", "2026", ["globalization"],
  ["What happens to this business if a trade agreement changes?"])
t(E, ["EC:113","EC:007"], "Sanctions on Russia",
  "After Russia invaded Ukraine in 2022, Western governments imposed sanctions and removed several Russian banks from the SWIFT payment network. About 1,000 companies curtailed or ended operations in Russia, and McDonald's sold its 850 Russian restaurants.",
  "\"Political risk is real: companies in Russia lost entire businesses in 2022. That's why we'd keep any single-country exposure small.\"",
  "EU Council; Yale Chief Executive Leadership Institute; McDonald's (2022)", "", ["globalization"],
  ["Should our client avoid investing in politically unstable countries?", "Would you invest in a country with a command economy?"])

# ---- Business, labor and government ----
t(E, ["EC:065","EC:070"], "Small businesses by the numbers",
  "The U.S. has about 36.2 million small businesses, 99.9% of all businesses. They employ about 62.3 million people, or 45.9% of U.S. employees.",
  "\"Small businesses employ almost half of American workers, according to the SBA. Lending to this owner is how our bank grows with the local economy.\"",
  "SBA Office of Advocacy, 2025 Small Business Profile", "2025", ["entrepreneur","biz-funding"],
  ["Why should our bank make loans to small businesses?", "What role does a small business like this play in the local economy?"])
t(E, ["EC:009","EC:065"], "Record business applications",
  "Americans filed a record 5.5 million applications to start new businesses in 2023, and applications stayed far above pre-2020 levels afterward.",
  "\"A record 5.5 million Americans applied to start businesses in 2023. Free enterprise is alive, and new owners need banking, loans and advice.\"",
  "U.S. Census Bureau, Business Formation Statistics", "", ["entrepreneur"],
  ["What does the profit motive mean for our client's new business?"])
t(E, ["EC:015"], "Union membership is about 10%",
  "In 2025, 10.0% of U.S. wage and salary workers belonged to unions: 32.9% in the public sector but only 5.9% in the private sector. Local government had the highest rate, 37.8%.",
  "\"Only about 6% of private-sector workers are in unions, but where they exist, contracts lock in wages for years, which a lender can build into the forecast.\"",
  "BLS Union Members 2025 (released Feb. 18, 2026)", "2026", ["biz-risk-profit"],
  ["How would a union contract affect this company's costs and its loan?", "Should a business owner worry if employees want to unionize?"])
t(E, ["EC:015"], "The 2023 auto strike",
  "The United Auto Workers' 2023 strike against Ford, GM and Stellantis ended with contracts that raise base wages by about 25% over the life of the deals.",
  "\"After the 2023 strike, autoworkers won about 25% raises over the contract. Labor costs are a big factor in any manufacturer's loan analysis.\"",
  "UAW; company statements (2023)", "", ["biz-risk-profit"],
  ["How would a union contract affect this company's costs and its loan?"])
t(E, ["EC:008"], "CHIPS Act: government as promoter",
  "The CHIPS and Science Act of 2022 provided about $52.7 billion to expand U.S. semiconductor manufacturing, research and workforce training.",
  "\"Government isn't only a regulator: the CHIPS Act put about $52.7 billion behind U.S. chip factories. Programs like that can help businesses grow.\"",
  "U.S. Department of Commerce", "", ["biz-funding","laws-regulators"],
  ["How could a government program help this business?", "Is government regulation good or bad for banks?"])
t(E, ["EC:070"], "The Community Reinvestment Act",
  "The Community Reinvestment Act of 1977 requires federally insured banks to help meet the credit needs of the communities they serve, including low- and moderate-income neighborhoods. Regulators rate each bank's performance.",
  "\"By law, banks are expected to serve their whole community. A small-business loan program here helps the town and the bank's CRA rating.\"",
  "FDIC; OCC; Federal Reserve", "", ["laws-regulators","bank-how"],
  ["Why should a bank care about the community and not just profit?"])
t(E, ["EC:070","EC:106"], "Business Roundtable: purpose of a corporation",
  "In 2019 the Business Roundtable, a group of major company CEOs, issued a new Statement on the Purpose of a Corporation committing to customers, employees, suppliers, communities and shareholders, not shareholders alone.",
  "\"Even big-company CEOs say business serves all stakeholders, not just owners. Treating customers and the community well builds long-term profit.\"",
  "Business Roundtable (Aug. 2019)", "", ["governance","ethics"],
  ["Why should a bank care about the community and not just profit?", "Why is ethics a business issue and not just a personal one?"])
t(E, ["EC:138"], "Chime's business model",
  "Chime's 2025 IPO filing showed most of its revenue came from interchange fees, the small percentage merchants pay each time members use a Chime debit card, rather than from loan interest like a traditional bank.",
  "\"Not every bank makes money the same way: Chime earns mostly from card swipes, while a traditional bank earns the spread between loans and deposits.\"",
  "Chime Financial Form S-1 (2025)", "2025", ["fintech-ai","providers"],
  ["How does this company actually make money?", "How will our bank compete against online banks offering higher rates?"])
t(E, ["EC:138","EC:010"], "Costco's membership model",
  "Costco earned about $4.8 billion in membership fees in fiscal 2024. That steady fee income lets it keep markups on products low.",
  "\"Costco makes a large share of its profit from memberships, not markups. Recurring revenue like that makes a business steadier and easier to finance.\"",
  "Costco Wholesale 2024 Annual Report", "2024", ["biz-risk-profit"],
  ["How does this company actually make money?", "How can this business raise profit without raising prices?"])
t(E, ["EC:107"], "Banking moved to the app",
  "In ABA's October 2026 survey, 44% of bank customers named a mobile app as their top way to manage their account, more than any other method; about 10% preferred visiting a branch.",
  "\"More customers bank by app than any other way, so our plan puts the app first and turns branches into advice centers for big decisions.\"",
  "American Bankers Association / Morning Consult survey (Nov. 2026)", "Nov 2026", ["fintech-ai","providers"],
  ["How should a traditional bank adapt to customers who never visit a branch?"])
t(E, ["EC:107","EC:013"], "JPMorgan's $18 billion tech budget",
  "JPMorgan Chase said it would spend about $18 billion on technology in 2025, up $1 billion from 2024, with a focus on AI to raise productivity.",
  "\"The biggest U.S. bank spends about $18 billion a year on technology. Smaller banks can't match that, so they adapt by partnering with fintechs and focusing on service.\"",
  "JPMorgan Chase investor day (2025)", "2025", ["fintech-ai"],
  ["How should a traditional bank adapt to customers who never visit a branch?", "What should this business change first to keep up with its market?"])
t(E, ["EC:105"], "Peak 65",
  "More than 11,200 Americans a day are turning 65 from 2024 through 2027, about 4.1 million a year, the largest wave in U.S. history.",
  "\"Over 11,000 Americans turn 65 every day. That social trend makes retirement-income planning one of the fastest-growing services in finance.\"",
  "Alliance for Lifetime Income, Peak 65", "", ["retire-income"],
  ["What outside factors could hurt this business over the next few years?", "How would you scan the environment before giving this advice?"])
t(E, ["EC:003"], "Education and earnings",
  "In 2024, full-time workers with a bachelor's degree earned a median of $1,543 a week, compared with $930 for high school graduates. Their unemployment rate was 2.5% versus 4.2%.",
  "\"A bachelor's degree is worth about $600 more a week at the median, and it cuts the unemployment rate almost in half. That's human capital paying off.\"",
  "BLS, Education pays (2024 annual averages)", "2024", ["college-save"],
  ["Is college worth it for our client's child?"])

# ---- World business ----
t(E, ["EC:140"], "FCPA enforcement in 2025",
  "A February 2025 executive order paused new Foreign Corrupt Practices Act enforcement for review. On June 9, 2025, the Justice Department issued new guidelines and resumed enforcement focused on serious misconduct. The law itself did not change.",
  "\"Bribing a foreign official is still a federal crime. Enforcement was reviewed in 2025, but the FCPA itself never changed.\"",
  "U.S. Department of Justice, FCPA guidelines memo (June 9, 2025)", "2025", ["ethics","laws-regulators"],
  ["A foreign official hints that a 'fee' will speed up our license. What do you do?", "Why does bribery hurt business even if it gets deals done?"])
t(E, ["EC:140","EC:106"], "Two of the biggest bribery cases",
  "Siemens paid about $1.6 billion to U.S. and German authorities in 2008 to settle bribery charges. Goldman Sachs agreed in 2020 to pay more than $2.9 billion over bribes linked to Malaysia's 1MDB fund.",
  "\"Bribery costs far more than it wins: Goldman Sachs paid over $2.9 billion over the 1MDB bribes.\"",
  "U.S. Department of Justice; SEC (2008, 2020)", "", ["ethics"],
  ["Why does bribery hurt business even if it gets deals done?", "Why is ethics a business issue and not just a personal one?"])
t(E, ["EC:111"], "Business email compromise",
  "Business email compromise, in which criminals impersonate executives or suppliers by email to redirect payments, cost U.S. victims about $2.8 billion in 2024. Total reported internet crime losses were about $16.6 billion.",
  "\"Email scams cost U.S. businesses about $2.8 billion in 2024. Our rule: any change to payment instructions gets confirmed by phone.\"",
  "FBI Internet Crime Complaint Center, 2024 report", "2025", ["scams","occ-fraud"],
  ["How can a small business manage clients in other time zones?", "Can our advisors text clients on WhatsApp?"])
t(E, ["EC:111"], "Fines for off-channel texting",
  "Since 2021, the SEC and CFTC have fined Wall Street firms more than $2 billion combined because employees used unapproved apps like WhatsApp for business, breaking recordkeeping rules.",
  "\"Firms paid more than $2 billion in fines for business texts on WhatsApp. Clients can text us, but only through a system that keeps records.\"",
  "SEC and CFTC enforcement announcements (2021-2024)", "", ["compliance","laws-regulators"],
  ["Can our advisors text clients on WhatsApp?"])
t(E, ["EC:116"], "79% of adults worldwide have an account",
  "In 2024, 79% of adults worldwide had an account at a bank, other financial institution or mobile money provider, up from 51% in 2011. Mobile money, like Kenya's M-Pesa (launched 2007), drove much of the growth.",
  "\"Most of the world's adults now have an account, largely thanks to mobile phones. In developing countries, the bank of the future is the phone.\"",
  "World Bank Global Findex Database 2025", "2025", ["globalization","providers"],
  ["How would you adapt a banking product for a developing country?", "Should our client invest in emerging markets?"])
t(E, ["EC:141"], "REAL ID and travel checks",
  "Since May 7, 2025, U.S. domestic flyers need a REAL ID-compliant license or another accepted ID such as a passport. For international trips, the State Department's travel.state.gov lists each country's passport validity, visa and vaccination rules.",
  "\"Before any business trip, we'd check travel.state.gov for the country's passport, visa and vaccine rules, and use a REAL ID or passport for domestic flights.\"",
  "Transportation Security Administration; U.S. Department of State", "2025", ["identity"],
  ["Our client is traveling to meet a supplier overseas next month. What should they check?"])
