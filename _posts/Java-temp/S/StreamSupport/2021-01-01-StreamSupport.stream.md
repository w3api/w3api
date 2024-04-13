---
title: StreamSupport.stream()
permalink: /Java/StreamSupport/stream/
date: 2021-01-11
key: Java.S.StreamSupport
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamSupport.metodos valor="stream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Stream<T> stream(Supplier<? extends Spliterator<T>> supplier, int characteristics, boolean parallel)
static <T> Stream<T> stream(Spliterator<T> spliterator, boolean parallel)
~~~

## Parámetros
* **Spliterator&lt;T&gt; spliterator**,  {% include w3api/param_description.html metodo=_dato parametro="Spliterator<T> spliterator" %}
* **Supplier&lt;? extends Spliterator&lt;T&gt;&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<? extends Spliterator<T>> supplier" %}
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
