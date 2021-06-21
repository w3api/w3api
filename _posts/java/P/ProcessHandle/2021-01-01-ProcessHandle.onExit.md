---
title: ProcessHandle.onExit()
permalink: /Java/ProcessHandle/onExit/
date: 2021-01-11
key: Java.P.ProcessHandle
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessHandle.metodos valor="onExit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletableFuture<ProcessHandle> onExit()
~~~

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[ProcessHandle](/Java/ProcessHandle/)

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
