---
title: StreamSupport.doubleStream()
permalink: /Java/StreamSupport/doubleStream/
date: 2021-01-11
key: Java.S.StreamSupport
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamSupport.metodos valor="doubleStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DoubleStream doubleStream(Supplier<? extends Spliterator.OfDouble> supplier, int characteristics, boolean parallel)
public static DoubleStream doubleStream(Spliterator.OfDouble spliterator, boolean parallel)
~~~

## Parámetros
* **Spliterator.OfDouble spliterator**,  {% include w3api/param_description.html metodo=_dato parametro="Spliterator.OfDouble spliterator" %}
* **Supplier&lt;? extends Spliterator.OfDouble&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<? extends Spliterator.OfDouble> supplier" %}
* **int characteristics**,  {% include w3api/param_description.html metodo=_dato parametro="int characteristics" %}
* **boolean parallel**,  {% include w3api/param_description.html metodo=_dato parametro="boolean parallel" %}

## Clase Padre
[StreamSupport](/Java/StreamSupport/)

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
