---
title: Collectors.summingLong()
permalink: /Java/Collectors/summingLong/
date: 2021-01-11
key: Java.C.Collectors
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="summingLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Collector<T,?,Long> summingLong(ToLongFunction<? super T> mapper)
~~~

## Parámetros
* **ToLongFunction&lt;? super T&gt; mapper**,  {% include w3api/param_description.html metodo=_dato parametro="ToLongFunction<? super T> mapper" %}

## Clase Padre
[Collectors](/Java/Collectors/)

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
