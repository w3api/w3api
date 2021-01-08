---
title: Collections.reverse()
permalink: Java/Collections/reverse
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="reverse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void reverse(List<?> list)
~~~

## Parámetros
* **List&lt;?&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="List<?> list" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
