---
title: IntStream.of()
permalink: /Java/IntStream/of/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static IntStream of(int t)
static IntStream of(int... values)
~~~

## Parámetros
* **int t**,  {% include w3api/param_description.html metodo=_dato parametro="int t" %}
* **int... values**,  {% include w3api/param_description.html metodo=_dato parametro="int... values" %}

## Clase Padre
[IntStream](/Java/IntStream/)

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
