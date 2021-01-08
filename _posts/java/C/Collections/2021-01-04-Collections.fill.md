---
title: Collections.fill()
permalink: Java/Collections/fill
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="fill" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> void fill(List<? super T> list, T obj)
~~~

## Parámetros
* **List&lt;? super T&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="List<? super T> list" %}
* **T obj**,  {% include w3api/param_description.html metodo=_data parametro="T obj" %}

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
