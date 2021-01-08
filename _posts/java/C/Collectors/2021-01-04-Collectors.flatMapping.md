---
title: Collectors.flatMapping()
permalink: Java/Collectors/flatMapping
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="flatMapping" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,U,A,R> Collector<T,?,R> flatMapping(Function<? super T,? extends Stream<? extends U>> mapper, Collector<? super U,A,R> downstream)
~~~

## Parámetros
* **? extends Stream&lt;? extends U&gt;&gt; mapper**,  {% include w3api/param_description.html metodo=_data parametro="? extends Stream<? extends U>> mapper" %}
* **Collector&lt;? super U**,  {% include w3api/param_description.html metodo=_data parametro="Collector<? super U" %}
* **A**,  {% include w3api/param_description.html metodo=_data parametro="A" %}
* **R&gt; downstream**,  {% include w3api/param_description.html metodo=_data parametro="R> downstream" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="Function<? super T" %}

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
