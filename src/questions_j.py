# Extra exam questions, part J (added Nov 2026 for the Econ Lab): brings every Economics PI to at least 3
# practice questions. Original questions; facts match the Econ Lab lessons (checked Nov 2026).
# Format: (PI, stem, [correct answer FIRST, then 3 wrong answers], explanation).
Q = []
def q(pi, stem, opts, exp): Q.append((pi, stem, opts, exp))

# ---------------- Economic foundations ----------------
q("EC:001", "A student chooses to work a Saturday shift for $120 instead of going to a concert. The concert is the student's",
  ["opportunity cost", "sunk cost", "fixed cost", "marginal revenue"],
  "Opportunity cost is the value of the next-best alternative you give up when you make a choice. By choosing to work, the student gives up the concert, so the concert is the opportunity cost. A sunk cost is money already spent that can't be recovered, and fixed costs and marginal revenue are business terms that don't describe this trade-off.")
q("EC:002", "Because a financial advisor's meeting is produced and used at the same moment, with the advisor present, services are described as",
  ["inseparable", "tangible", "durable", "standardized"],
  "Services are inseparable: they are produced and consumed at the same time, usually with the provider present, like an advisor meeting or a haircut. Services are intangible, not tangible, and they are not durable goods. They also tend to be variable rather than standardized, because quality depends on who provides them and when.")
q("EC:003", "The skills and knowledge a worker gains through education and training are called",
  ["human capital", "financial capital", "natural resources", "capital goods"],
  "Human capital is the knowledge, skill and experience that make a worker more productive, and it is built through education and training. Financial capital is money used to buy productive assets, capital goods are tools and equipment, and natural resources are part of land. Higher human capital tends to raise earnings, which is why education is treated as an investment.")
q("EC:004", "A bank's mobile app lets customers transfer money at 2 a.m. on a holiday. The app mainly creates",
  ["time utility", "form utility", "possession utility", "place utility"],
  "Time utility is value created by making a product or service available when customers want it. Being able to transfer money at 2 a.m. on a holiday is about when, not where, so it is time utility. Form utility comes from changing a product's form, possession utility from making ownership easier, and place utility from availability where the customer is.")
q("EC:004", "An auto dealer arranges a five-year loan so a buyer can drive home a new car today. The financing creates",
  ["possession utility", "form utility", "time utility", "information utility"],
  "Possession utility is value added by making it easier for a customer to own a product, most often through credit or financing. The loan lets the buyer take ownership today and pay over time. Form utility is about producing or changing the product, time utility is about when it is available, and information utility comes from providing knowledge such as labels or advice.")
q("EC:007", "In which type of economic system does the government decide what is produced, how it is produced and what prices are charged?",
  ["Command economy", "Market economy", "Traditional economy", "Mixed economy"],
  "In a command (planned) economy, the government makes the major economic decisions, including what to produce, how and at what prices. A market economy leaves these choices to buyers and sellers through supply and demand, a traditional economy relies on customs, and a mixed economy blends market decisions with some government involvement, as in the United States.")
q("EC:007", "The United States is best described as a mixed economy because",
  ["markets make most decisions, but government regulates, taxes and provides some services", "the government owns most businesses and sets most prices", "customs passed down through generations decide what is produced", "there is no government involvement in business"],
  "A mixed economy combines market decisions with government involvement. In the U.S., private buyers and sellers make most economic decisions, while government regulates industries, collects taxes, insures bank deposits through the FDIC and runs programs such as Social Security. Government ownership of most businesses describes a command economy, and customs describe a traditional one.")

# ---------------- Markets, prices and competition ----------------
q("EC:005", "When a product's price is set below the equilibrium price, the market will most likely have a",
  ["shortage", "surplus", "balanced supply", "drop in demand"],
  "At a price below equilibrium, buyers want more than sellers are willing to supply, so the quantity demanded exceeds the quantity supplied. That gap is a shortage, and it usually pushes the price up toward equilibrium. A surplus happens when the price is above equilibrium. The low price doesn't reduce demand; it raises the quantity demanded.")
q("EC:006", "A lender charges a borrower with a low credit score a higher interest rate than a borrower with an excellent score. This shows that prices",
  ["reflect risk and ration scarce credit", "are set by the government for all borrowers", "are always the same for every customer", "only cover a lender's fixed costs"],
  "Interest is the price of borrowing, and risk-based pricing uses that price to reflect the chance of default. A higher rate compensates the lender for the greater risk and rations credit toward borrowers most likely to repay. Rates are not set by the government for each borrower, they are not the same for everyone, and they cover expected losses and the cost of funds, not only fixed costs.")
