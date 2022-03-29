<template>
	<div class="registerPage">
		<router-link :to="'/'">
			<div class="titleContainer">
				<h1 class="title1">Math</h1>
				<h1 class="title2">World</h1>
			</div>
		</router-link>

		<div class="registerFormContainer">
			<h1>Register</h1>
			<div>as</div>
			<br />
			<n-button-group>
				<n-button
					strong
					round
					:color="role == 'Student' ? '#253759' : none"
					id="asStudent"
					@click="role = 'Student'"
				>
					Student
				</n-button>
				<n-button
					strong
					round
					:color="role == 'Teacher' ? '#253759' : none"
					id="asTeacher"
					@click="role = 'Teacher'"
				>
					Teacher
				</n-button>
			</n-button-group>
			<div><br /></div>
			<div class="outerCon">
				<n-grid x-gap="12" :cols="'1 s:1 m:2 l:2 xl:2'" responsive="screen">
					<n-gi>
						<div class="registerForm">
							<label for="first_name">First Name *</label>
							<input
								type="text"
								name="first_name"
								id="first_name"
								v-model="first_name"
							/>
							<div
								class="errorMessage"
								v-if="!this.first_name && this.clickedRegister"
								id="firstNameRequired"
							>
								First name is required
							</div>
							<label for="last_name">Last Name *</label>
							<input
								type="text"
								name="last_name"
								id="last_name"
								v-model="last_name"
							/>
							<div
								class="errorMessage"
								v-if="!this.last_name && this.clickedRegister"
								id="lastNameRequired"
							>
								Last name is required
							</div>
							<label for="school">School *</label>
							<input type="text" name="school" id="school" v-model="school" />
							<div
								class="errorMessage"
								v-if="!this.school && this.clickedRegister"
								id="schoolRequired"
							>
								School is required
							</div>
						</div>
					</n-gi>

					<n-gi>
						<div class="registerForm">
							<label for="text">Email *</label>
							<input type="text" name="email" id="email" v-model="email" />
							<div
								class="errorMessage"
								v-if="!this.email && this.clickedRegister"
								id="emailRequired"
							>
								Email is required
							</div>
							<div
								class="errorMessage"
								id="emailTooLong"
								v-if="emailTooLong && this.email && this.clickedRegister"
							>
								Length must not exceed 50 characters.
							</div>

							<div
								class="errorMessage"
								v-if="!checkValidity && this.email && this.clickedRegister"
								id="emailMustValid"
							>
								Email must be valid
							</div>
							<label for="password">Password *</label>
							<input
								type="password"
								name="password"
								id="password"
								v-model="password"
							/>
							<div
								class="errorMessage"
								id="passwordRequired"
								v-if="!this.password && this.clickedRegister"
							>
								Password is required
							</div>
							<div
								class="errorMessageP"
								id="passwordNoLower"
								v-if="!this.hasLower && this.password"
							>
								Password must have lowercase letter.
							</div>
							<div
								class="errorMessageP"
								id="passwordNoUpper"
								v-if="!this.hasUpper && this.password"
							>
								Password must have uppercase letter.
							</div>
							<div
								class="errorMessageP"
								id="passwordNoNumber"
								v-if="!this.hasNumber && this.password"
							>
								Password must have a number.
							</div>
							<div
								class="errorMessageP"
								id="passwordNoChar"
								v-if="!this.hasChar && this.password"
							>
								Password must have a character.
							</div>

							<div
								class="errorMessageP"
								id="invalidPasswordLength"
								v-if="!this.greaterThan && this.password"
							>
								Length must be 10 or more.
							</div>
							<div
								class="errorMessage"
								id="passwordTooLong"
								v-if="passwordTooLong && this.password"
							>
								Length must not exceed 25 characters.
							</div>
							<label for="repeat_password">Repeat Password *</label>
							<input
								type="password"
								name="repeat_password"
								id="repeat_password"
								v-model="repeat_password"
							/>
							<div
								class="errorMessage"
								id="passwordDontMatch"
								v-if="!this.passwordMatch"
							>
								Password doesn't match
							</div>
						</div>
					</n-gi>
				</n-grid>
			</div>

			<div class="buttonsContainer">
				<n-button
					strong
					secondary
					round
					type="info"
					size="large"
					id="signupBtn"
					@click="this.register"
					>Register</n-button
				>

				<span>or</span>

				<router-link :to="'/login'">
					<n-button strong round color="#253759" size="large" id="loginBtn"
						>Log In Instead</n-button
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
				first_name: "",
				last_name: "",
				school: "",
				email: "",
				password: "",
				repeat_password: "",
				clicked: false,
				clickedRegister: false,
			};
		},
		methods: {
			register() {
				this.clickedRegister = true;
				if (this.validated) {
					const user = {
						first_name: this.first_name,
						last_name: this.last_name,
						school: this.school,
						email: this.email,
						password1: this.password,
						password2: this.repeat_password,
					};

					this.$router.push("/welcome");
				}
			},
		},

		computed: {
			validated: function () {
				if (
					this.first_name &&
					this.last_name &&
					this.school &&
					this.checkValidity &&
					this.passwordMatch &&
					this.hasLower &&
					this.hasUpper &&
					this.hasNumber &&
					this.hasChar &&
					this.greaterThan &&
					!this.passwordTooLong &&
					!this.emailTooLong
				) {
					return true;
				}
				return false;
			},

			checkValidity: function () {
				return /.+@.+\..+/.test(this.email);
			},

			passwordMatch: function () {
				return this.repeat_password == this.password;
			},

			hasLower: function () {
				return /^(?=.*?[a-z])/.test(this.password);
			},
			hasUpper: function () {
				return /^(?=.*?[A-Z])/.test(this.password);
			},
			hasNumber: function () {
				return /^(?=.*?[0-9])/.test(this.password);
			},
			hasChar: function () {
				return /^(?=.*?[#?!@$%^&*-])/.test(this.password);
			},
			greaterThan: function () {
				return this.password.length > 10;
			},
			passwordTooLong: function () {
				return this.password.length > 25;
			},
			emailTooLong: function () {
				return this.email.length > 50;
			},
		},
	};
</script>

<style scoped>
	.registerPage {
		min-height: 100vh;
		display: flex;
		align-items: center;
		flex-direction: column;
	}

	.titleContainer {
		padding: 10px;
		display: flex;
		margin-top: 50px;
		justify-content: center;
		align-items: center;
		cursor: pointer;
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

	.registerForm {
		text-align: start;
		display: flex;
		justify-content: center;
		align-items: flex-start;
		flex-direction: column;
		padding: 25px;
	}

	.outerCon {
		display: flex;
		justify-content: center;
		align-items: flex-start;
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
		padding-top: 20px;
	}

	input {
		border: none;
		border-bottom: 1px solid #253759;
		width: 275px;
		font-size: 18px;
		padding: 10px 0px;
		margin-bottom: 20px;
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
		color: red;
	}

	.errorMessageP {
		color: red;
	}
</style>
