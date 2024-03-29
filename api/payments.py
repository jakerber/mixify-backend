"""Stripe API wrapper module."""
import config
import stripe

stripe.api_key = config.STRIPE_SECRET_KEY


def create_boost_payment(cost_usd: float, queue_song_id: str, fpjs_visitor_id: str) -> str:
    """Create a Stripe payment intent for Mixify boost.

    :param cost_usd: payment amount in USD
    :param queue_song_id: ID of song being boosted
    :param fpjs_visitor_id: FingerprintJS visitor ID
    :return: intent client secret
    """
    intent = stripe.PaymentIntent.create(
        amount=int(cost_usd * 100),
        currency='usd',
        automatic_payment_methods={'enabled': True},
        description='Mixify Boost',
        statement_descriptor='Mixify Boost',
        metadata={
            'queue_song_id': queue_song_id,
            'fpjs_visitor_id': fpjs_visitor_id
        })
    return intent.client_secret
