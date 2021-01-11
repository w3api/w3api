---
title: Watchable.register()
permalink: Java/Watchable/register
date: 2021-01-11
key: JavaJava.W.Watchable
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.Watchable.metodos valor="register" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
WatchKey register(WatchService watcher, WatchEvent.Kind<?>... events) throws IOException
WatchKey register(WatchService watcher, WatchEvent.Kind<?>[] events, WatchEvent.Modifier... modifiers) throws IOException
~~~

## Parámetros
* **WatchService watcher**,  {% include w3api/param_description.html metodo=_dato parametro="WatchService watcher" %}
* **WatchEvent.Modifier... modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="WatchEvent.Modifier... modifiers" %}
* **WatchEvent.Kind&lt;?&gt;[] events**,  {% include w3api/param_description.html metodo=_dato parametro="WatchEvent.Kind<?>[] events" %}
* **WatchEvent.Kind&lt;?&gt;... events**,  {% include w3api/param_description.html metodo=_dato parametro="WatchEvent.Kind<?>... events" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [ClosedWatchServiceException](/Java/ClosedWatchServiceException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Watchable](/Java/Watchable/)

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
