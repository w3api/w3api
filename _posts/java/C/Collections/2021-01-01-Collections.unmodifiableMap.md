---
title: Collections.unmodifiableMap()
permalink: /Java/Collections/unmodifiableMap/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="unmodifiableMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <K,V> Map<K,V> unmodifiableMap(Map<? extends K,? extends V> m)
~~~

## Parámetros
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends K" %}
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> m" %}

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
