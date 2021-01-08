---
title: EventQueue.remove()
permalink: Java/EventQueue-com-sun-jdi-event/remove
date: 2021-01-04
key: JavaJava.E.EventQueue-com-sun-jdi-event
category: java
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
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [VMDisconnectedException](/Java/VMDisconnectedException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[EventQueue](/Java/EventQueue-com-sun-jdi-event/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventQueue-com-sun-jdi-event.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
