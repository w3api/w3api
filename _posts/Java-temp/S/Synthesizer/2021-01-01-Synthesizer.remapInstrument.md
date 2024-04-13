---
title: Synthesizer.remapInstrument()
permalink: /Java/Synthesizer/remapInstrument/
date: 2021-01-11
key: Java.S.Synthesizer
category: Java
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
* **Instrument to**,  {% include w3api/param_description.html metodo=_dato parametro="Instrument to" %}
* **Instrument from**,  {% include w3api/param_description.html metodo=_dato parametro="Instrument from" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Synthesizer](/Java/Synthesizer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
