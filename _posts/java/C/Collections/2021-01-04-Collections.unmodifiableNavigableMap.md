---
title: Collections.unmodifiableNavigableMap()
permalink: Java/Collections/unmodifiableNavigableMap
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="unmodifiableNavigableMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <K,V> NavigableMap<K,V> unmodifiableNavigableMap(NavigableMap<K,? extends V> m)
~~~

## Parámetros
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> m" %}
* **NavigableMap&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="NavigableMap<K" %}

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
