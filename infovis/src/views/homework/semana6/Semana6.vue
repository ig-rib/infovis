<template>
    <div>
        <v-layout class="week-title-layout" justify-center py-5>
            Semana 6
        </v-layout>
        <v-layout pt-3 mb-5 class="week-description-layout">
            Población por Provincias Argentinas
        </v-layout>
        <v-layout justify-center>
            <Tableau
                ref="tableau"
                :url="url">
            </Tableau>
        </v-layout>
    </div>
</template>

<script>
export default {
    data () {
        return {
            url: 'https://public.tableau.com/shared/HXS67PCQG?:display_count=y&:origin=viz_share_link'
        }
    }
}
</script>

<style lang="scss">
    @import '@/styles/week.scss';
</style>
