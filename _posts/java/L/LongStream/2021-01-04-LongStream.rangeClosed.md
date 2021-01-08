---
title: LongStream.rangeClosed()
permalink: Java/LongStream/rangeClosed
date: 2021-01-04
key: JavaJava.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="rangeClosed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static LongStream rangeClosed(long startInclusive, long endInclusive)
~~~

## Parámetros
* **long endInclusive**,  {% include w3api/param_description.html metodo=_data parametro="long endInclusive" %}
* **long startInclusive**,  {% include w3api/param_description.html metodo=_data parametro="long startInclusive" %}

## Clase Padre
[LongStream](/Java/LongStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
