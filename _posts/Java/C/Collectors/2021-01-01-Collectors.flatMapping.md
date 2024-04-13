---
title: Collectors.flatMapping()
permalink: /Java/Collectors/flatMapping/
date: 2021-01-11
key: Java.C.Collectors
category: Java
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
* **Collector&lt;? super U**,  {% include w3api/param_description.html metodo=_dato parametro="Collector<? super U" %}
* **R&gt; downstream**,  {% include w3api/param_description.html metodo=_dato parametro="R> downstream" %}
* **? extends Stream&lt;? extends U&gt;&gt; mapper**,  {% include w3api/param_description.html metodo=_dato parametro="? extends Stream<? extends U>> mapper" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super T" %}
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