q("EC:012", "A market with only a few large firms, such as airlines or wireless carriers, that closely watch and react to each other's prices is a(n)",
  ["oligopoly", "monopoly", "pure competition", "monopolistic competition"],
  "An oligopoly is a market dominated by a few large sellers whose decisions affect each other, so if one cuts prices, the others often match. A monopoly has a single seller, pure competition has many sellers of identical products, and monopolistic competition has many sellers of similar but differentiated products, like restaurants.")

# ---------------- Private enterprise, profit and risk ----------------
q("EC:009", "A homeowner can use the house as collateral for a loan because private enterprise protects",
  ["property rights", "price controls", "government ownership", "guaranteed profits"],
  "Private enterprise rests on property rights: the legal right to own, use and sell property. Because the owner legally owns the home and courts enforce that ownership, a lender can accept it as collateral and claim it if the loan isn't repaid. Price controls and government ownership are features of command systems, and private enterprise never guarantees profits.")
q("EC:009", "In a private enterprise system, the profit motive mainly encourages businesses to",
  ["take risks, innovate and serve customers efficiently", "avoid all risk", "let the government set their prices", "share profits equally with competitors"],
  "The profit motive is the chance to earn a reward for taking business risk. It pushes owners to invest, innovate, control costs and meet customer needs better than rivals. Profit comes with the possibility of loss, so businesses don't avoid all risk. Government doesn't set most prices in private enterprise, and competitors don't share profits.")
q("EC:010", "A company's sales rose 20%, but its profit fell. The most likely reason is that",
  ["its expenses grew faster than its revenue", "its revenue fell", "its profit margin rose", "its prices were too high"],
  "Profit equals revenue minus expenses. If revenue grows 20% but expenses grow even faster, for example from higher ingredient costs or new staff, profit shrinks. The facts say revenue rose, so it didn't fall. A falling profit with rising sales means the margin shrank, not rose. High prices alone wouldn't explain rising sales with falling profit.")
q("EC:065", "Which agency guarantees part of certain bank loans to small businesses, reducing the lender's risk?",
  ["Small Business Administration (SBA)", "Securities and Exchange Commission (SEC)", "Federal Deposit Insurance Corporation (FDIC)", "Internal Revenue Service (IRS)"],
  "The Small Business Administration guarantees a portion of loans such as its 7(a) loans, which go up to $5 million, so banks can lend to small businesses that might not qualify otherwise. The SEC regulates securities markets, the FDIC insures bank deposits, and the IRS collects taxes. None of those three guarantees small-business loans.")
q("EC:065", "According to the SBA, small businesses make up about what share of all U.S. businesses?",
  ["99.9%", "50%", "75%", "25%"],
  "The SBA Office of Advocacy's 2025 profile counted about 36.2 million small businesses, 99.9% of all U.S. businesses, employing about 45.9% of U.S. employees. This shows why small businesses matter so much to the economy: nearly every business is small, and together they employ almost half the private workforce.")

# ---------------- Government, taxes and labor ----------------
q("EC:008", "When the government guarantees small-business loans or funds research to help industries grow, it is acting as a",
  ["promoter of business", "regulator of business", "competitor of business", "consumer of business"],
  "Government plays several roles in business. When it guarantees loans, funds research or offers incentives, as the SBA and the CHIPS and Science Act do, it acts as a promoter that helps businesses grow. A regulator sets rules, a competitor would sell competing products, and when government buys goods and services it acts as a purchaser.")
q("EC:015", "Negotiation between a labor union and an employer over wages, benefits and working conditions is called",
  ["collective bargaining", "arbitration", "a lockout", "mediation"],
  "Collective bargaining is the process in which a union negotiates with an employer on behalf of all its members, producing a labor contract. Arbitration is when a neutral third party makes a binding decision, mediation is when a neutral party helps both sides reach their own agreement, and a lockout is an employer keeping workers out during a dispute.")
q("EC:015", "A state law that bans contracts requiring workers to pay union fees as a condition of employment is a",
  ["right-to-work law", "minimum wage law", "closed shop law", "collective bargaining law"],
  "Right-to-work laws prohibit agreements that make paying union dues or fees a condition of keeping a job. The Taft-Hartley Act of 1947 allowed states to pass them, and 26 states had them after Michigan's repeal took effect in 2024. A closed shop, which required union membership before hiring, was banned by Taft-Hartley. Minimum wage laws set a pay floor and have nothing to do with union fees.")
