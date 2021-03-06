---
title: WatchService.poll()
permalink: /Java/WatchService/poll/
date: 2021-01-11
key: Java.W.WatchService
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WatchService.metodos valor="poll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
WatchKey poll()
WatchKey poll(long timeout, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

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
