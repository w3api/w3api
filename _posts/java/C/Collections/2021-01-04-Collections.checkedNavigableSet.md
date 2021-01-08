---
title: Collections.checkedNavigableSet()
permalink: Java/Collections/checkedNavigableSet
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="checkedNavigableSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> NavigableSet<E> checkedNavigableSet(NavigableSet<E> s, Class<E> type)
~~~

## Parámetros
* **Class&lt;E&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<E> type" %}
* **NavigableSet&lt;E&gt; s**,  {% include w3api/param_description.html metodo=_data parametro="NavigableSet<E> s" %}

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
