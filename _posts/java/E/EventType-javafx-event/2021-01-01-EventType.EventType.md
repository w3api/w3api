---
title: EventType.EventType()
permalink: Java/EventType-javafx-event/EventType
date: 2021-01-11
key: JavaJava.E.EventType-javafx-event
category: java
tags: ['java se', 'javafx.event', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventType-javafx-event.constructores valor="EventType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public EventType()
public EventType(String name)
public EventType(EventType<? super T> superType)
public EventType(EventType<? super T> superType, String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **EventType&lt;? super T&gt; superType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<? super T> superType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[EventType](/Java/EventType-javafx-event/)

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
