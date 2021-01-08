---
title: Collections.replaceAll()
permalink: Java/Collections/replaceAll
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="replaceAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> boolean replaceAll(List<T> list, T oldVal, T newVal)
~~~

## Parámetros
* **T oldVal**,  {% include w3api/param_description.html metodo=_data parametro="T oldVal" %}
* **List&lt;T&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="List<T> list" %}
* **T newVal**,  {% include w3api/param_description.html metodo=_data parametro="T newVal" %}

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
