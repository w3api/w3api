---
title: ProcessHandle.onExit()
permalink: Java/ProcessHandle/onExit
date: 2021-01-04
key: JavaJava.P.ProcessHandle
category: java
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

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProcessHandle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
