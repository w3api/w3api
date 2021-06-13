---
title: Collections.checkedList()
permalink: /Java/Collections/checkedList/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="checkedList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> List<E> checkedList(List<E> list, Class<E> type)
~~~

## Parámetros
* **Class&lt;E&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<E> type" %}
* **List&lt;E&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<E> list" %}

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
