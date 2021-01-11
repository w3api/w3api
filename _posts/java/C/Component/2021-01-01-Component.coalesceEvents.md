---
title: Component.coalesceEvents()
permalink: Java/Component/coalesceEvents
date: 2021-01-11
key: JavaJava.C.Component
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="coalesceEvents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected AWTEvent coalesceEvents(AWTEvent existingEvent, AWTEvent newEvent)
~~~

## Parámetros
* **AWTEvent newEvent**,  {% include w3api/param_description.html metodo=_dato parametro="AWTEvent newEvent" %}
* **AWTEvent existingEvent**,  {% include w3api/param_description.html metodo=_dato parametro="AWTEvent existingEvent" %}

## Clase Padre
[Component](/Java/Component/)

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
