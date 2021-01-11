---
title: Collectors.toCollection()
permalink: Java/Collectors/toCollection
date: 2021-01-11
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="toCollection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,C extends Collection<T>>Collector<T,?,C> toCollection(Supplier<C> collectionFactory)
~~~

## Parámetros
* **Supplier&lt;C&gt; collectionFactory**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<C> collectionFactory" %}

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
