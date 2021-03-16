<template>
    <v-container>
        <v-layout class="week-title-layout" justify-center py-5>
            Semana 3
        </v-layout>
        <v-layout pt-3 mb-5 class="week-description-layout">
            Makeover Monday Week 11 - World's Largest Crops
        </v-layout>
        <v-layout justify-center>
            <Tableau
                :url="'https://public.tableau.com/views/WorldsLargestCrops/Dashboard1?:language=es&:display_count=y&:origin=viz_share_link'">
            </Tableau>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    mounted () {
    }
}
</script>

<style lang="scss">
    @import '@/styles/week.scss';
</style>
