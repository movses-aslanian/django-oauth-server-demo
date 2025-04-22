from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):
    oidc_claim_scope = OAuth2Validator.oidc_claim_scope
    oidc_claim_scope.update({
        "email": "openid",
        "name": "openid",
    })

    def get_additional_claims(self, request):
        user = request.user
        return {
            "name": ' '.join([user.first_name, user.last_name]),
            "email": request.user.email,
        }
