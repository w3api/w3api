---
title: WatchService
permalink: /Java/WatchService/
date: 2021-01-11
key: Java.W.WatchService
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WatchService.description }}

## Sintaxis
~~~java
public interface WatchService extends Closeable
~~~

## Métodos
* [close()](/Java/WatchService/close)
* [poll()](/Java/WatchService/poll)
* [take()](/Java/WatchService/take)

## Ejemplo
~~~java
{{ site.data.Java.W.WatchService.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WatchService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
