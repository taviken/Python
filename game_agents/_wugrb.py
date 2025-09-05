"""Implementation of the MTG color alignments system, using a normalized radar chart style data structure.
Based on this article https://homosabiens.substack.com/p/the-mtg-color-wheel
"""

from ._normal import NormalArray
from typing import Dict


class WUBRG:
    def __init__(self):
        self.array = NormalArray(("white", "blue", "black", "red", "green"))

    def inc_w(self):
        self.array.inc("white")

    def inc_u(self):
        self.array.inc("blue")

    def inc_b(self):
        self.array.inc("black")

    def inc_r(self):
        self.array.inc("red")

    def inc_g(self):
        self.array.inc("green")

    @property
    def asdict(self) -> Dict[str, float]:
        return self.array.normalized

    @property
    def white(self):
        """
        White seeks peace, and it tries to achieve that peace through the imposition
        of order. White believes that the solution to all suffering and unhappiness
        is coordination and cooperation and rules and restraint. The archetypal
        white organization would be a church, and a white dystopia would be a fascist
        regime such as the one in George Orwell's 1984, or a stagnant society like
        the one in Lois Lowry's The Giver.

        From a negative perspective, white craves order. It needs certainty, predictability,
        clear expectations. Rules. Clear distinctions. Justice. White struggles
        with ambiguity and nuance, and doesn't do a good job of stepping outside
        of its own frame or perspective.

        A white agent, when injured or disoriented or low-resourced, will tend
        to double down on structure—trying to force things into place, ignoring
        or attacking anything that threatens to not-fit its preconceptions. And
        with too much white, things ossify, freezing into suffocating unchangeability,
        rituals that are empty of meaning and have lost their original purpose
        """
        return self.asdict["white"]

    @property
    def blue(self):
        """
        Blue seeks perfection, and it tries to achieve that perfection through
        the pursuit of knowledge. Blue believes that things could be almost arbitrarily
        good if we could all just figure out the truth, and then apply that understanding
        to its fullest extent. The archetypal blue organization would be a university
        or a research lab, and a blue dystopia would be one in which efficiency
        were pursued without morals or limits, or in which intelligence were the
        sole axis of a meritocracy.

        Victory for a blue agent feels like clarity, revelation, actualization,
        conclusion — a final puzzle piece clicking into place, or the last note
        of a perfect symphonic performance. Defeat feels like everything is slippery,
        foggy, intractable (and will be evermore), like there's no path forward
        and nothing to be done, like all of the potential is wasted and all of
        the confusion is permanent.

        From a negative perspective, blue craves clarity. Its need to see and understand
        and optimize can become frantic, like a child clutching a stuffed animal—even
        if knowledge won't do anything, won't allow for any new actions or help
        in any way, blue will often scrabble for it, even at the expense of other
        stuff that would help. A blue agent, when injured or disoriented or low-resourced,
        will often perseverate, spinning its wheels on irrelevant questions or
        tinkering with trivialities as a way to avoid having to engage with the
        big things it doesn't understand and doesn't feel ready for.
        """
        return self.asdict["blue"]

    @property
    def black(self):
        """
        Black seeks satisfaction, and it tries to achieve that satisfaction through
        ruthlessness. Black wants power and agency so that it can act upon its
        preferences at any time, doing whatever it wants, whenever it wants, and
        reshaping the world around it as it sees fit.. It recognizes no limits
        upon this pursuit except those which emerge from its own desires and self-interest.
        It is capable of cooperation and alliance, but only consequentially, as
        in game theory; at its core, black is amoral, not immoral, since it doesn't
        think morality is even really a Thing. The archetypal black organization
        would be a hedge fund or a startup, and a black dystopia would be a totalitarian
        dictatorship.

        Victory for a black agent feels hefty, exultant, and satisfying, like a
        bag of gold coins or a heavy hammer — it's the feeling you have when you
        know that the game is won, even if you haven't yet crossed the finish line.
        Defeat, on the other hand, feels like aging or imprisonment — like scrabbling
        against an unscalable wall behind which your dreams are turning to ash
        and trickling away, leaving you with nothing.

        From a negative perspective, black can't handle codependency or obligation.
        It starts to freak out if it feels penned-in, depended-upon, trapped, drained.
        A black agent, when injured or disoriented or low-resourced, is extremely
        loath to cooperate, to invest, to engage in interactions that don't visibly
        and immediately pay off. Black needs a feeling of power and possibility
        and potential, and when that's missing or threatened, it tends to shift
        even harder into a kind of short-sighted transactional mode, often driving
        away precisely the people and opportunities that would have helped. With
        too much black, concepts like “cooperation” and “sustainability” drop away—black-out-of-balance
        is like a wildfire, consuming everything as quickly as possible, sowing
        the seeds of its own suffocation.
        """
        return self.asdict["black"]

    @property
    def red(self):
        """
        Red seeks freedom, and it tries to achieve that freedom through action.
        Red wants the ability to live in the moment and follow the thread of aliveness
        and passion. It's a bit strange to speak of a red “organization,” but to
        the extent that it's possible to have an archetypal red organization, it
        would be one of those art studios that's owned by no one where there's
        paint on every wall and it's almost impossible to move around what with
        all of the dancing and debating and half-finished projects. A red dystopia,
        on the other hand, would simply be anarchy.

        From a negative perspective, red is pathologically incapable of accepting
        limitations—the sort of person who's unable to marry because they're unable
        to commit, because committing means cutting off avenues of future possibility.
        It's also unable to tolerate quietness, emptiness, boredom, ennui. Red
        is restless, needing independence, freedom of movement, a sense of unconstrained
        choice, passion.

        A red agent, when injured or disoriented or low-resourced, will tend to
        flail or explode, magnifying and amplifying its emotions and then following
        them wherever they lead (and justifying the actions it takes as being valid
        and unimpeachable because they came from the heart). Red, fearing a loss
        of freedom and direction, responds by breaking everything around it and
        driving as hard and fast as it can in whatever direction it happens to
        be facing. With too much red, there's no pattern, no ground to stand on,
        no reliability, no predictability.
        """
        return self.asdict["red"]

    @property
    def green(self):
        """
        Green seeks harmony, and it tries to achieve that harmony through acceptance.
        Green is the color of nature, wisdom, stoicism, taoism, and destiny; it
        believes that most of the suffering and misfortune in the world comes from
        attempts to cast off one's natural mantle, step outside of one's natural
        role, or fix things which aren't broken — it's the color of Chesterton's
        Fence. It seeks to embrace what is, harmony as distinct from order — the
        archetypal green organization would be a hippie commune, or the pop culture
        interpretation of a Native American tribe (such as in Disney's Pocahontas),
        while a green dystopia would be something like the society in Divergent
        or a tribe with absolutely rigid traditions and an unchanging and unchangeable
        relationship to its environment.

        From a negative perspective, green is pathologically passive. It has too
        much faith in everything working out, in things being the way they should
        be, in accepting whatever comes, however horrible. It can be phlegmatic
        to a fault, passing up opportunities to save itself and refusing to prepare
        for predictable, oncoming change. Green struggles with taking a stand,
        and is suspicious of any kind of novel agency.

        A green agent, when injured or disoriented or low-resourced, will often
        surrender or give up, turning to blind faith or repeating its default actions
        over and over again, unable to try something new. Worse, out-of-balance
        green will often undermine or sabotage others' attempts to salvage a situation,
        dragging everyone else down with it. Green tends to fall back on what it
        already knows, regardless of whether that's appropriate. And with too much
        green, all distinctions between good and bad, or better and worse, fall
        away, and everything becomes gray and indistinguishable.
        """
        return self.asdict["green"]
