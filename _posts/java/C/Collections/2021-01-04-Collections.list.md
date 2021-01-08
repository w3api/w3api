---
title: Collections.list()
permalink: Java/Collections/list
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> ArrayList<T> list(Enumeration<T> e)
~~~

## Parámetros
* **Enumeration&lt;T&gt; e**,  {% include w3api/param_description.html metodo=_data parametro="Enumeration<T> e" %}

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
