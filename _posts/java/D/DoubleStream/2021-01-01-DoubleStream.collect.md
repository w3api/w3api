---
title: DoubleStream.collect()
permalink: /Java/DoubleStream/collect/
date: 2021-01-11
key: Java.D.DoubleStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="collect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R> R collect(Supplier<R> supplier, ObjDoubleConsumer<R> accumulator, BiConsumer<R,R> combiner)
~~~

## Parámetros
* **ObjDoubleConsumer&lt;R&gt; accumulator**,  {% include w3api/param_description.html metodo=_dato parametro="ObjDoubleConsumer<R> accumulator" %}
* **R&gt; combiner**,  {% include w3api/param_description.html metodo=_dato parametro="R> combiner" %}
* **Supplier&lt;R&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<R> supplier" %}
* **BiConsumer&lt;R**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<R" %}

## Clase Padre
[DoubleStream](/Java/DoubleStream/)

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
