---
title: Collections.unmodifiableSet()
permalink: Java/Collections/unmodifiableSet
date: 2021-01-11
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="unmodifiableSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Set<T> unmodifiableSet(Set<? extends T> s)
~~~

## Parámetros
* **Set&lt;? extends T&gt; s**,  {% include w3api/param_description.html metodo=_dato parametro="Set<? extends T> s" %}

## Clase Padre
[Collections](/Java/Collections/)

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
