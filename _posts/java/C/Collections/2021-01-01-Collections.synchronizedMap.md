---
title: Collections.synchronizedMap()
permalink: /Java/Collections/synchronizedMap/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="synchronizedMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <K,V> Map<K,V> synchronizedMap(Map<K,V> m)
~~~

## Parámetros
* **Map&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<K" %}
* **V&gt; m**,  {% include w3api/param_description.html metodo=_dato parametro="V> m" %}

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
