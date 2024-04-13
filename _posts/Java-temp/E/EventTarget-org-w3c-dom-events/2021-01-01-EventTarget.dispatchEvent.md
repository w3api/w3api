---
title: EventTarget.dispatchEvent()
permalink: /Java/EventTarget-org-w3c-dom-events/dispatchEvent/
date: 2021-01-11
key: Java.E.EventTarget-org-w3c-dom-events
category: Java
tags: ['java se', 'org.w3c.dom.events', 'java.xml', 'metodo java', 'Java 1.5', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventTarget-org-w3c-dom-events.metodos valor="dispatchEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean dispatchEvent(Event evt) throws EventException
~~~

## Parámetros
* **Event evt**,  {% include w3api/param_description.html metodo=_dato parametro="Event evt" %}

## Excepciones
[EventException](/Java/EventException/)

## Clase Padre
[EventTarget](/Java/EventTarget-org-w3c-dom-events/)

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
