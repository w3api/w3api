---
title: WeakEventHandler
permalink: /Java/WeakEventHandler/
date: 2021-01-11
key: Java.W.WeakEventHandler
category: Java
tags: ['java se', 'javafx.event', 'javafx.base', 'clase java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WeakEventHandler.description }}

## Sintaxis
~~~java
public final class WeakEventHandler<T extends Event> extends Object implements EventHandler<T>
~~~

## Constructores
* [WeakEventHandler()](/Java/WeakEventHandler/WeakEventHandler/)

## Métodos
* [handle()](/Java/WeakEventHandler/handle)
* [wasGarbageCollected()](/Java/WeakEventHandler/wasGarbageCollected)

## Ejemplo
~~~java
{{ site.data.Java.W.WeakEventHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WeakEventHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