q("EC:015", "Compared with the private sector, the union membership rate among U.S. public-sector workers is",
  ["much higher", "much lower", "about the same", "zero, because public workers can't join unions"],
  "In 2025, 32.9% of public-sector workers belonged to unions, compared with 5.9% of private-sector workers, according to the BLS (released February 2026). The overall rate was 10.0%. Public employees such as teachers, police and firefighters can join unions, and local government has the highest rate of all, 37.8%.")

# ---------------- Productivity ----------------
q("EC:013", "Labor productivity is measured as",
  ["output per hour worked", "total hours worked", "total wages paid", "number of employees"],
  "Labor productivity is output divided by labor input, usually output per hour worked. Total hours, total wages and number of employees measure inputs or costs, not efficiency. A business raises productivity when it produces more with the same hours, often through better technology, training or processes. The BLS reported U.S. nonfarm productivity rose at a 3.6% annual rate in Q3 2026.")
q("EC:023", "A bakery with one oven hires a fourth worker, who adds only 20 loaves a day while the second worker added 80. This illustrates",
  ["the law of diminishing returns", "economies of scale", "the law of demand", "specialization increasing without limit"],
  "The law of diminishing returns says that adding more of one input, workers, to a fixed input, one oven, eventually adds less output per unit. The fourth worker adds far less than the second because workers are waiting for the oven. Economies of scale involve growing all inputs together over the long run, and the law of demand concerns prices and quantity demanded.")

# ---------------- Indicators and the business cycle ----------------
q("EC:017", "Real GDP differs from nominal GDP because real GDP",
  ["is adjusted for inflation", "includes only goods, not services", "counts intermediate goods", "is measured in a foreign currency"],
  "Real GDP removes the effect of rising prices, so it shows whether the economy actually produced more. Nominal GDP uses current prices, so it can rise just because of inflation. Both measures include goods and services and count only final goods, to avoid double counting. U.S. GDP is measured in dollars.")
q("EC:018", "During which phase of the business cycle do GDP and employment usually fall?",
  ["Contraction", "Expansion", "Peak", "Recovery"],
  "In a contraction, economic activity declines: GDP falls, unemployment rises and spending slows; a significant, lasting contraction is a recession. In an expansion, GDP and jobs grow. The peak is the high point before a downturn, and recovery is the rebound after the trough.")
q("EC:018", "Which industry is most likely to be hurt in a recession because its sales swing strongly with the business cycle?",
  ["New car sales", "Groceries", "Electric utilities", "Prescription drugs"],
  "Cyclical industries, such as new cars, travel and home building, sell products people can delay, so their sales fall sharply in recessions. Defensive industries like groceries, utilities and prescription drugs sell necessities that people keep buying in any economy, so their sales stay steadier.")
q("EC:081", "Which monthly government report measures total household spending on goods and services?",
  ["Personal consumption expenditures (PCE) from the BEA", "The unemployment rate from the BLS", "The producer price index", "The federal budget"],
  "Personal consumption expenditures, published monthly by the Bureau of Economic Analysis, measure total household spending. Consumer spending makes up about 68% of U.S. GDP, which is why economists watch it closely. The unemployment rate measures joblessness, the producer price index measures wholesale prices, and the federal budget shows government spending.")
q("EC:081", "If consumer spending rises 0.5% in a month but prices rise about the same amount, real consumer spending",
  ["was nearly unchanged", "rose 1%", "fell 0.5%", "rose 0.5%"],
  "Real spending adjusts for inflation. If households spent 0.5% more in dollars but prices also rose about 0.5%, they bought about the same amount of goods and services. That's what happened in September 2026: spending rose 0.5%, but real spending grew less than 0.1% (BEA). This is why economists focus on real, not nominal, spending.")
q("EC:082", "A worker who quit one job and is looking for a better one is part of which type of unemployment?",
  ["Frictional", "Structural", "Cyclical", "Seasonal"],
  "Frictional unemployment is the short-term unemployment of people between jobs or entering the workforce, and it exists even in a healthy economy. Structural unemployment comes from a mismatch between workers' skills and available jobs, cyclical unemployment is caused by recessions, and seasonal unemployment comes from jobs that end at certain times of year.")
q("EC:082", "A retiree who isn't looking for work is counted in the unemployment rate as",
  ["not in the labor force", "unemployed", "employed part time", "structurally unemployed"],
  "The unemployment rate counts only people who are jobless and actively looking for work. Retirees, full-time students and others who aren't looking are outside the labor force, so they aren't counted as unemployed. That's why the unemployment rate (4.1% in October 2026, BLS) doesn't include everyone without a job.")
