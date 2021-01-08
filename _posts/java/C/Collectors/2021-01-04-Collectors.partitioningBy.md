---
title: Collectors.partitioningBy()
permalink: Java/Collectors/partitioningBy
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="partitioningBy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Collector<T,?,Map<Boolean,List<T>>> partitioningBy(Predicate<? super T> predicate)
static <T,D,A> Collector<T,?,Map<Boolean,D>> partitioningBy(Predicate<? super T> predicate, Collector<? super T,A,D> downstream)
~~~

## Parámetros
* **Collector&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="Collector<? super T" %}
* **Predicate&lt;? super T&gt; predicate**,  {% include w3api/param_description.html metodo=_data parametro="Predicate<? super T> predicate" %}
* **A**,  {% include w3api/param_description.html metodo=_data parametro="A" %}
* **D&gt; downstream**,  {% include w3api/param_description.html metodo=_data parametro="D> downstream" %}

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
