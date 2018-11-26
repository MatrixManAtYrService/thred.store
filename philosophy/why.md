# Why build thred.store

## Because I want us to be ready, whether or not crypto is the future

Technology exists to solve problems.
Money is a technology.
For example, when Caesar paid his troops with Roman coin and then demanded that concquered lands pay taxes with those coins, he was solving the problem of how to feed his troops even when they were in distant lands.
At the time, few would have expected that a superior technology could exist.
Times have changed.
Cryptocurrencies as we know them today are probably not ready to compete with existing monetary systems, but they are evolving faster.
There may be a time when we must choose whether to upgrade, and if you work in technology you know that upgrading can be a bumpy, but potentially worthwhile process.

As users, how should we feel about this upgrade?
Maybe the bumps aren't worth it--maybe we should stick with what we have.
On the other hand, if our system's competators become more efficient, that could lead to a bumpy future as well.

    Choices

          U := upgrade
         ~U := don't upgrade

It would be very typical of humans if we formed cliques and disagreed about this in unproductive ways.
Please suspend any reflex you have along those lines, at least for now.
I believe that even if we disagree about what we should do ultimately, we may be able to agree about how to prepare for it.

    Proposed Action

          A := Educate people on the fundamentals of cryptocurrency and provide them with safe ways to use it

    Harm Reduction Predicate

     H(x,y) := If we want to make the hazards of x less painful, we should y

    Future Decision

        U or ~U

    Current Dilemma

        H(U, A) or H(~U, A) => A

That is to say: whichever path we choose, being prepared means taking many of the same steps.
In this essay I will argue that using thred.store is a good first step.
For those who think crypto is the future, we will look at why it addresses the needs of such a society.
Then we will look at how thred.store can be used to teach math, computer science, and security fundamentals--skills that will be relevant to navigating a cryptocurrency-capable world, even if we decide against replacing existing monetary systems with cryptocurrencies.

Throughout, I will be taking the statements below for granted:

    Premises for This Essay

        P1. Cryptocurrencies only work well if users can control whether and when their secrets are shared.
        P2. If you understand nothing about a technology that you use, you risk being manipulated by those who do.

# If Crypto is the future, how should we prepare now?

    Premises for this section:

        If cryptocurrency is the future...

            Q0. Some people will decide against using banks at all.
            Q1. Criminals will learn to steal secrets, even in "cold storage", and perhaps violently.
            Q2. Criminals won't try as hard to steal secrets if it takes multiple stolen secrets to access value.
            Q3. Sometimes people will want trusted others to have access to their secrets.
            Q4. As the ability of individuals to solve their own problems increases, the need for external authority diminishes.

Currently, we allow banks (governments, and credit reporting agencies) to be authorities about our financial lives.
Maybe this as somewhat of a hazard--it means that these entities can be fooled (or coerced) into exposing our secrets or controlling our access to money, but it is also useful because if somebody "steals my identity" I can contact such an authority and expect them to fix it.
If crypto is the future, there will be people who decline to grant that authority to a third party.
These people will essentially be their own banks, notaries and (with sufficient inginuity and community participation) credit reporting agencies.
From a financial perspective, there will be no way for these people to recover their identity--or any of the money associated with it--if it is "stolen".
They will just have to create a new identity and start from scratch.

Every cryptocurrency that I have met so far requires users to generate a secret which they will use to authorize transactions.
This usually looks like either a large number stored on a computer that they trust, or a piece of paper with secret words written on it.
Usually it's both.
There are ways to keep the secret on the computer safe--they differ depending on the cryptocurrency (and particularly the wallet software) in use.
These methods are important, but they're not part of the problem that thred.store is trying to solve.
thred.store concerns itself with how we should treat that list of secret words.

The question is this:

 > How should I treat a list of secret words if...
 >      - losing it means I lose all of my money
 >      - somebody who finds it gets all of my money
 >      - somebody who finds it can impersonate me
 >      - I want trusted people to be able to recover my money if for some reason I am unable to access it myself
 >      - I want multiple trusted people to have to collaborate before they have access

Maybe secrets like this should be stored in a bank safe deposit box, but people who are unwilling to authorize a bank to monitor their funds are also unlikely to authorize a bank to monitor the secret that controls their funds.
For those users that decide against relying on a powerful trusted(?) organization to keep their secrets, there are some problems:

    1. If more copies of a secret exist, then you are less likely to lose it.
    2. If fewer copies of a secret exist, then an enemy is more likely to find it.
    3. If individual secrets allow unlimited access, they will attract potentially dangerous attention to the people that store them.
    4. Over time, secrets on paper may be destroyed by fire, mold, or other entropy sources.

