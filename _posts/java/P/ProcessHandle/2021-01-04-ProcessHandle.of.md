---
title: ProcessHandle.of()
permalink: Java/ProcessHandle/of
date: 2021-01-04
key: JavaJava.P.ProcessHandle
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
* **long pid**,  {% include w3api/param_description.html metodo=_data parametro="long pid" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[ProcessHandle](/Java/ProcessHandle/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProcessHandle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
