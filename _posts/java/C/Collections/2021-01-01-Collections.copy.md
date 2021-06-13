---
title: Collections.copy()
permalink: /Java/Collections/copy/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="copy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> void copy(List<? super T> dest, List<? extends T> src)
~~~

## Parámetros
* **List&lt;? extends T&gt; src**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends T> src" %}
* **List&lt;? super T&gt; dest**,  {% include w3api/param_description.html metodo=_dato parametro="List<? super T> dest" %}

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
