---
title: LongStream.collect()
permalink: Java/LongStream/collect
date: 2021-01-04
key: JavaJava.L.LongStream
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
* **R&gt; combiner**,  {% include w3api/param_description.html metodo=_data parametro="R> combiner" %}
* **BiConsumer&lt;R**,  {% include w3api/param_description.html metodo=_data parametro="BiConsumer<R" %}
* **Supplier&lt;R&gt; supplier**,  {% include w3api/param_description.html metodo=_data parametro="Supplier<R> supplier" %}
* **ObjLongConsumer&lt;R&gt; accumulator**,  {% include w3api/param_description.html metodo=_data parametro="ObjLongConsumer<R> accumulator" %}

## Clase Padre
[LongStream](/Java/LongStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
