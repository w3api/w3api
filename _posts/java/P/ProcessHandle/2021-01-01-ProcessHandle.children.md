---
title: ProcessHandle.children()
permalink: /Java/ProcessHandle/children/
date: 2021-01-11
key: Java.P.ProcessHandle
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessHandle.metodos valor="children" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Stream<ProcessHandle> children()
~~~

## Excepciones
[SecurityException](/Java/SecurityException/)

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
