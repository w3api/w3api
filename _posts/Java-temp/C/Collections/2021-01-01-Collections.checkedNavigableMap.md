---
title: Collections.checkedNavigableMap()
permalink: /Java/Collections/checkedNavigableMap/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="checkedNavigableMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <K,V> NavigableMap<K,V> checkedNavigableMap(NavigableMap<K,V> m, Class<K> keyType, Class<V> valueType)
~~~

## Parámetros
* **Class&lt;V&gt; valueType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<V> valueType" %}
* **NavigableMap&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="NavigableMap<K" %}
* **Class&lt;K&gt; keyType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<K> keyType" %}
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
