<template>
	<div class="welcome">
		<div class="titleContainer">
			<h1 class="title1">Math</h1>
			<h1 class="title2">World</h1>
		</div>

		<div class="messageContainer">
			<h1 class="message" id="main_message">Hello, World!</h1>
		</div>
		<div class="buttonsContainer">
			<router-link :to="'/'">
				<n-button strong round color="#253759" size="large" id="loginBtn"
					>Log Out</n-button
				>
			</router-link>
		</div>

		<div class="content" id="sub_message">Welcome to Math World</div>
	</div>
</template>

<script>
	export default {};
</script>

<style scoped>
	.welcome {
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
	.title2,
	.message {
		margin: 0px;
		padding: 5px;
		font-size: 40px;
	}

	.title1,
	.message {
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