It is hard to come up with examples of items that make better targets for theives.
These lists of secret words are a very juicy combination of high-value, easy-to-steal, and easy-to-sell-anonymously.
Right now, they are so scarce that they are not worth breaking into somebody's house to look for, but if crypto is the future then they may become more common.
With a little forethought, we can avoid creating situations that contribute to the criminal element.
If the majority of secret stores are protected in a way that makes them useless without some stored-elsewhere secret, the practice of stealing them will never become popular in the first place.

So far as I know there are only a few documented solutions to these problems.
You can address problems 1 and 2 by buying multiple electronic gadgets which protect the word-lists with passwords and then storing backups of those gadgets with trusted people.
You can address problem 4 with metal gadgets that encode data in fire-resistant ways.
You can address problem 3 by storing only partial word-lists with trusted people.
I build thred.store to address all of these problems as cheaply and accessably as possible.

If crypto is the future then thred.store is a human-doable offline multi-factor encryption system designed to support delegated trust and resist technologically advanced adversaries.
The two-factor systems of today involve the combination of something-you-have and something-you-know to authenticate you as the trusted user.
thred.store uses this concept to encrypt your secrets in a way that you can decrypt on your own, but that can also be decrypted by configurable subsets of your trusted-others.

Problems 1 and 2 are addressed by ensuring that no single component of the system can grant access to the wallet(s).
Problem 3 is addressed by allowing the user to configure which combinations of trusted-others can gain access and recommending that they not put ultimate power in any one trusted other's hands.
Problem 4 is addressed by providing a method of encoding words on easily accessable time-resistant materials (nuts, bolts, and washers are recommended, but any way to durably persist a sequence of differently sized objects will do).

The trade-off is that thred.store is not easy to use, so you could say that it introduces a fifth problem that _is_ addressed by the solutions mentioned above.

    5. Trusted users may fail to recover a secret because they either:
        - don't recognize it as a valuable secret
        - don't understand how to decode it

Because of this it is important to understand that thred.store is 10% metal, 20% documenation, and 70% social expectation.
If it is going to help protect future generations in crypto-enabled future, then that community must maintain a relatively high bar for the competences required to use it.
It will also require that individual sets of trusted-others think carefuly about how they configure their thred.stores so that value always flows when it should and never flows when it shouldn't.
Occasional practice might also be a good idea.

If this project was about making a product, then the above constraints would be too stringent to make thred.store worthwhile.
Humans don't typically overflow with decades-ahead forethought, the motivation to maintain exceptional numeracy in their communities, or social connections that can be relied on to treat complex secrets properly.
Perhaps I am being unrealistic.
But this endeavor is not about reselling bought-in-bulk metal washers at a markup.

Part of it is about keeping future generations safe from certain pitfalls that we already associate with cryptocurrency.
We can do this by providing a recipe for secret storage, which is what thred.store is.
But the other part is about providing a set of standards.
Are we thoughtful enough, or will our failure to plan for the future cause heartache down the road?
Are we competent enough, or is our trust in cryptography a blind one?
Are our personal trust networks solid enough, or do we need third parties to have authority over our financial dealings?
I don't know these answers, but I hope that one day we can handle these things.
Maybe using thred.store can give us some practice.

# If Crypto is not the future, how should we prepare now?


    Premises for this section:

        R0. Current infrastructure will be unable to handle the load that micropayments (when they become commonplace) will place on it.
        R1. If alternative economies exist with a lower cost of doing business, they will siphon value away from existing ones.
        R2. Powerful arbitrators of financial dealings are less likely to abuse their power if they know they can be replaced.
        R3. We would benefit from raising the bar for what counts as numeracy and computer literacy, especially in the areas of privacy and security.

In this section I will model an economy as a technology that serves its users by providing trusted computation in exchange for being granted arbitration authority over financial conflicts.
I believe this model matches our own in important ways.
One of its failure modes appears to be historically uncommon, but I think we can expect it to be more prevalent in the future.
We should want to avoid such a failure and work to mitigate the harm, should it come to pass, and I will argue that the best way to achieve both of these goals is to change the way we educate future generations about technology.
Finally, I'll argue that thred.store acts as both textbook and standardized-test that we can use to teach and evaluate the kind of technological competencies that I am talking about.

