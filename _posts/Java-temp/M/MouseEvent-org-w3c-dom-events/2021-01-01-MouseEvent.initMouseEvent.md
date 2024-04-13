---
title: MouseEvent.initMouseEvent()
permalink: /Java/MouseEvent-org-w3c-dom-events/initMouseEvent/
date: 2021-01-11
key: Java.M.MouseEvent-org-w3c-dom-events
category: Java
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
* **String typeArg**,  {% include w3api/param_description.html metodo=_dato parametro="String typeArg" %}
* **EventTarget relatedTargetArg**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget relatedTargetArg" %}
* **int clientYArg**,  {% include w3api/param_description.html metodo=_dato parametro="int clientYArg" %}
* **boolean ctrlKeyArg**,  {% include w3api/param_description.html metodo=_dato parametro="boolean ctrlKeyArg" %}
* **boolean shiftKeyArg**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shiftKeyArg" %}
* **int detailArg**,  {% include w3api/param_description.html metodo=_dato parametro="int detailArg" %}
* **short buttonArg**,  {% include w3api/param_description.html metodo=_dato parametro="short buttonArg" %}
* **boolean metaKeyArg**,  {% include w3api/param_description.html metodo=_dato parametro="boolean metaKeyArg" %}
* **int clientXArg**,  {% include w3api/param_description.html metodo=_dato parametro="int clientXArg" %}
* **AbstractView viewArg**,  {% include w3api/param_description.html metodo=_dato parametro="AbstractView viewArg" %}
* **int screenXArg**,  {% include w3api/param_description.html metodo=_dato parametro="int screenXArg" %}
* **boolean cancelableArg**,  {% include w3api/param_description.html metodo=_dato parametro="boolean cancelableArg" %}
* **int screenYArg**,  {% include w3api/param_description.html metodo=_dato parametro="int screenYArg" %}
* **boolean altKeyArg**,  {% include w3api/param_description.html metodo=_dato parametro="boolean altKeyArg" %}
* **boolean canBubbleArg**,  {% include w3api/param_description.html metodo=_dato parametro="boolean canBubbleArg" %}

## Clase Padre
[MouseEvent](/Java/MouseEvent-org-w3c-dom-events/)

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
