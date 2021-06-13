---
title: IntStream.collect()
permalink: /Java/IntStream/collect/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="collect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R> R collect(Supplier<R> supplier, ObjIntConsumer<R> accumulator, BiConsumer<R,R> combiner)
~~~

## Parámetros
* **ObjIntConsumer&lt;R&gt; accumulator**,  {% include w3api/param_description.html metodo=_dato parametro="ObjIntConsumer<R> accumulator" %}
* **R&gt; combiner**,  {% include w3api/param_description.html metodo=_dato parametro="R> combiner" %}
* **Supplier&lt;R&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<R> supplier" %}
* **BiConsumer&lt;R**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<R" %}

## Clase Padre
[IntStream](/Java/IntStream/)

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
