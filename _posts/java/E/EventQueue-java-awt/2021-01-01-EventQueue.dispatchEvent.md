---
title: EventQueue.dispatchEvent()
permalink: /Java/EventQueue-java-awt/dispatchEvent/
date: 2021-01-11
key: Java.E.EventQueue-java-awt
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventQueue-java-awt.metodos valor="dispatchEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void dispatchEvent(AWTEvent event)
~~~

## Parámetros
* **AWTEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="AWTEvent event" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[EventQueue](/Java/EventQueue-java-awt/)

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
