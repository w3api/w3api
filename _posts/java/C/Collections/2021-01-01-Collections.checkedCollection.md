---
title: Collections.checkedCollection()
permalink: /Java/Collections/checkedCollection/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="checkedCollection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> Collection<E> checkedCollection(Collection<E> c, Class<E> type)
~~~

## Parámetros
* **Collection&lt;E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<E> c" %}
* **Class&lt;E&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<E> type" %}

## Clase Padre
[Collections](/Java/Collections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
