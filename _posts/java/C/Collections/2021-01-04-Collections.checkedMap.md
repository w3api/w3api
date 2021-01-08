---
title: Collections.checkedMap()
permalink: Java/Collections/checkedMap
date: 2021-01-04
key: JavaJava.C.Collections
category: java
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
* **Class&lt;K&gt; keyType**,  {% include w3api/param_description.html metodo=_data parametro="Class<K> keyType" %}
* **Class&lt;V&gt; valueType**,  {% include w3api/param_description.html metodo=_data parametro="Class<V> valueType" %}
* **V&gt; m**,  {% include w3api/param_description.html metodo=_data parametro="V> m" %}
* **Map&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="Map<K" %}

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
