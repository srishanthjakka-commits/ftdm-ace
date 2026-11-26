# Economics speaking drills for the Econ Lab (prep 1 minute, speak 1 minute). Added Nov 2026 for regionals.
# Each model is a strong 45-60 second answer: Answer -> Reason -> Example -> Tie back to the client.
DRILLS = []
def drill(id, scenario, pis, model):
    DRILLS.append(dict(id=id, scenario=scenario, pis=pis, model=model, style="client", econ=True))

drill("e-opportunity-cost", "A client (judge) says: \"I can afford a $40,000 truck, so why shouldn't I buy it?\" Explain the real cost.",
 ["EC:001","EC:006"],
 "Being able to afford it isn't the whole story; the real cost is the opportunity cost. Say a used truck would do the same job for $25,000. The extra $15,000 could go into a Roth IRA instead, and at a 7% average return it could grow to roughly $58,000 in 20 years. Interest is a price too: a bigger loan at today's rates means paying more for the same years of driving. So our advice is to pick the truck that meets your needs, then put the difference to work.")
drill("e-supply-demand-homes", "A first-time buyer (judge) asks: \"Rates are about 7%. Why haven't home prices dropped?\"",
 ["EC:005","EC:084"],
 "It's supply and demand. Higher rates did cool demand, but they cut supply even more: millions of owners have mortgages below 4% and don't want to sell and give that up. Fewer homes for sale means buyers still compete, so prices stay high. With the 30-year rate near 7.11% in November 2026, the smart move is to buy only when the payment fits, about 28% of gross income, and plan to refinance if rates fall. Waiting for prices to crash could take years.")
drill("e-gdp-explain", "A judge asks your team to explain GDP in plain language and say what last quarter's number means for a small business.",
 ["EC:017","EC:018"],
 "GDP is the total value of everything the country produces in a period, from haircuts to cars. Real GDP removes inflation so we can see if we actually made more. Real GDP grew at a 3.4% annual rate in the third quarter of 2026, which means the economy is expanding: more spending, more hiring. For a small business, that's a decent time to grow, but GDP looks backward, so we'd still keep a cash reserve and a line of credit in case growth slows.")
drill("e-unemployment-types", "A recent graduate (judge) asks: \"Unemployment is only about 4%, so why can't my cousin find a job?\"",
 ["EC:082","EC:003"],
 "A low overall rate doesn't mean every job seeker finds work quickly. Some unemployment is frictional, people between jobs; some is structural, when skills don't match the jobs open, like tellers replaced by apps. Your cousin may be in a field with fewer openings. The fix is human capital: a short certificate in a growing field or new skills that match job postings. Meanwhile, a part-time job keeps income coming and builds experience.")
drill("e-inflation-pricing", "A coffee shop owner (judge) says costs are up 8% this year and asks whether to raise prices.",
 ["EC:083","EC:010"],
 "Yes, but selectively. With inflation at 3.7% and your costs up 8%, absorbing it all would shrink your margin. Raise prices most on drinks customers love and can't easily find elsewhere, like specialty lattes, and hold prices on basics that customers compare. Small, regular increases cause less pushback than one big jump. Cut waste and renegotiate with your milk supplier too. That protects profit without sending loyal customers to the chain down the street.")
drill("e-fed-hike", "A client (judge) asks: \"The Fed raised rates again. What does that mean for me?\"",
 ["EC:084","EC:083"],
 "It depends which side of the rate you're on. The Fed raised its target to 3.75%-4.00% in September 2026 to slow inflation. As a saver, you win: high-yield savings and CDs pay more. As a borrower, you lose, especially on variable debt: credit cards and home equity lines move with the prime rate, now about 7%. So we'd pay down your credit card first, move savings to a high-yield account, and lock a fixed rate on any new loan.")