We will start with a fiction.
Imagine a busy marketplace where buyers and sellers come together to do business, but nobody wants to carry any money because they don't have any pockets.
Elsewhere there is a room full of people--each armed with an abacus--whose job it is to keep track of how much money which buyer or seller should control.
All day, the marketplace collects notes that determine how money should flow between the people, and later those notes are taken to the room full of people with abaci, who stay up all night making sure that all the money is accounted for.
The next morning more notes make it back to the marketplace, and the cycle starts over.

A typical user of this system specializes in what they produce--so they have many of one thing to sell, but they also have households to run, so they need to buy small amounts of many different things.
If a user can go to the market with lots of one type of value and exchange things until he has many small values that meet his needs then he doesn't have to return to the market on the following day.
If he can't solve that problem in a day he must return the next day and continue the process.
Sometimes, a user would have enough time to make all his transactions in one day, but he has to stop part-way becuase he needs the notes to make it to the abacus people and back before he can continue.
That loss of time is just the cost of doing business.

In addition to computing the who-has-what-money amounts each night, the abacus people are in charge of resolving disputes over who actually sent which money to whom.
They discourage bad behavior among the users by using their priviliged position in the arbitration over financial matters to punish bad actors.
They used to extract fees for their services on a per-transaction basis, but lately they have been finding other ways to use that position to pay the bills.

Coming up with enough abaci to compete with the existing system is expensive, so nobody worries about a competator springing up locally and using the same marketplace to replace the abacus people.
Distant competators exist, but they're all doing pretty much the same thing, so it seems unlikely that they'll take over here at home.
For a time, the system is stable.

