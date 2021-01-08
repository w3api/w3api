---
title: Collectors.summingInt()
permalink: Java/Collectors/summingInt
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="summingInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Collector<T,?,Integer> summingInt(ToIntFunction<? super T> mapper)
~~~

## Parámetros
* **ToIntFunction&lt;? super T&gt; mapper**,  {% include w3api/param_description.html metodo=_data parametro="ToIntFunction<? super T> mapper" %}

## Clase Padre
[Collectors](/Java/Collectors/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collectors.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
