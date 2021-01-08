---
title: Collections.synchronizedSet()
permalink: Java/Collections/synchronizedSet
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="synchronizedSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Set<T> synchronizedSet(Set<T> s)
~~~

## Parámetros
* **Set&lt;T&gt; s**,  {% include w3api/param_description.html metodo=_data parametro="Set<T> s" %}

## Clase Padre
[Collections](/Java/Collections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collections.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
