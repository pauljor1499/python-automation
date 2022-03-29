<template>
	<div class="logInPage">
		<div class="error" v-if="error">
			<h3 id="wrongcredentialError">{{ errorMessage }}</h3>
		</div>
		<router-link :to="'/'">
			<div class="titleContainer">
				<h1 class="title1">Math</h1>
				<h1 class="title2">World</h1>
			</div>
		</router-link>
		<div class="loginFormContainer">
			<h1>Log In</h1>
			<div>as</div>
			<br />

			<n-button-group>
				<n-button
					strong
					round
					:color="role == 'Student' ? '#253759' : none"
					id="asStudent"
					@click="this.changeRole"
				>
					Student
				</n-button>
				<n-button
					strong
					round
					:color="role == 'Teacher' ? '#253759' : none"
					id="asTeacher"
					@click="this.changeRole"
				>
					Teacher
				</n-button>
			</n-button-group>

			<div class="loginForm">
				<br />

				<label for="text">Email</label>
				<input type="text" name="email" id="email" v-model="email" />
				<div
					class="errorMessage"
					id="emailRequired"
					v-if="!hasEmail && this.clicked"
				>
					Email is required
				</div>
				<div
					class="errorMessage"
					id="emailMustValid"
					v-if="!checkValidity && this.email && this.clicked"
				>
					Email must be valid
				</div>

				<div
					class="errorMessage"
					id="emailTooLong"
					v-if="emailTooLong && this.email && this.clicked"
				>
					Email too long
				</div>
				<label for="password">Password</label>
				<input
					type="password"
					name="password"
					id="password"
					v-model="password"
				/>
				<div
					class="errorMessage"
					id="passwordRequired"
					v-if="!hasPassword && this.clicked"
				>
					Password is required
				</div>
				<div
					class="errorMessage"
					id="passwordTooLong"
					v-if="passwordTooLong && this.clicked"
				>
					Exceeded Number of Characters Allowed
				</div>
				<div
					class="errorMessage"
					id="passwordTooShort"
					v-if="passwordTooShort && this.clicked"
				>
					Password length should be 10 or more.
				</div>
			</div>
			<div class="buttonsContainer">
				<n-button
					strong
					round
					color="#253759"
					size="large"
					id="loginBtn"
					@click="this.logIn"
					>Log In</n-button
				>

				<span>or</span>
				<router-link :to="'/register'">
					<n-button
						strong
						secondary
						round
						type="info"
						size="large"
						id="signupBtn"
						>Register instead</n-button
					>
				</router-link>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				role: "Student",
				email: "",
				password: "",
				clicked: false,
				data: { email: "user123@gmail.com", password: "Testing123!" },
				signInDialog: false,
				error: false,
				errorMessage: "",
			};
		},
		methods: {
			changeRole() {
				this.error = false;
				this.clicked = false;
				this.email = "";
				this.password = "";
				if (this.role == "Student") {
					this.role = "Teacher";
				} else {
					this.role = "Student";
				}
			},
			async logIn() {
				this.error = false;

				if (this.role == "Student") {
					if (
						this.hasEmail &&
						this.hasPassword &&
						this.checkValidity &&
						!this.passwordTooLong &&
						!this.passwordTooShort &&
						!this.emailTooLong
					) {
						if (
							this.email == this.data.email &&
							this.password == this.data.password
						) {
							this.$router.push("/welcome");
						} else {
							this.error = true;
							this.errorMessage = "Email or Password is incorrect.";
						}
					}
				} else if (this.role == "Teacher") {
					if (
						this.hasEmail &&
						this.hasPassword &&
						this.checkValidity &&
						!this.passwordTooLong &&
						!this.passwordTooShort &&
						!this.emailTooLong
					) {
						if (
							this.email == this.data.email &&
							this.password == this.data.password
						) {
							this.$router.push("/welcome");
						} else {
							this.error = true;
							this.errorMessage = "Email or Password is incorrect.";
						}
					}
				}

				this.clicked = true;
			},
		},

		computed: {
			checkValidity: function () {
				return /.+@.+\..+/.test(this.email);
			},
			hasEmail: function () {
				return this.email != "";
			},
			hasPassword: function () {
				return this.password != "";
			},
			passwordTooLong: function () {
				return this.password.length > 25;
			},
			passwordTooShort: function () {
				return this.password.length < 10;
			},
			emailTooLong: function () {
				return this.email.length > 50;
			},
		},
	};
</script>

<style scoped>
	.logInPage {
		min-height: 100vh;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}
	.titleContainer {
		padding: 5px;
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: 0px;
	}

	.title1,
	.title2 {
		margin: 0px;
		padding: 5px;
		font-size: 40px;
	}

	.title1 {
		color: #253759;
	}

	.title2 {
		color: #c0d9d9;
	}

	.loginForm {
		text-align: start;
		display: flex;
		justify-content: center;
		align-items: flex-start;
		flex-direction: column;
	}

	input:focus,
	textarea:focus,
	select:focus {
		outline: none;
	}

	label {
		font-size: 16px;
		font-weight: 600;
		color: #253759;
		padding-top: 10px;
	}

	input {
		border: none;
		border-bottom: 1px solid #253759;
		width: 275px;
		font-size: 18px;
		padding: 10px 0px;
		margin-bottom: 20px;
	}

	.selectRole {
		margin: auto;
		padding: 10px;
		font-size: 16px;
		border-radius: 5px;
	}

	.buttonsContainer {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		padding: 20px;
	}

	span {
		padding: 5px;
	}

	.errorMessage {
		color: rgb(212, 57, 57);
	}

	.error {
		color: rgb(212, 57, 57);
		border: 1px solid rgb(212, 57, 57);
		border-radius: 5px;
		padding: 0px 20px;
		margin: 10px;
	}
</style>
