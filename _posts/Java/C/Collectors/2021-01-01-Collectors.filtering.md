---
title: Collectors.filtering()
permalink: /Java/Collectors/filtering/
date: 2021-01-11
key: Java.C.Collectors
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="filtering" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,A,R> Collector<T,?,R> filtering(Predicate<? super T> predicate, Collector<? super T,A,R> downstream)
~~~

## Parámetros
* **R&gt; downstream**,  {% include w3api/param_description.html metodo=_dato parametro="R> downstream" %}
* **A**,  {% include w3api/param_description.html metodo=_dato parametro="A" %}
* **Predicate&lt;? super T&gt; predicate**,  {% include w3api/param_description.html metodo=_dato parametro="Predicate<? super T> predicate" %}
* **Collector&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Collector<? super T" %}

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
