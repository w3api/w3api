---
title: WatchService.take()
permalink: /Java/WatchService/take/
date: 2021-01-11
key: Java.W.WatchService
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WatchService.metodos valor="take" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
WatchKey take() throws InterruptedException
~~~

## Excepciones
[ClosedWatchServiceException](/Java/ClosedWatchServiceException/), [InterruptedException](/Java/InterruptedException/)

## Clase Padre
[WatchService](/Java/WatchService/)

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