q("EC:083", "Inflation caused by rising energy and raw material costs that push up businesses' prices is called",
  ["cost-push inflation", "demand-pull inflation", "deflation", "disinflation"],
  "Cost-push inflation happens when production costs, such as energy, materials or wages, rise and businesses pass them on as higher prices. Gasoline topping $4.50 in spring 2026 is an example. Demand-pull inflation comes from spending growing faster than output, deflation is falling prices, and disinflation is prices rising more slowly.")
q("EC:083", "Which borrower is usually helped by unexpected inflation?",
  ["A homeowner with a fixed-rate mortgage", "A saver with cash in a checking account", "A retiree living on a fixed pension", "A lender receiving fixed payments"],
  "With a fixed-rate mortgage, the payment stays the same while inflation raises prices and usually wages, so the borrower repays with dollars that are worth less. Savers holding cash, retirees on fixed incomes and lenders receiving fixed payments are hurt, because inflation reduces the buying power of the money they hold or receive.")
q("EC:084", "When interest rates rise, the prices of existing bonds usually",
  ["fall", "rise", "stay exactly the same", "become guaranteed"],
  "Bond prices move opposite to interest rates. When new bonds pay higher rates, older bonds with lower fixed payments are worth less, so their prices fall, and long-term bonds fall the most. This interest-rate risk contributed to Silicon Valley Bank's failure in 2023. Bond prices are never guaranteed before maturity.")

# ---------------- Business in society ----------------
q("EC:070", "The Community Reinvestment Act (1977) requires federally insured banks to",
  ["help meet the credit needs of their whole community, including low- and moderate-income areas", "pay higher taxes than other businesses", "offer free checking accounts to everyone", "lend only to large corporations"],
  "The Community Reinvestment Act encourages and requires federally insured banks to serve the credit needs of all the communities where they take deposits, including low- and moderate-income neighborhoods, and regulators rate their performance. It doesn't set special taxes, require free checking or limit lending to large corporations.")
q("EC:070", "Customers, employees, suppliers, the community and shareholders who are affected by a company's decisions are its",
  ["stakeholders", "competitors", "regulators", "creditors only"],
  "Stakeholders are everyone affected by a business's actions. In 2019 the Business Roundtable, a group of major company CEOs, committed to serving all stakeholders rather than shareholders alone. Competitors are rivals, regulators are government agencies, and creditors are only one type of stakeholder.")
q("EC:071", "Hiring, organizing work and controlling results so that the other activities of a business run well is the business activity of",
  ["management", "production", "marketing", "finance"],
  "Management plans, organizes, staffs, leads and controls a business so production, marketing and finance work together. Production creates the goods or services, marketing identifies customer wants and gets products to them, and finance obtains and manages the money the business needs.")
q("EC:138", "A business that charges customers a recurring monthly fee for ongoing access to a service is using a",
  ["subscription model", "freemium model", "franchise model", "razor-and-blade model"],
  "In a subscription model, customers pay a recurring fee, monthly or yearly, for continued access, as with streaming services or software. A freemium model gives basic features free and charges for upgrades, a franchise model sells the right to use a brand and system, and a razor-and-blade model sells a cheap base product and profits from refills.")
q("EC:138", "A traditional bank earns most of its profit from",
  ["the spread between interest earned on loans and interest paid on deposits", "selling advertising", "membership fees", "franchise royalties"],
  "A traditional bank's main business model is net interest income: it pays depositors one rate and lends money out at a higher rate, keeping the difference, plus fees. Advertising, membership fees and franchise royalties are other business models. Many fintechs, by contrast, earn mostly interchange fees from debit card use.")
q("EC:138", "Fintech apps that earn most of their revenue from the small fee merchants pay each time a customer uses a debit card are relying on",
  ["interchange fees", "interest on loans", "overdraft fees", "membership dues"],
  "Interchange fees are small percentages of each card purchase that merchants pay, part of which goes to the card issuer. Chime's 2025 IPO filing showed most of its revenue came from interchange fees, a different model from a traditional bank's reliance on loan interest. Overdraft fees and membership dues are other possible revenue sources, but they weren't the main model.")
q("EC:103", "The number of employees a manager directly supervises is called the manager's",
  ["span of control", "chain of command", "line authority", "organizational chart"],
  "Span of control is the number of people who report directly to a manager. A wide span means a flatter organization with fewer layers; a narrow span means a taller one. The chain of command is the line of authority from top to bottom, line authority is the right to direct others, and an organizational chart is the diagram showing the structure.")
q("EC:105", "Which tool scans a business's external environment by looking at political, economic, social, technological, legal and environmental factors?",
  ["PESTLE analysis", "Break-even analysis", "Ratio analysis", "Payback period"],
  "PESTLE analysis examines political, economic, social, technological, legal and environmental forces outside a business that it can't control but must respond to. Break-even analysis finds the sales needed to cover costs, ratio analysis evaluates financial statements, and the payback period measures how long an investment takes to repay its cost.")
