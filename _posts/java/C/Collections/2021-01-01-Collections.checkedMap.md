---
title: Collections.checkedMap()
permalink: /Java/Collections/checkedMap/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="checkedMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <K,V> Map<K,V> checkedMap(Map<K,V> m, Class<K> keyType, Class<V> valueType)
~~~

## Parámetros
* **Map&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<K" %}
* **Class&lt;V&gt; valueType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<V> valueType" %}
* **Class&lt;K&gt; keyType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<K> keyType" %}
* **V&gt; m**,  {% include w3api/param_description.html metodo=_dato parametro="V> m" %}

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