But then three technologies emerge:
The pocket calculator is invented (and they're cheap), waiting all night for the notes to come back from the abacus people seems kind of silly--why are they still using abaci?
The telephone is invented; every day, before the market opens, users call each other to decide which transactions they will perform--as long as they can trust each other's word, they can make transactions more efficiently--which means more time spet at home making things to sell and less time making return trips to the market.
Advertising improves, and with it improves ability of users to trick each other into behaving against their best intrests in the market.

The abacus people are still in charge of being the authority on transactions, so even though their computational services are worth less, they are still able to justify the authority that they have been extending over the users in lieu of actually charging money for their services.
But they have two big problems.

One is that the extension of that authority over the users has eroded the inherent trust that used to exist between them.
As a result, they've started using very small transactions to solve problems that they used to use trust to solve.
Nobody is sure how far it will go, but some users have gone from tens of transactions per day to hundreds per day.
The abacus people used to finish the notes by midnight, but lately it has been more like 1:00AM.
Nobody is sure what will happen when they can't finish before the next day starts.

An example of user turning to micropayments to solve non-financial problems is when those with access to money started been paying others to stand in lines for them.
This got so bad at one point that the the less powerful users spent whole days at the market without making a single transaction, they just stood there and watched the rich users swap places with people in front of them.
Living close enough to the market to arrive early and provide this service has made several users very rich.

Two practices emerged to combate this.
One is a clever trick with the pocket calculators.
Using some math that I wont get into here, users devised a system for keeping track of their place in line so that when they get back to the market, they aren't edged-out by people who arrived earlier.
The other is line-entry-fees.
By requiring a small fee every time somebody enters a line, users have made being a placeholder prohibitively expensive.
This has fixed the problem of placeholders edging out legitimate users, but nobody knows if the abacus people can handle the increase in transaction volume.

Besides the question of whether they can handle the burden of centralizing the daily flood of transactions in a timely way, the abacus people have noticed another problem.
Ever since the users started using their pocket calculators, certain ones have stopped coming to the market as frequently as they used to.
The theory is that these users make arrangements over the phone and travel to each other's houses to exchange goods.
They appear to have found a way to use those pocket calculators to avoid waiting on the bank to process transactions.

Only a few users are doing this, but the concern is that those users have avoided paying the typical cost of doing business--both in terms of waiting for abacus people, and in terms of accepting their authority to arbitrate.
Provided they can find an efficient way to settle disputes and move goods, they will have an advantage over the other users.

This is especially concerning to the abacus people because they've been keeping food on the table by offering services that help the rich get richer, rather than producing things you can use or eat.
Suppose half of the value that flows through the market every day were to stop showing up.
Whether the abacus people could find something to eat would depend on which half had dissapeared.
The rich-get-richer-services are unlikely to leave because they function by using abacus-arbitration-authority to inject costs-of-doing-business into the market and profiting off those.
They would be less effective in a market with fewer costs-of-doing-business.
The segment of the market that is most likely to leave is the things-people-actually-need segment, since they'll be just fine without the other half.

This fiction ends with the abacus people facing a choice:
    1. Treat the emerging system as competition, and work to provide a better service so that it doesn't take hold.
    2. Treat the users of the emerging system as criminals, and lean on existing authority to drive up their costs of doing business so that the traditional market is once again the cheaper option.
    3. Ignore the emerging system and trust that it will fail on its own.
As users, we should hope that they choose the first, but that means we're going to need to teach them to use pocket calculators.

I hope that the correspondence between this model and our world is easy to see.
My experience with the technology in use by banks and similar organization does not exactly indicate that they use abaci, but the technologies that they do use are typically quite dated.
I am not sure about the first non-financial problem we will see solved by micropayments, but it is coming.
A couple that come to mind involve automated vehicles exchanging tokens to navigate merges and lane changes or web servers collecting micropayments to make denial-of-service attacks cost prohibitive.
I cannot measure the impact that waiting for banks (either to open, or to clear a transaction) has on overall economic efficiency, but when alternatives arive without those delays I expect that in retrospect we'll see that it is significant.
The users in my fictional economy have some challenging times ahead, and although the correspondence with our world isn't perfect, I think that it is close enough that we should probably be prepared for similar ones.

So far in this section, the point is that our financial institutions are only used to competing with equally inefficient institutions of the same kind, and that they are not prepared to compete with something else entirely.
Until recently, the thought of jumpstarting an alternative economy and doing business in it was absurd.
You'd have to print your own money, enforce laws around it, and still figure out how banking should work--all at a lower cost than the original system.
But a mature cryptocurrency would handle all of those problems at a fraction of the cost of the current system.
Eventually, the potential savings will outweigh the risks, and people will start trying out alternatives.

In order to remain competative, our monetary infrastructure will need to run 24/7, with minimal human intervention, and with as few middlemen as possible.
Otherwise, the costs (in delay-seconds or human-wage-dollars) will have to be offloaded onto users as costs-of-doing-business.
We'll also need to drastically reduce occurrances of "identity theft" so that whoever bears the cost of fraudlent activity has to bear less of it (because these costs also trickle down).
For the former, we'll need to get more familliar with code.
For the latter, we'll need to adopt something like asymetric cryptography for identifying payers.

The best way to learn to code is to have a computational problem that you need to solve.
Whether you're encoding or decoding a secret, working with thred.store means solving a series of computational problems.
It was designed so that each problem could--at least in principle--be solved with a pencil and paper.
They're bite sized and easy to learn.
This might get tedious, so writing code to help with the dull parts is an expected step when teaching with thred.store.
It would be easy to provide code that does the job, but since thred.store handles secrets, students should be suspicious of trusting any code they did not write.
To uphold this idea (and prevent cheating), I would recommend that students only be allowed to use code they had written for thred.store activities.

Such an activity might look like this:
A teacher gives each student a thred.store and requires that they find the encoded word by the end of the week.
During that time, students study how numbers are represented in various bases (thred.store uses base 4 by default) and how to convert them (base 26 works well for decoding into words).
As students come up with their hidden words, the teacher can know that those students are ready to move on.
This is likely the first lesson, and it wouldn't require that the students write any code, but later lessons could involve the making and breaking of rudimentary cryptosystems.
It takes very little code to achieve these tasks, and I believe students would quickly see the value in automating their work.


thred.store is connected to a wealth of mathematical concepts, and although mastery of these concepts is not needed for basic usage, one does not have to go too far afield to devise hands-on excercises that can help teach them.
Here are some examples:

- Modular arithmetic comes up quite naturally when trying to use key-addition to encrypt values.
- Good old fashioned find-x type algebra is necessary when determining the maximum storage capacity of a given set of hardware or working with (BIP-39 type) checksums.
- The frequencies of washer-sizes that get used for various encoding schemes differs in interesting ways and could be a starting point for a lesson in statistics.
- Sequential data manipulations for trust delegation afford opportunities to talk about functions (injections vs surjections, etc) and commutativity.
- The natural way to handle snippits of thred.store helper code is through function composition.  In the thred.store case this translates nicely to category theory.

If we can manage to replace the TI-83 graphing calculator with something like a Jupyter notebook running python, and if we can teach students to lean on such computational resources whenever they need to do something repetative, then I think we'll have taken a significant step towards building an economy that can remain competative in the future.
It is, after all, a willingness to repeatedly perform trivial computation by hand that leads to rooms full of abacus people.
What we need are people who will point out inefficiency and say: "I know a better way".
In addition to using thred.store to teach some relevant math, I hope that it will motivate this shift in tooling.

