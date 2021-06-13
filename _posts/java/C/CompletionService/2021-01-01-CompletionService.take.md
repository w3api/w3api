---
title: CompletionService.take()
permalink: /Java/CompletionService/take/
date: 2021-01-11
key: Java.C.CompletionService
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionService.metodos valor="take" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Future<V> take() throws InterruptedException
~~~

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[CompletionService](/Java/CompletionService/)

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
