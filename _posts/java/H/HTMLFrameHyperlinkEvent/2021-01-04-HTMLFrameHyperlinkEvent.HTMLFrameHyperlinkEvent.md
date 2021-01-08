---
title: HTMLFrameHyperlinkEvent.HTMLFrameHyperlinkEvent()
permalink: Java/HTMLFrameHyperlinkEvent/HTMLFrameHyperlinkEvent
date: 2021-01-04
key: JavaJava.H.HTMLFrameHyperlinkEvent
category: java
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
* **HyperlinkEvent.EventType type**,  {% include w3api/param_description.html metodo=_data parametro="HyperlinkEvent.EventType type" %}
* **String targetFrame**,  {% include w3api/param_description.html metodo=_data parametro="String targetFrame" %}
* **InputEvent inputEvent**,  {% include w3api/param_description.html metodo=_data parametro="InputEvent inputEvent" %}
* **URL targetURL**,  {% include w3api/param_description.html metodo=_data parametro="URL targetURL" %}
* **String desc**,  {% include w3api/param_description.html metodo=_data parametro="String desc" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **Element sourceElement**,  {% include w3api/param_description.html metodo=_data parametro="Element sourceElement" %}

## Clase Padre
[HTMLFrameHyperlinkEvent](/Java/HTMLFrameHyperlinkEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HTMLFrameHyperlinkEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