q("EC:105", "An aging population that increases demand for retirement planning is an example of which type of factor in the business environment?",
  ["Social", "Technological", "Legal", "Political"],
  "Population traits such as age, family structure and lifestyles are social factors. With more than 11,200 Americans a day turning 65 from 2024 through 2027, demand for retirement-income services is rising. Technological factors involve new tools, legal factors involve laws and regulations, and political factors involve government stability and policy.")
q("EC:106", "An action that is legal but misleads customers in order to boost sales is best described as",
  ["unethical, because ethics go beyond what the law requires", "ethical, because it is legal", "required by the law", "a smart competitive strategy with no downside"],
  "Business ethics are moral principles such as honesty and fairness, and they set a higher bar than the law. A misleading tactic can be legal and still unethical. It also carries real business risk: Wells Fargo agreed to pay $3 billion in 2020 after sales pressure led employees to open accounts customers hadn't authorized.")
q("EC:107", "A company that changes its main product or business model in response to a shifting market, like Netflix moving from DVDs to streaming, is making a",
  ["pivot", "merger", "recall", "liquidation"],
  "A pivot is a major change in a company's business model or main product to adapt to the market. Netflix pivoted from mailing DVDs to streaming and shipped its final DVD in 2023. A merger combines two companies, a recall pulls a defective product, and liquidation means selling off assets to close a business.")
q("EC:107", "A bank sees that most customers now manage their accounts by app. The best way to adapt is to",
  ["improve its mobile app and turn low-traffic branches into advice centers", "open more branches", "ignore the trend, since branches have always worked", "raise fees on mobile users"],
  "Organizations adapt by responding to how customers now behave. In ABA's October 2026 survey, more customers named a mobile app as their top way to bank than any other method, and only about 10% preferred a branch. Improving the app meets that need, while converting quiet branches into advice centers keeps in-person help for big decisions and cuts costs.")

# ---------------- Global trade ----------------
q("EC:016", "A country should specialize in producing goods for which it has the lowest opportunity cost. This is the principle of",
  ["comparative advantage", "absolute advantage", "protectionism", "a trade deficit"],
  "Comparative advantage means producing a good at a lower opportunity cost than another country. Even if one country is better at producing everything (absolute advantage), both countries gain by specializing in what they give up least to produce and then trading. Protectionism uses trade barriers, and a trade deficit is when imports exceed exports.")
q("EC:016", "In September 2026 the U.S. imported more goods and services than it exported. This means the U.S. had a",
  ["trade deficit", "trade surplus", "budget surplus", "balanced trade account"],
  "The balance of trade equals exports minus imports. When imports exceed exports, a country has a trade deficit; in September 2026 the U.S. goods and services deficit was $105.0 billion (Census Bureau and BEA). A trade surplus is the opposite, and a budget surplus refers to government revenue exceeding spending, not trade.")
q("EC:109", "A U.S. company moves production from China to Mexico to be closer to its customers and reduce shipping risk. This is called",
  ["nearshoring", "offshoring", "outsourcing to the government", "dumping"],
  "Nearshoring means moving production to a nearby country, often to shorten supply chains and reduce risk. Offshoring means moving work to any foreign country, often far away for lower costs. Dumping is selling exports below their fair price, and moving production to Mexico has nothing to do with outsourcing to the government.")
q("EC:109", "Which is a risk that globalization creates for businesses?",
  ["Long global supply chains can be disrupted by events far away", "Customers have fewer product choices", "Businesses can sell only in their home country", "Competition from foreign firms disappears"],
  "Globalization connects businesses to suppliers and customers worldwide, which lowers costs and widens markets but also exposes them to disruptions anywhere along the chain, like chip shortages in 2021-22 or shipping detours around the Red Sea in 2023-24. Globalization gives customers more choices, opens foreign markets and increases foreign competition.")
q("EC:109", "To reduce dependence on one country, Apple said a majority of iPhones sold in the U.S. in the June 2025 quarter came from India. This shows a company",
  ["diversifying its global supply chain", "ending globalization", "becoming a command economy", "eliminating all imports"],
  "By shifting production for the U.S. market from China to India, Apple spread its supply chain across countries to reduce tariff and concentration risk. It's still a global company importing from abroad, so it hasn't ended globalization or eliminated imports, and a company's sourcing decision has nothing to do with a country's economic system.")
