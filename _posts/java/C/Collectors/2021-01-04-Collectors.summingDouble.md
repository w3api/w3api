---
title: Collectors.summingDouble()
permalink: Java/Collectors/summingDouble
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="summingDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Collector<T,?,Double> summingDouble(ToDoubleFunction<? super T> mapper)
~~~

## Parámetros
* **ToDoubleFunction&lt;? super T&gt; mapper**,  {% include w3api/param_description.html metodo=_data parametro="ToDoubleFunction<? super T> mapper" %}

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
