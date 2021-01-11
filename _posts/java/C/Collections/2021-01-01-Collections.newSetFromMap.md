---
title: Collections.newSetFromMap()
permalink: Java/Collections/newSetFromMap
date: 2021-01-11
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="newSetFromMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E> Set<E> newSetFromMap(Map<E,Boolean> map)
~~~

## Parámetros
* **Map&lt;E**,  {% include w3api/param_description.html metodo=_dato parametro="Map<E" %}
* **Boolean&gt; map**,  {% include w3api/param_description.html metodo=_dato parametro="Boolean> map" %}

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
