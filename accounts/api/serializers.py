from rest_framework import serializers

from accounts.models import Account

# class LoginSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ['email', 'password',]

# 		extra_kwargs = {'password': {'write_only': True}}

# 	def validate(self, data):
# 		password = data.get('password')
# 		email = data.get('email')

#auth
class AuthSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['email']
    def save(self):
        email = self.validated_data['email']
        if Account.objects.filter(email=email).exists():
            u = Account.objects.get(email=email)
            raise serializers.ValidationError({
                'user_id': u.id,
                'login_type': "signin", 
            })
            # raise serializers.ValidationError({'email': 'email already exsists.'})
        print(email)
        return email

class RegistrationSerializers(serializers.HyperlinkedModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # firstname = serializers.CharField(style={'input_type': 'text'}, write_only=False)
    # lastname = serializers.CharField(style={'input_type': 'text'}, write_only=False)
    
    class Meta:
        model = Account
        fields = ['email', 'password','first_name', 'last_name', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def	save(self):

        account = Account(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            # username=self.validated_data['username'],
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        # user, created = User.objects.get_or_create(email=account.email)
        # if created:    
        #     account.set_password(password)
        #     account.save()
        # else:
        #     raise serializers.ValidationError({'email': 'email exsists.'})
        # global u
        # try:
        #     u = User.objects.get(email=account.email)
        # except u.Exist:
        #     raise serializers.ValidationError({'email': 'email exsists.'})
        # response for register
        if Account.objects.filter(email=account.email).exists():
            # u = User.objects.get(email=account.email)
            # raise serializers.ValidationError({
            #     'user_id': u.id,
            #     'login_type': "signin", 
            # })
            raise serializers.ValidationError({'email': 'email already exsists.'})
        else:
            account.set_password(password)
            account.save()
        return account
    
        