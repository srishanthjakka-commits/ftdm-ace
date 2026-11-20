# (pi, question, [correct, wrong, wrong, wrong], explanation) -- correct answer first; the app shuffles.
Q = []
def q(pi, stem, opts, exp): Q.append((pi, stem, opts, exp))

# --- careers, networking, client service, CRM ---
q("PD:152","Which finance professional develops investment strategies and oversees portfolios for clients?",
 ["Fund manager","Claims adjuster","Payroll clerk","Bank teller"],
 "Fund (portfolio) managers make investment decisions and monitor client portfolios.")
q("PD:152","A drawback often associated with careers in securities and investments is that",
 ["the work can be very stressful with long hours.","pay is always low.","no license is ever needed.","jobs involve no contact with clients."],
 "Investment careers can pay well but bring pressure, market swings and long hours.")
q("PD:152","Which finance career area focuses on helping individuals manage money, save and invest to meet personal goals?",
 ["Personal financial planning","Corporate treasury","Insurance underwriting","Auditing"],
 "Financial planners and advisors work with individuals on budgeting, saving, investing and retirement.")
q("PD:153","A financial planner holds free money-management workshops for local small business owners. The main networking benefit is",
 ["meeting potential new clients and contacts.","avoiding paperwork.","lowering taxes.","replacing professional licenses."],
 "Seminars position the planner as an expert and create new business relationships.")
q("PD:153","Which is the best way for a new accountant to build professional relationships in finance?",
 ["Joining and actively participating in a professional association","Avoiding industry events","Only communicating by email","Declining all lunch invitations"],
 "Associations offer committees, offices, seminars and conferences where relationships grow.")
q("PD:153","A wealth advisor asks satisfied clients to recommend her to friends and offers them a thank-you gift. She is",
 ["implementing a referral system.","front-running.","practicing insider trading.","benchmarking."],
 "A referral system turns happy clients into a steady source of new business.")
q("CR:012","A financial planner's main responsibility to clients is to",
 ["provide appropriate guidance that helps them reach their financial goals.","sell the products with the highest commissions.","keep their goals secret from them.","guarantee investment returns."],
 "Planners must give suitable advice and products that fit each client's goals and risk tolerance.")
q("CR:012","Noah, a tax preparer, is asked by a friend at a party how much a mutual client earns. Noah should",
 ["keep the client's information confidential.","share it because they're friends.","post it online.","estimate the number."],
 "Finance professionals have an ethical and legal duty to protect client confidentiality.")
q("CR:012","Before designing a service plan, what should a finance professional find out first?",
 ["What level of service and communication the client expects","The client's favorite sports team","What competitors charge for unrelated products","The client's neighbors' incomes"],
 "Understanding client expectations is the basis for long-term, satisfying relationships.")
q("CR:012","An advisor recommends a fund managed by her own firm without telling the client she earns a bonus for it. This is a",
 ["conflict of interest.","diversification strategy.","capital gain.","risk transfer."],
 "Undisclosed personal benefit creates a conflict of interest. Advisors must disclose it or avoid it.")
q("CR:024","What is the primary benefit of CRM technology?",
 ["It consolidates customer data and interactions in a single hub.","It eliminates the need for salespeople.","It sets the company's stock price.","It replaces accounting software."],
 "CRM software centralizes customer information so every employee can serve customers consistently.")
q("CR:024","A CRM system collects thousands of data points per customer. Why is human judgment still needed?",
 ["To tell useful information apart from unnecessary information","Because computers can't store data","To delete all customer records","To avoid analyzing results"],
 "Managers must decide which data actually matters for decisions.")
q("CR:024","A bank analyzes its CRM data to predict how much each customer will deposit next year. This prediction technique is",
 ["regression.","classification.","normalization.","filtering."],
 "Regression predicts a number (a deposit amount). Classification predicts a category, like 'likely to leave.'")
q("CR:024","CRM software shows that a client who just bought a home has no homeowners insurance with the firm. This information most directly reveals a",
 ["sales opportunity.","compliance violation.","sunk cost.","market contraction."],
 "CRM data helps firms spot customer needs and cross-sell relevant products.")

