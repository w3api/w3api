---
title: EventType.getEventType()
permalink: Java/EventType-jdk-jfr/getEventType
date: 2021-01-11
key: JavaJava.E.EventType-jdk-jfr
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventType-jdk-jfr.metodos valor="getEventType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static EventType getEventType(Class<? extends Event> eventClass)
~~~

## Parámetros
* **Class&lt;? extends Event&gt; eventClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Event> eventClass" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[EventType](/Java/EventType-jdk-jfr/)

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
