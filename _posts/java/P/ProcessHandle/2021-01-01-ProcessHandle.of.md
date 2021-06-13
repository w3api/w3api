---
title: ProcessHandle.of()
permalink: /Java/ProcessHandle/of/
date: 2021-01-11
key: Java.P.ProcessHandle
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessHandle.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static Optional<ProcessHandle> of(long pid)
~~~

## Parámetros
* **long pid**,  {% include w3api/param_description.html metodo=_dato parametro="long pid" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ProcessHandle](/Java/ProcessHandle/)

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
