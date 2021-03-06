---
title: StreamSupport.longStream()
permalink: /Java/StreamSupport/longStream/
date: 2021-01-11
key: Java.S.StreamSupport
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamSupport.metodos valor="longStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LongStream longStream(Supplier<? extends Spliterator.OfLong> supplier, int characteristics, boolean parallel)
public static LongStream longStream(Spliterator.OfLong spliterator, boolean parallel)
~~~

## Parámetros
* **Spliterator.OfLong spliterator**,  {% include w3api/param_description.html metodo=_dato parametro="Spliterator.OfLong spliterator" %}
* **int characteristics**,  {% include w3api/param_description.html metodo=_dato parametro="int characteristics" %}
* **Supplier&lt;? extends Spliterator.OfLong&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<? extends Spliterator.OfLong> supplier" %}
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
