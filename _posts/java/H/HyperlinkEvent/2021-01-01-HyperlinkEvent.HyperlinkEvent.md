---
title: HyperlinkEvent.HyperlinkEvent()
permalink: /Java/HyperlinkEvent/HyperlinkEvent/
date: 2021-01-11
key: Java.H.HyperlinkEvent
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HyperlinkEvent.constructores valor="HyperlinkEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL u)
public HyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL u, String desc)
public HyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL u, String desc, Element sourceElement)
public HyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL u, String desc, Element sourceElement, InputEvent inputEvent)
~~~

## Parámetros
* **URL u**,  {% include w3api/param_description.html metodo=_dato parametro="URL u" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **InputEvent inputEvent**,  {% include w3api/param_description.html metodo=_dato parametro="InputEvent inputEvent" %}
* **HyperlinkEvent.EventType type**,  {% include w3api/param_description.html metodo=_dato parametro="HyperlinkEvent.EventType type" %}
* **String desc**,  {% include w3api/param_description.html metodo=_dato parametro="String desc" %}
* **Element sourceElement**,  {% include w3api/param_description.html metodo=_dato parametro="Element sourceElement" %}

## Clase Padre
[HyperlinkEvent](/Java/HyperlinkEvent/)

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
