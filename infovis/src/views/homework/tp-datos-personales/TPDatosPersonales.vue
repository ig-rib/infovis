<template>
    <div>
        <v-layout class="week-title-layout" justify-center py-5>
            TP Infovis - Datos Personales
        </v-layout>
        <v-layout pt-3 mb-5 justify-center class="week-description-layout">
            Noticias
        </v-layout>
        <!-- <v-layout>
            <iframe src="@/assets/tp-datos-personales/datospersonales.html"></iframe>
        </v-layout> -->
        <v-layout justify-center>
            <Tableau
                width="1020px"
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
            url: 'https://public.tableau.com/views/DatosPersonalesActualizado/Dashboard1?:language=es&:display_count=y&publish=yes&:origin=viz_share_link'
        }
    }
}
</script>

<style lang="scss">
    @import '@/styles/week.scss';
</style>
