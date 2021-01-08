---
title: EventTarget.addEventListener()
permalink: Java/EventTarget-org-w3c-dom-events/addEventListener
date: 2021-01-04
key: JavaJava.E.EventTarget-org-w3c-dom-events
category: java
tags: ['java se', 'org.w3c.dom.events', 'java.xml', 'metodo java', 'Java 1.5', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventTarget-org-w3c-dom-events.metodos valor="addEventListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addEventListener(String type, EventListener listener, boolean useCapture)
~~~

## Parámetros
* **boolean useCapture**,  {% include w3api/param_description.html metodo=_data parametro="boolean useCapture" %}
* **EventListener listener**,  {% include w3api/param_description.html metodo=_data parametro="EventListener listener" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}

## Clase Padre
[EventTarget](/Java/EventTarget-org-w3c-dom-events/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventTarget-org-w3c-dom-events.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
