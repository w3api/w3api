---
title: StreamSupport.intStream()
permalink: /Java/StreamSupport/intStream/
date: 2021-01-11
key: Java.S.StreamSupport
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamSupport.metodos valor="intStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static IntStream intStream(Supplier<? extends Spliterator.OfInt> supplier, int characteristics, boolean parallel)
public static IntStream intStream(Spliterator.OfInt spliterator, boolean parallel)
~~~

## Parámetros
* **Spliterator.OfInt spliterator**,  {% include w3api/param_description.html metodo=_dato parametro="Spliterator.OfInt spliterator" %}
* **Supplier&lt;? extends Spliterator.OfInt&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<? extends Spliterator.OfInt> supplier" %}
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
