---
title: LongStream.collect()
permalink: Java/LongStream/collect
date: 2021-01-11
key: Java.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="collect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R> R collect(Supplier<R> supplier, ObjLongConsumer<R> accumulator, BiConsumer<R,R> combiner)
~~~

## Parámetros
* **R&gt; combiner**,  {% include w3api/param_description.html metodo=_dato parametro="R> combiner" %}
* **Supplier&lt;R&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<R> supplier" %}
* **ObjLongConsumer&lt;R&gt; accumulator**,  {% include w3api/param_description.html metodo=_dato parametro="ObjLongConsumer<R> accumulator" %}
* **BiConsumer&lt;R**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<R" %}

## Clase Padre
[LongStream](/Java/LongStream/)

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