# --- data & databases ---
q("NF:124","Reorganizing a database to reduce duplicate data and improve data integrity is called",
 ["normalization.","filtering.","front-running.","data mining."],
 "Normalization splits data into related tables so each fact is stored once.")
q("NF:124","An analyst wants only the companies in the technology industry from a list of 5,000 stocks. She should use",
 ["data filtering.","Benford's Law.","normalization.","a pivot to the primary market."],
 "Filtering selects a subset of records that meet specific criteria.")
q("NF:124","To find customers who live in Springdale AND spent over $100,000, a database user must",
 ["set query criteria on both the city and purchase-amount fields.","sort the whole database alphabetically.","delete all other records.","create a new table by hand."],
 "Queries retrieve records that meet the criteria you specify, here on two fields at once.")
q("NF:124","What is the first step in creating a successful multi-table database query?",
 ["Pinpoint exactly what you want to know","Delete duplicate tables","Print every record","Choose a font"],
 "You must define the question before choosing the tables, fields and criteria.")
q("NF:124","An auditor applies Benford's Law to a company's expense data. If the data were fabricated, what pattern would she most likely see?",
 ["The digits 1 through 9 appearing as the first digit about equally often","The digit 1 leading about 30% of the time","Only even numbers","Every number ending in zero"],
 "Real measured data follows Benford's Law (small leading digits are common). Made-up data often shows leading digits spread evenly.")
q("NF:124","Benford's Law works best on data that is",
 ["measured, such as invoice amounts.","assigned, such as phone numbers.","limited to one digit.","made up of ZIP codes."],
 "Assigned numbers like IDs and phone numbers don't follow Benford's pattern. Naturally measured amounts do.")
q("NF:015","An insurance company's environmental scan notes that new state laws will change how policies must be written. This is a",
 ["political factor.","economic factor.","social factor.","technological factor."],
 "Laws and regulations are political (legal) factors in a PEST analysis.")
q("NF:149","A data mining technique that finds if-then relationships, such as 'if a customer opens a checking account, then they often open a savings account,' is",
 ["rule induction.","normalization.","benchmarking.","vertical analysis."],
 "Rule induction discovers if-then rules among data.")
q("NF:150","Which use of customer data is most likely to raise ethical concerns?",
 ["Analyzing customers' search history to target ads without their knowledge","Sending a receipt by email","Recording a purchase for warranty purposes","Asking customers for feedback"],
 "Many consumers see covert use of their personal browsing data as an invasion of privacy.")
q("NF:014","A CRM system can help a company predict a customer's product preferences by tracking the customer's",
 ["prior purchases.","credit card number.","social security number.","shoe size only."],
 "Purchase history in internal records is a strong guide to future preferences.")

# --- EI ---
q("EI:008","A coworker interrupts others and ignores their rights to get his way. His behavior is",
 ["aggressive.","assertive.","passive.","empathetic."],
 "Aggressive behavior disregards others' rights. Assertive behavior states your needs while respecting others.")
q("EI:008","Which is an example of practicing verbal assertiveness?",
 ["Starting conversations and stating your opinion respectfully","Staying silent in every meeting","Yelling to win arguments","Agreeing with everything to avoid conflict"],
 "Assertiveness means expressing yourself honestly and respectfully.")
q("EI:019","Priya is assigned a project she has never done before. Instead of worrying, she tells herself it's a chance to learn. She is",
 ["thinking positively.","using humor.","looking good.","avoiding the task."],
 "Reframing a challenge as an opportunity is the 'think positively' step of maintaining a positive attitude.")
q("EI:023","Which belief best supports self-confidence?",
 ["Mistakes are a normal part of growth.","I should never try anything new.","Others are always more capable.","Feedback means I failed."],
 "Confident people accept mistakes as learning opportunities.")
q("EI:092","Being comfortable not knowing an answer right away, without immediately looking it up, shows",
 ["tolerance for ambiguity.","herd mentality.","aggressiveness.","procrastination."],
 "Tolerance for ambiguity is comfort with uncertainty.")
q("EI:124","A loan officer must decide whether to approve a friend's loan application that doesn't quite meet bank standards. She faces a(n)",
 ["ethical dilemma.","capital gain.","market contraction.","variance."],
 "An ethical dilemma involves competing values, here friendship versus duty to the employer.")
