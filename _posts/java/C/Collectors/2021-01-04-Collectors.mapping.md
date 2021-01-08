---
title: Collectors.mapping()
permalink: Java/Collectors/mapping
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="mapping" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,U,A,R> Collector<T,?,R> mapping(Function<? super T,? extends U> mapper, Collector<? super U,A,R> downstream)
~~~

## Parámetros
* **Collector&lt;? super U**,  {% include w3api/param_description.html metodo=_data parametro="Collector<? super U" %}
* **A**,  {% include w3api/param_description.html metodo=_data parametro="A" %}
* **? extends U&gt; mapper**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> mapper" %}
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
