---
title: LongStream.of()
permalink: Java/LongStream/of
date: 2021-01-04
key: JavaJava.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static LongStream of(long t)
static LongStream of(long... values)
~~~

## Parámetros
* **long t**,  {% include w3api/param_description.html metodo=_data parametro="long t" %}
* **long... values**,  {% include w3api/param_description.html metodo=_data parametro="long... values" %}

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