q("EI:128","What is the most important thing a person can do to build trust?",
 ["Keep promises","Talk often","Agree with everyone","Avoid giving opinions"],
 "Consistently doing what you say you'll do is the foundation of trust.")
q("EI:134","Investors who buy a stock only because everyone else is buying it are showing",
 ["herd mentality.","home bias.","tolerance for ambiguity.","due diligence."],
 "Herd mentality means following the crowd without independent thinking.")
q("EI:012","Before asking his manager to approve new budgeting software, Tyrell gathers cost data and examples of time savings. He is",
 ["doing his homework to persuade effectively.","being aggressive.","avoiding the issue.","practicing herd mentality."],
 "Effective persuasion is backed by facts and benefits relevant to the audience.")
q("EI:004","Which is an example of an unethical work habit?",
 ["Calling in sick to go to a concert","Taking a scheduled vacation day","Working through lunch to meet a deadline","Clocking out on time"],
 "Misusing sick leave is dishonest. The others are legitimate.")
q("EI:091","A decision maker may accept the risks of a decision because",
 ["the benefits of reaching an important goal outweigh the risks.","risks never matter.","they have no information.","someone else will be blamed."],
 "Good decision makers weigh risk against reward and accept reasonable risk for important goals.")

# --- econ & ops ---
q("EC:002","Which characteristic distinguishes a service from a good?",
 ["It is intangible.","It can be stored in inventory.","It is always cheaper.","It is produced before it is sold."],
 "Services can't be touched or stored, and they're usually produced and consumed at the same time.")
q("EC:002","Copy paper and cleaning products that a bank buys and uses up regularly are classified as",
 ["supplies.","capital goods.","raw materials.","services."],
 "Supplies are industrial goods continually consumed in operating a business.")
q("EC:005","According to the law of demand, when the price of a product rises, the quantity demanded usually",
 ["falls.","rises.","stays the same.","doubles."],
 "Price and quantity demanded have an inverse relationship.")
q("EC:018","Businesses investing heavily in new plants and equipment is a sign that producers expect",
 ["consumer spending to increase.","a recession.","prices to fall.","a shortage of workers only."],
 "Firms expand capacity when they expect growth (the expansion phase).")
q("EC:010","Which action would most directly increase a bank's profit by reducing expenses?",
 ["Eliminating some free services","Adding free checking for everyone","Lowering loan interest rates","Opening more branches"],
 "Cutting the cost of free services lowers expenses, which raises profit.")
q("EC:016","A government places tariffs on imported steel to protect domestic steelmakers. This is an example of",
 ["protectionism.","free trade.","deflation.","specialization."],
 "Protectionism shields domestic industries from foreign competition.")
q("EC:072","Corporations are more likely to finance with debt than with stock partly because",
 ["interest paid is tax-deductible.","dividends are tax-deductible.","debt has no interest.","stock must be repaid."],
 "The interest deduction lowers the after-tax cost of borrowing.")
q("OP:024","Which is an example of an operating (overhead) cost?",
 ["Monthly utility bill","Raw materials for one product","A one-time purchase of stock","Sales tax collected for the state"],
 "Overhead costs are ongoing costs of running the business, not tied to a specific product.")
q("OP:025","Which employee action best helps control business expenses?",
 ["Eliminating wasteful use of supplies","Ordering extra supplies 'just in case'","Leaving equipment on overnight","Ignoring procedures"],
 "Employees control expenses by reducing waste, protecting assets and working productively.")
q("OP:163","The Six Sigma quality model involves continuously implementing activities that",
 ["improve quality and reduce inefficiencies.","increase defects and costs.","eliminate customer feedback.","lessen decision-making."],
 "Six Sigma relentlessly reduces defects and variation.")
q("OP:519","What is the first step when planning a project?",
 ["Identify the project's stakeholders","Buy the materials","Write the final report","Celebrate completion"],
 "Knowing who is involved and affected shapes every later planning decision.")
q("OP:013","To reduce the chance of cash theft, a business should",
 ["divide cash-related duties among different employees.","let one person handle all cash.","leave cash drawers open.","skip daily cash counts."],
 "Separating duties means no single person can steal and hide it.")

