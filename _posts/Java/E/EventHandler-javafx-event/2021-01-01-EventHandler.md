---
title: EventHandler
permalink: /Java/EventHandler-javafx-event/
date: 2021-01-11
key: Java.E.EventHandler-javafx-event
category: Java
tags: ['java se', 'javafx.event', 'javafx.base', 'interface java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EventHandler-javafx-event.description }}

## Sintaxis
~~~java
@FunctionalInterface public interface EventHandler<T extends Event> extends EventListener
~~~

## Métodos
* [handle()](/Java/EventHandler-javafx-event/handle/)

## Ejemplo
~~~java
{{ site.data.Java.E.EventHandler-javafx-event.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventHandler-javafx-event.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
