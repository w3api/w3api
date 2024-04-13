---
title: HTMLFrameHyperlinkEvent.HTMLFrameHyperlinkEvent()
permalink: /Java/HTMLFrameHyperlinkEvent/HTMLFrameHyperlinkEvent/
date: 2021-01-11
key: Java.H.HTMLFrameHyperlinkEvent
category: Java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLFrameHyperlinkEvent.constructores valor="HTMLFrameHyperlinkEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HTMLFrameHyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL targetURL, String targetFrame)
public HTMLFrameHyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL targetURL, String desc, String targetFrame)
public HTMLFrameHyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL targetURL, String desc, Element sourceElement, InputEvent inputEvent, String targetFrame)
public HTMLFrameHyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL targetURL, String desc, Element sourceElement, String targetFrame)
public HTMLFrameHyperlinkEvent(Object source, HyperlinkEvent.EventType type, URL targetURL, Element sourceElement, String targetFrame)
~~~

## Parámetros
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **String targetFrame**,  {% include w3api/param_description.html metodo=_dato parametro="String targetFrame" %}
* **InputEvent inputEvent**,  {% include w3api/param_description.html metodo=_dato parametro="InputEvent inputEvent" %}
* **URL targetURL**,  {% include w3api/param_description.html metodo=_dato parametro="URL targetURL" %}
* **HyperlinkEvent.EventType type**,  {% include w3api/param_description.html metodo=_dato parametro="HyperlinkEvent.EventType type" %}
* **String desc**,  {% include w3api/param_description.html metodo=_dato parametro="String desc" %}
* **Element sourceElement**,  {% include w3api/param_description.html metodo=_dato parametro="Element sourceElement" %}

## Clase Padre
[HTMLFrameHyperlinkEvent](/Java/HTMLFrameHyperlinkEvent/)

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
