---
title: Collectors.maxBy()
permalink: Java/Collectors/maxBy
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="maxBy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Collector<T,?,Optional<T>> maxBy(Comparator<? super T> comparator)
~~~

## Parámetros
* **Comparator&lt;? super T&gt; comparator**,  {% include w3api/param_description.html metodo=_data parametro="Comparator<? super T> comparator" %}

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
