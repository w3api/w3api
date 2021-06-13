---
title: WebErrorEvent.WebErrorEvent()
permalink: /Java/WebErrorEvent/WebErrorEvent/
date: 2021-01-11
key: Java.W.WebErrorEvent
category: java
tags: ['java se', 'javafx.scene.web', 'javafx.web', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebErrorEvent.constructores valor="WebErrorEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WebErrorEvent(Object source, EventType<WebErrorEvent> type, String message, Throwable exception)
~~~

## Parámetros
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **Throwable exception**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable exception" %}
* **EventType&lt;WebErrorEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<WebErrorEvent> type" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[WebErrorEvent](/Java/WebErrorEvent/)

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