# --- communications, CR, PD ---
q("CO:014","Two loan officers at the same level discuss how to handle a new procedure. This is",
 ["lateral communication.","upward communication.","downward communication.","grapevine gossip."],
 "Lateral (horizontal) communication happens between peers.")
q("CO:016","What is a primary advantage of written communication in business?",
 ["It creates a lasting record that can be referenced later.","It is always faster than talking.","It never needs editing.","It shows tone perfectly."],
 "Written records reduce misunderstandings and provide accountability.")
q("CO:031","A letter to a customer whose loan payment is three months overdue, urging immediate payment, is a",
 ["persuasive message.","informational message.","progress report.","thank-you note."],
 "Collection letters try to get the reader to act, so they're persuasive.")
q("CO:039","A memo explaining a bank's new expense reimbursement policy to employees is a(n)",
 ["informational message.","persuasive message.","complaint letter.","sales letter."],
 "Informational messages communicate facts so readers understand them.")
q("CO:058","Which question would get the most detailed answer from a client?",
 ["What are your goals for retirement?","Do you have a 401(k)?","Are you over 40?","Is your account at our bank?"],
 "Open-ended questions invite full answers. The others can be answered yes or no.")
q("CO:092","A CFO needs to announce a new, non-urgent travel policy to all 800 employees. The best channel is",
 ["a formal company-wide email.","a text to each employee.","a hallway conversation.","a social media post."],
 "Official, non-urgent information for everyone fits a formal written company-wide message.")
q("CR:010","When handling a customer complaint, an employee should offer",
 ["solutions available within the business's policies.","whatever the customer demands.","no response until the customer leaves.","an argument about who is right."],
 "Resolve complaints fairly within company policy, with empathy and follow-up.")
q("PD:012","A team generates as many ideas as possible in 10 minutes without criticizing any of them. This technique is",
 ["brainstorming.","benchmarking.","budgeting.","filtering."],
 "Brainstorming separates idea generation from evaluation.")
q("PD:126","A bank adds an AI tool that speeds up loan approvals. This is best described as",
 ["innovation.","invention.","regression.","consolidation."],
 "Innovation improves or applies something in a new way. Invention creates something that never existed.")
q("PD:018","The most significant benefit of setting personal goals is that it",
 ["provides a clear sense of direction.","guarantees success.","removes all stress.","eliminates the need for planning."],
 "Goals focus effort and give direction.")
q("PD:252","Leo takes a problem directly to the company president instead of his supervisor. He has",
 ["bypassed the chain of command.","followed the chain of command.","used lateral communication.","shown appropriate assertiveness."],
 "The chain of command says to go to your direct supervisor first.")
q("SM:001","The management function that monitors work and compares results to plans is",
 ["controlling.","planning.","staffing.","organizing."],
 "Controlling measures performance against goals and corrects problems.")
q("MK:014","A teen buys a brand of sneakers after seeing popular influencers wear them. This is a",
 ["social influence on buying behavior.","psychological influence only.","situational influence.","economic influence."],
 "Social factors include family, friends, reference groups and celebrities or influencers.")
q("BL:002","In a contract, what each party gives or receives in exchange is called",
 ["consideration.","capacity.","an offer.","a tort."],
 "Consideration is the bargained-for exchange of value that makes a contract binding.")
q("BL:003","A form of business organization whose primary goal is a mission other than profit is a",
 ["nonprofit.","sole proprietorship.","partnership.","C corporation."],
 "Nonprofits pursue social or charitable missions. Profits are reinvested, not distributed.")
q("BL:072","An agent who acts on behalf of a principal must",
 ["act in the best interest of the principal.","act only in their own interest.","keep all profits.","ignore the principal's instructions."],
 "Agents owe fiduciary duties of loyalty, obedience and care to the principal.")
q("FI:351","Accountants must present financial information that is",
 ["objective.","biased toward management.","exaggerated.","kept secret from auditors."],
 "Objectivity means unbiased, factual reporting.")
q("FI:356","A company selling securities to the public must",
 ["tell investors about the risks of the securities.","guarantee investors will profit.","avoid answering questions.","sell only risk-free securities."],
 "Securities laws require full and fair disclosure of material risks.")
