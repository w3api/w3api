---
title: MouseEvent.initMouseEvent()
permalink: Java/MouseEvent-org-w3c-dom-events/initMouseEvent
date: 2021-01-04
key: JavaJava.M.MouseEvent-org-w3c-dom-events
category: java
tags: ['java se', 'org.w3c.dom.events', 'java.xml', 'metodo java', 'Java 1.5', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseEvent-org-w3c-dom-events.metodos valor="initMouseEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void initMouseEvent(String typeArg, boolean canBubbleArg, boolean cancelableArg, AbstractView viewArg, int detailArg, int screenXArg, int screenYArg, int clientXArg, int clientYArg, boolean ctrlKeyArg, boolean altKeyArg, boolean shiftKeyArg, boolean metaKeyArg, short buttonArg, EventTarget relatedTargetArg)
~~~

## Parámetros
* **boolean canBubbleArg**,  {% include w3api/param_description.html metodo=_data parametro="boolean canBubbleArg" %}
* **boolean ctrlKeyArg**,  {% include w3api/param_description.html metodo=_data parametro="boolean ctrlKeyArg" %}
* **int clientXArg**,  {% include w3api/param_description.html metodo=_data parametro="int clientXArg" %}
* **boolean altKeyArg**,  {% include w3api/param_description.html metodo=_data parametro="boolean altKeyArg" %}
* **boolean shiftKeyArg**,  {% include w3api/param_description.html metodo=_data parametro="boolean shiftKeyArg" %}
* **String typeArg**,  {% include w3api/param_description.html metodo=_data parametro="String typeArg" %}
* **int screenYArg**,  {% include w3api/param_description.html metodo=_data parametro="int screenYArg" %}
* **int detailArg**,  {% include w3api/param_description.html metodo=_data parametro="int detailArg" %}
* **int clientYArg**,  {% include w3api/param_description.html metodo=_data parametro="int clientYArg" %}
* **boolean metaKeyArg**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaKeyArg" %}
* **short buttonArg**,  {% include w3api/param_description.html metodo=_data parametro="short buttonArg" %}
* **AbstractView viewArg**,  {% include w3api/param_description.html metodo=_data parametro="AbstractView viewArg" %}
* **int screenXArg**,  {% include w3api/param_description.html metodo=_data parametro="int screenXArg" %}
* **boolean cancelableArg**,  {% include w3api/param_description.html metodo=_data parametro="boolean cancelableArg" %}
* **EventTarget relatedTargetArg**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget relatedTargetArg" %}

## Clase Padre
[MouseEvent](/Java/MouseEvent-org-w3c-dom-events/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MouseEvent-org-w3c-dom-events.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
