---
title: Synthesizer.unloadInstruments()
permalink: Java/Synthesizer/unloadInstruments
date: 2021-01-04
key: JavaJava.S.Synthesizer
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Synthesizer.metodos valor="unloadInstruments" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void unloadInstruments(Soundbank soundbank, Patch[] patchList)
~~~

## Parámetros
* **Patch[] patchList**,  {% include w3api/param_description.html metodo=_data parametro="Patch[] patchList" %}
* **Soundbank soundbank**,  {% include w3api/param_description.html metodo=_data parametro="Soundbank soundbank" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