q("EC:100", "Which change would most likely strengthen the U.S. dollar against other currencies?",
  ["U.S. interest rates rising relative to other countries' rates", "Higher inflation in the U.S.", "Political instability in the U.S.", "U.S. interest rates falling sharply"],
  "Higher interest rates attract foreign investors seeking better returns, which raises demand for dollars and strengthens the currency; in late 2026 expectations of higher U.S. rates helped push the dollar up. Higher inflation, political instability and falling rates tend to weaken a currency because they make holding it less attractive.")
q("EC:100", "A strong U.S. dollar is generally good news for",
  ["Americans traveling abroad and businesses that import goods", "U.S. companies that export products", "foreign tourists visiting the U.S.", "U.S. companies' profits earned in euros"],
  "A strong dollar buys more foreign currency, so Americans traveling abroad and U.S. importers pay less for foreign goods and services. The same strength makes U.S. exports more expensive for foreign buyers, makes trips to the U.S. pricier for foreign tourists and shrinks the dollar value of profits earned in other currencies.")
q("EC:112", "USMCA, the trade agreement among the United States, Mexico and Canada, replaced which agreement in 2020?",
  ["NAFTA", "The European Union", "ASEAN", "The World Trade Organization"],
  "The United States-Mexico-Canada Agreement took effect in 2020, replacing the North American Free Trade Agreement, which began in 1994. At its first joint review on July 1, 2026, the U.S. declined to renew it, triggering annual reviews, but the agreement remains in force. The EU, ASEAN and WTO are separate organizations.")
q("EC:112", "An economic union of 27 countries with a single market, 21 of which share a common currency, is the",
  ["European Union", "ASEAN", "Mercosur", "USMCA"],
  "The European Union has 27 member countries and a single market for goods, services, people and money. Since Bulgaria adopted the euro on January 1, 2026, 21 EU members use the euro. ASEAN is a Southeast Asian bloc of 11 countries, Mercosur is a South American trade bloc, and USMCA covers the U.S., Mexico and Canada, none of which share a currency.")
q("EC:112", "Which international organization sets global trade rules and settles trade disputes among its 166 members?",
  ["World Trade Organization", "International Monetary Fund", "World Bank", "OPEC"],
  "The World Trade Organization sets the rules of international trade and provides a system for settling disputes among member countries. The International Monetary Fund promotes financial stability and lends to countries in crisis, the World Bank finances development projects, and OPEC is a group of oil-exporting countries.")
q("EC:113", "When a government takes over privately owned foreign businesses in its country, it is called",
  ["expropriation (nationalization)", "privatization", "a trade alliance", "deregulation"],
  "Expropriation, or nationalization, is a government seizing ownership of private property or businesses, a major political risk for foreign investors. Privatization is the opposite, selling government-owned businesses to private owners. A trade alliance reduces barriers among countries, and deregulation removes rules.")
q("EC:113", "After Russia invaded Ukraine in 2022, Western governments removed several Russian banks from the SWIFT payment network. This is an example of",
  ["sanctions, a political factor affecting trade", "a free-trade agreement", "comparative advantage", "a natural risk"],
  "Sanctions are penalties governments impose on another country, such as asset freezes, trade bans or cutting banks off from international payment systems like SWIFT. They are a political factor that can shut down trade and investment almost overnight. A free-trade agreement reduces barriers, comparative advantage explains why trade happens, and natural risks come from nature.")
q("EC:113", "A business can transfer some of the risk of losing its foreign investment to war or government seizure by buying",
  ["political risk insurance", "business interruption insurance from its local agent only", "term life insurance", "a certificate of deposit"],
  "Political risk insurance, offered by agencies such as the U.S. International Development Finance Corporation and the World Bank's MIGA, protects businesses against losses from expropriation, political violence and currency restrictions. Term life insurance covers a person's death, and a CD is a savings product. Ordinary business interruption policies generally don't cover political events.")
q("EC:104", "Letting a foreign company use your brand name or technology in exchange for a fee is the market-entry method called",
  ["licensing", "foreign direct investment", "a joint venture", "exporting"],
  "Licensing grants a foreign company the right to use a brand, patent or technology for a fee or royalty, which lets a firm enter a market with little investment. Foreign direct investment means owning facilities abroad, a joint venture shares ownership with a local partner, and exporting sells products made at home to foreign buyers.")
q("EC:104", "For a small business with little money to invest, the lowest-risk way to begin selling in foreign markets is usually",
  ["exporting", "building a factory abroad", "buying a foreign competitor", "forming a joint venture"],
  "Exporting, selling products made at home to foreign buyers, requires the least investment and commitment, so it lets a small business test demand with limited risk. Building a factory abroad or buying a foreign company is foreign direct investment, the highest commitment, and a joint venture requires sharing ownership and investment with a partner.")

