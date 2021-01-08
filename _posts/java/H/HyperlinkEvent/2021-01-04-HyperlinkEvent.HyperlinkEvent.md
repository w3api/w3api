---
title: HyperlinkEvent.HyperlinkEvent()
permalink: Java/HyperlinkEvent/HyperlinkEvent
date: 2021-01-04
key: JavaJava.H.HyperlinkEvent
category: java
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
* **HyperlinkEvent.EventType type**,  {% include w3api/param_description.html metodo=_data parametro="HyperlinkEvent.EventType type" %}
* **InputEvent inputEvent**,  {% include w3api/param_description.html metodo=_data parametro="InputEvent inputEvent" %}
* **URL u**,  {% include w3api/param_description.html metodo=_data parametro="URL u" %}
* **String desc**,  {% include w3api/param_description.html metodo=_data parametro="String desc" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **Element sourceElement**,  {% include w3api/param_description.html metodo=_data parametro="Element sourceElement" %}

## Clase Padre
[HyperlinkEvent](/Java/HyperlinkEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HyperlinkEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