drill("e-recession-prep", "A salon owner (judge) asks how to prepare for a recession that might or might not come.",
 ["EC:018","EC:011"],
 "Prepare while times are good, because that's when banks lend easily. First, build cash reserves of three to six months of fixed costs. Second, open a line of credit now, even if you don't use it. Third, keep some costs flexible, like booth rentals or part-time staff. Salons are discretionary, so clients stretch visits in a downturn, but loyalty programs and memberships keep them coming. The 2020 recession lasted two months and 2008's lasted 18; reserves get you through either.")
drill("e-tariff-explain", "A gift shop owner (judge) asks: \"Who actually pays for tariffs?\"",
 ["EC:016","EC:008"],
 "The importer pays the tariff first: when your goods arrive, you or your supplier pay the tax at the border. Then the cost gets shared. You can raise prices, which shifts some to customers; accept a lower margin; or switch to a supplier in a lower-tariff country. The average effective U.S. tariff rate was about 6.7% in July 2026, but around 23% on goods from China. So we'd check where each product comes from and price the most affected items accordingly.")
drill("e-strong-dollar", "An exporter (judge) asks: \"Is a strong dollar good or bad for my business?\"",
 ["EC:100","EC:104"],
 "For an exporter, a strong dollar is mostly a headwind. It makes your products more expensive for foreign buyers, and payments in yen or euros convert into fewer dollars. In November 2026 a dollar bought about 159 yen, near a multi-year high. It does help on the cost side if you import materials. To manage it, we'd use forward contracts to lock exchange rates on confirmed orders and price in a way that keeps you competitive.")
drill("e-business-model", "A judge asks: \"How does a bank make money, and how is that different from an app like Chime?\"",
 ["EC:138","EC:012"],
 "A traditional bank mainly earns the spread: it pays depositors one rate and lends that money out at a higher rate, plus fees. A fintech like Chime earns mostly interchange fees, the small cut merchants pay each time a member swipes a debit card, according to its 2025 IPO filing. That's why fintechs push card use and banks push loans. For a bank competing with Chime, the edge is lending and advice, so we'd lead with fast personal and small-business loans.")
drill("e-bribe-request", "A judge playing a client says: \"Our overseas agent wants a small payment to an official to speed up our permit. It's normal there. Okay?\"",
 ["EC:140","EC:106"],
 "No, and here's why. The Foreign Corrupt Practices Act makes paying a foreign official to win or speed up business a federal crime for U.S. companies, even overseas. Penalties can reach billions: Siemens paid about $1.6 billion in 2008. Beyond the law, it signals that your company can be pressured again. Decline politely, document the request, report it to legal, and use a licensed customs broker and official channels. A slower permit is far cheaper than a bribery case.")
drill("e-culture-meeting", "A client (judge) is meeting investors from Japan next week and asks how to prepare.",
 ["EC:110","EC:045"],
 "Research the business culture and focus on relationships first. Japan is a high-context culture: meaning comes from relationships and tone, not just words. Exchange business cards with both hands and read them before putting them away. Expect decisions to take time, because they're often made by group consensus, so don't push for an answer in the first meeting. Bring materials in Japanese if possible and confirm next steps in writing afterward. Respect builds the trust that closes deals.")
drill("e-diminishing", "A bakery owner (judge) asks: \"Sales are up. Should I hire two more bakers?\"",
 ["EC:023","EC:013"],
 "Maybe not, because of diminishing returns. With one oven, each extra baker adds less output: if the third baker added 50 loaves but a fourth would add only 20, the oven is your bottleneck. Two more bakers would mostly wait their turn while costing full wages. Instead, we'd finance a second oven, which raises every baker's productivity. Compare the extra output to the cost: equipment that doubles capacity usually beats paying for people who can't use it.")
drill("e-small-biz-value", "A town council member (judge) asks: \"Why should our town care whether small businesses survive?\"",
 ["EC:065","EC:070"],
 "Because small businesses are the local economy. Nationally, they're 99.9% of all businesses and employ about 46% of workers, according to the SBA. Locally, they hire neighbors, buy from local suppliers and pay taxes that fund schools and roads, and the money they earn gets spent again in town. They also keep big chains competitive. So the town can help with a small-business loan fund through local banks and simple permitting, which pays back in jobs and tax revenue.")
