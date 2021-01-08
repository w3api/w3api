---
title: Synthesizer.remapInstrument()
permalink: Java/Synthesizer/remapInstrument
date: 2021-01-04
key: JavaJava.S.Synthesizer
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Synthesizer.metodos valor="remapInstrument" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean remapInstrument(Instrument from, Instrument to)
~~~

## Parámetros
* **Instrument from**,  {% include w3api/param_description.html metodo=_data parametro="Instrument from" %}
* **Instrument to**,  {% include w3api/param_description.html metodo=_data parametro="Instrument to" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Synthesizer](/Java/Synthesizer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Synthesizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
