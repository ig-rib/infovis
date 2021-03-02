<template>
    <div>
        <v-layout my-5 mx-2>
            <v-flex>
                <v-btn rounded outlined color="primary" @click="goHome">
                    IR AL INICIO
                </v-btn>
            </v-flex>
        </v-layout>
        <router-view/>
    </div>
</template>

<script>
export default {
    methods: {
        goHome () {
            this.$router.push({name: 'Home'})
        }
    }
}
</script>

<style lang="scss">

</style>
