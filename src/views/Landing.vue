<template>
	<div class="landing">
		<div class="titleContainer">
			<h1 class="title1">Math</h1>
			<h1 class="title2">World</h1>
		</div>
		<div class="buttonsContainer">
			<router-link :to="'/login'">
				<n-button strong round color="#253759" size="large" id="loginBtn"
					>Log In</n-button
				>
			</router-link>

			<span>or</span>
			<router-link :to="'/register'">
				<n-button strong secondary round type="info" size="large" id="signupBtn"
					>Register</n-button
				>
			</router-link>
		</div>

		<div class="content">For Teachers and For Students</div>
	</div>
</template>

<script>
	export default {};
</script>

<style scoped>
	.landing {
		min-height: 100vh;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}

	.titleContainer {
		padding: 10px;
		display: flex;
		margin-top: -200px;
		justify-content: center;
		align-items: center;
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

	span {
		padding: 10px;
	}

	.buttonsContainer {
		padding-bottom: 20px;
	}

	.n-button {
		margin: 5px;
	}
</style>
