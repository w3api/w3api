---
title: Collectors.collectingAndThen()
permalink: /Java/Collectors/collectingAndThen/
date: 2021-01-11
key: Java.C.Collectors
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="collectingAndThen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,A,R,RR> Collector<T,A,RR> collectingAndThen(Collector<T,A,R> downstream, Function<R,RR> finisher)
~~~

## Parámetros
* **Function&lt;R**,  {% include w3api/param_description.html metodo=_dato parametro="Function<R" %}
* **R&gt; downstream**,  {% include w3api/param_description.html metodo=_dato parametro="R> downstream" %}
* **RR&gt; finisher**,  {% include w3api/param_description.html metodo=_dato parametro="RR> finisher" %}
* **Collector&lt;T**,  {% include w3api/param_description.html metodo=_dato parametro="Collector<T" %}
* **A**,  {% include w3api/param_description.html metodo=_dato parametro="A" %}

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
