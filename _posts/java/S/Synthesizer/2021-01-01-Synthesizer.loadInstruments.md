---
title: Synthesizer.loadInstruments()
permalink: Java/Synthesizer/loadInstruments
date: 2021-01-11
key: JavaJava.S.Synthesizer
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Synthesizer.metodos valor="loadInstruments" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean loadInstruments(Soundbank soundbank, Patch[] patchList)
~~~

## Parámetros
* **Soundbank soundbank**,  {% include w3api/param_description.html metodo=_dato parametro="Soundbank soundbank" %}
* **Patch[] patchList**,  {% include w3api/param_description.html metodo=_dato parametro="Patch[] patchList" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
