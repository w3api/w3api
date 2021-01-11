---
title: InvocationEvent.InvocationEvent()
permalink: Java/InvocationEvent/InvocationEvent
date: 2021-01-11
key: JavaJava.I.InvocationEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InvocationEvent.constructores valor="InvocationEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected InvocationEvent(Object source, int id, Runnable runnable, Object notifier, boolean catchThrowables)
public InvocationEvent(Object source, Runnable runnable)
public InvocationEvent(Object source, Runnable runnable, Object notifier, boolean catchThrowables)
public InvocationEvent(Object source, Runnable runnable, Runnable listener, boolean catchThrowables)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **Runnable runnable**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable runnable" %}
* **Object notifier**,  {% include w3api/param_description.html metodo=_dato parametro="Object notifier" %}
* **boolean catchThrowables**,  {% include w3api/param_description.html metodo=_dato parametro="boolean catchThrowables" %}
* **Runnable listener**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable listener" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InvocationEvent](/Java/InvocationEvent/)

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