# ---------------- Doing business around the world ----------------
q("EC:110", "In a high-context culture, business communication relies mostly on",
  ["relationships, tone and unspoken cues", "detailed written contracts only", "direct, blunt statements", "speed over relationship building"],
  "In high-context cultures such as Japan and China, much of the meaning comes from relationships, tone, status and what isn't said, so trust is built before business. Low-context cultures like the U.S. and Germany rely more on direct, explicit statements and detailed written agreements, and tend to move faster.")
q("EC:110", "In Japan, the respectful way to receive a business card is to",
  ["take it with both hands and read it before putting it away", "put it in your back pocket right away", "write notes on it during the meeting", "slide it across the table without looking"],
  "Business cards (meishi) are treated as an extension of the person in Japan, so they are offered and received with both hands and read carefully before being put away. Stuffing a card in a pocket, writing on it or ignoring it is seen as disrespectful. Small gestures like this help build the trust that business relationships depend on.")
q("EC:111", "Criminals who send emails pretending to be a company's supplier and asking it to wire payments to a new account are committing",
  ["business email compromise", "insider trading", "identity verification", "a webinar"],
  "Business email compromise (BEC) is fraud in which criminals impersonate executives, vendors or partners by email to redirect payments. It cost U.S. victims about $2.8 billion in 2024, according to the FBI. The best defense is confirming any payment change by calling a known phone number. Insider trading is a securities crime, and the other choices aren't fraud.")
q("EC:111", "Financial firms must use approved, archived communication channels with clients mainly because",
  ["securities rules require firms to keep records of business communications", "texting clients is always illegal", "email is too slow for business", "clients can't use phones"],
  "Recordkeeping rules require financial firms to preserve business communications. Since 2021, the SEC and CFTC have fined firms more than $2 billion combined for employees using unapproved apps such as WhatsApp. Texting clients is allowed through compliant systems that save the messages, so the issue is recordkeeping, not texting itself.")
q("EC:111", "Which is a major benefit of video conferencing for global business?",
  ["It cuts travel costs and lets teams in different countries meet quickly", "It eliminates all time-zone differences", "It removes every cybersecurity risk", "It guarantees no misunderstandings"],
  "Video conferencing lets people in different countries meet face to face without travel, saving money and speeding decisions. It doesn't remove time-zone differences, can introduce cybersecurity risks and can still lead to misunderstandings when tone or cultural cues are missed, so businesses still need clear communication practices.")
q("EC:114", "A narrow waterway that carries a large share of world trade, such as the Strait of Hormuz, is called a",
  ["chokepoint", "free-trade zone", "landlocked route", "trade alliance"],
  "A chokepoint is a narrow route that a large share of shipping must pass through. About one-fifth of the world's oil consumption flows through the Strait of Hormuz (EIA), so disruptions there raise oil and gasoline prices worldwide, as in 2026. A free-trade zone is an area with reduced customs rules, and a trade alliance is an agreement among countries.")
q("EC:114", "Compared with coastal countries, landlocked countries usually face",
  ["higher transportation costs for trade", "lower shipping costs", "no need for trade", "guaranteed trade surpluses"],
  "Countries without a coastline must ship goods over land or through neighbors' ports, which adds cost, time and dependence on other countries. That's why ports and navigable rivers are major geographic advantages in trade. Being landlocked doesn't eliminate the need to trade or guarantee a surplus.")
q("EC:115", "Many former British colonies use English in business and a common-law legal system. This shows how a country's",
  ["history affects its trade relationships", "geography sets its climate", "economic system is chosen each year", "currency is always pegged to the pound"],
  "A country's history shapes trade today. Colonial ties often leave a shared language, legal traditions and business networks, which make contracts and trade easier between those countries. Hong Kong, for example, still uses common law. This is about history, not climate, and former colonies don't have to peg their currencies to the British pound.")
q("EC:115", "China's market reforms that began in 1978 and its entry into the World Trade Organization in 2001 led to",
  ["China becoming the world's largest exporter of goods", "China leaving world trade", "the end of the WTO", "China adopting the euro"],
  "China's economic history shows how policy changes reshape trade. After reforms opened its economy starting in 1978 and WTO membership in 2001 lowered barriers with other members, China became the world's largest goods exporter. It didn't leave world trade, the WTO still operates, and China uses its own currency, the yuan (renminbi).")
