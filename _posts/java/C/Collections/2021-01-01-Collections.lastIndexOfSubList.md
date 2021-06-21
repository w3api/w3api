---
title: Collections.lastIndexOfSubList()
permalink: /Java/Collections/lastIndexOfSubList/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="lastIndexOfSubList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int lastIndexOfSubList(List<?> source, List<?> target)
~~~

## Parámetros
* **List&lt;?&gt; source**,  {% include w3api/param_description.html metodo=_dato parametro="List<?> source" %}
* **List&lt;?&gt; target**,  {% include w3api/param_description.html metodo=_dato parametro="List<?> target" %}

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
