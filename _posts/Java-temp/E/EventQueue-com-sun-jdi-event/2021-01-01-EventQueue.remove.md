---
title: EventQueue.remove()
permalink: /Java/EventQueue-com-sun-jdi-event/remove/
date: 2021-01-11
key: Java.E.EventQueue-com-sun-jdi-event
category: Java
tags: ['java se', 'com.sun.jdi.event', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventQueue-com-sun-jdi-event.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
EventSet remove() throws InterruptedException
EventSet remove(long timeout) throws InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}

## Excepciones
[VMDisconnectedException](/Java/VMDisconnectedException/), [InterruptedException](/Java/InterruptedException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[EventQueue](/Java/EventQueue-com-sun-jdi-event/)

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
