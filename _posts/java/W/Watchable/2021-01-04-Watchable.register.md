---
title: Watchable.register()
permalink: Java/Watchable/register
date: 2021-01-04
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
* **WatchEvent.Kind&lt;?&gt;[] events**,  {% include w3api/param_description.html metodo=_data parametro="WatchEvent.Kind<?>[] events" %}
* **WatchEvent.Modifier... modifiers**,  {% include w3api/param_description.html metodo=_data parametro="WatchEvent.Modifier... modifiers" %}
* **WatchEvent.Kind&lt;?&gt;... events**,  {% include w3api/param_description.html metodo=_data parametro="WatchEvent.Kind<?>... events" %}
* **WatchService watcher**,  {% include w3api/param_description.html metodo=_data parametro="WatchService watcher" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClosedWatchServiceException](/Java/ClosedWatchServiceException/), [IOException](/Java/IOException/)

## Clase Padre
[Watchable](/Java/Watchable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.Watchable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
