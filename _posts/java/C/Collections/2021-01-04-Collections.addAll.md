---
title: Collections.addAll()
permalink: Java/Collections/addAll
date: 2021-01-04
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
* **Collection&lt;? super T&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? super T> c" %}
* **T... elements**,  {% include w3api/param_description.html metodo=_data parametro="T... elements" %}

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
