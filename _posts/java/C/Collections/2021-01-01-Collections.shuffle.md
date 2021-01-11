---
title: Collections.shuffle()
permalink: Java/Collections/shuffle
date: 2021-01-11
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="shuffle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void shuffle(List<?> list)
public static void shuffle(List<?> list, Random rnd)
~~~

## Parámetros
* **Random rnd**,  {% include w3api/param_description.html metodo=_dato parametro="Random rnd" %}
* **List&lt;?&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<?> list" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Collections](/Java/Collections/)

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
