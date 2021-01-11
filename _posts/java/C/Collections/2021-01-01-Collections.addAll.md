---
title: Collections.addAll()
permalink: Java/Collections/addAll
date: 2021-01-11
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> boolean addAll(Collection<? super T> c, T... elements)
~~~

## Parámetros
* **T... elements**,  {% include w3api/param_description.html metodo=_dato parametro="T... elements" %}
* **Collection&lt;? super T&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? super T> c" %}

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
