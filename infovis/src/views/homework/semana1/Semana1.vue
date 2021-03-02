<template>
    <v-container>
        <v-layout class="week-title-layout" justify-center py-5>
            Semana 1
        </v-layout>
        <v-layout pt-3 class="week-description-layout">
            Conceptos nuevos en "A Tour Through The Visualization Zoo" e intento de visualización del dataset de Makeover Monday, "Seats Held by Women in National Parliaments and Governments"
        </v-layout>
        <v-layout justify-center>
            <v-tabs centered>
                <v-tab>
                    Visualization Zoo
                </v-tab>
                <v-tab>
                    Makeover Monday
                </v-tab>
                <v-tab-item>
                    <visualization-zoo></visualization-zoo>
                </v-tab-item>
                <v-tab-item>
                    <makeover-monday></makeover-monday>
                </v-tab-item>
            </v-tabs>
        </v-layout>
    </v-container>
</template>

<script>
import VisualizationZoo from '@/views/homework/semana1/VisualizationZoo.vue'
import MakeoverMonday from '@/views/homework/semana1/MakeoverMonday.vue'
export default {
    components: {
        'visualization-zoo': VisualizationZoo,
        'makeover-monday': MakeoverMonday
    }
}
</script>

<style lang="scss">
    @import '@/styles/week.scss';
</style>