q("EC:115", "People in a country that once suffered hyperinflation may prefer to save in foreign currency or gold because",
  ["past experiences shape long-lasting attitudes toward money", "hyperinflation is required by law", "banks in every country are unsafe", "gold always earns interest"],
  "Economic history leaves lasting memories. Families who saw savings wiped out by hyperinflation or currency collapse often distrust their local currency and banks for generations. Germany's 1923 hyperinflation, for instance, shaped a lasting national focus on price stability. Gold doesn't pay interest, and not all banks are unsafe; in the U.S., FDIC insurance protects deposits.")
q("EC:116", "Fast-growing economies such as India, Brazil and Mexico that are becoming more industrialized are often called",
  ["emerging markets", "command economies", "traditional economies", "developed economies"],
  "Emerging markets are economies moving from developing toward developed status, with rapid growth and industrialization. They often offer higher growth but more risk for investors. Command and traditional describe how an economy makes decisions, not its development level, and developed economies like the U.S., Japan and Germany already have high incomes.")
q("EC:116", "The World Bank classifies countries' economic development mainly by",
  ["income per person (GNI per capita)", "population size", "land area", "number of trade agreements"],
  "The World Bank sorts countries into low, lower-middle, upper-middle and high income groups based on gross national income per person. Population and land area don't show how wealthy people are, and the number of trade agreements isn't a development measure. Income per person is a common way to compare living standards across countries.")
q("EC:116", "Mobile money services like Kenya's M-Pesa matter for developing economies mainly because they",
  ["give people without bank branches nearby a way to save and send money", "replace the need for any currency", "are only used by large corporations", "prevent all fraud"],
  "In many developing countries, mobile phones reach far more people than bank branches. Mobile money lets people store, send and receive money by phone, which expanded financial inclusion: 79% of adults worldwide had an account in 2024, up from 51% in 2011 (World Bank Global Findex 2025). It still uses currency, serves individuals and doesn't eliminate fraud.")
q("EC:140", "The U.S. law that bans U.S. companies from bribing foreign government officials to win or keep business is the",
  ["Foreign Corrupt Practices Act", "Sarbanes-Oxley Act", "Dodd-Frank Act", "Fair Credit Reporting Act"],
  "The Foreign Corrupt Practices Act of 1977 prohibits bribing foreign officials and requires public companies to keep accurate books and internal controls. Sarbanes-Oxley focuses on corporate financial reporting, Dodd-Frank reformed financial regulation after 2008, and the Fair Credit Reporting Act governs consumer credit reports.")
q("EC:140", "Compared with the FCPA, the U.K. Bribery Act of 2010 is stricter because it",
  ["bans facilitating payments and covers private-sector bribery", "allows bribes under $1,000", "applies only to government employees", "has no penalties"],
  "The U.K. Bribery Act covers bribes to private businesses as well as public officials and does not allow facilitating payments, the small payments for routine government actions that the FCPA narrowly permits. It doesn't allow small bribes, it isn't limited to government employees, and it carries serious penalties including prison.")
q("EC:140", "A company caught bribing foreign officials is most likely to face",
  ["large fines, criminal charges and damage to its reputation", "a tax refund", "guaranteed new contracts", "no consequences if the bribe was common locally"],
  "Bribery carries heavy legal and business costs. Siemens paid about $1.6 billion in 2008, and Goldman Sachs agreed to pay more than $2.9 billion in 2020 over the 1MDB bribes. Penalties can include prison for individuals, loss of contracts and lasting reputational harm. U.S. law applies even when bribery is common in the other country.")
q("EC:141", "Official permission from a country to enter for a specific purpose, such as business, is a",
  ["visa", "passport", "boarding pass", "REAL ID"],
  "A visa is permission granted by the country you are visiting to enter for a purpose and length of stay. A passport, issued by your own country, proves identity and citizenship. A boarding pass lets you board a flight, and a REAL ID is a U.S. identification standard for domestic flights, not permission to enter another country.")
q("EC:141", "Many countries require a traveler's passport to be valid for at least how long beyond the trip?",
  ["Six months", "One week", "One day", "Five years"],
  "Many countries require that a visitor's passport remain valid at least six months beyond the planned departure date, and some require blank pages too. Travelers who don't meet the rule can be refused boarding or entry. The State Department's travel.state.gov lists each country's exact requirements.")
q("EC:141", "A business traveler going to a country that requires proof of yellow fever vaccination should check requirements with the",
  ["CDC Travelers' Health and the State Department", "IRS", "FDIC", "SEC"],
  "The Centers for Disease Control and Prevention's Travelers' Health pages list vaccines required or recommended for each country, including yellow fever certificates, and the State Department's travel.state.gov lists entry requirements. The IRS handles taxes, the FDIC insures bank deposits and the SEC regulates securities, so none of them sets travel health rules.")
