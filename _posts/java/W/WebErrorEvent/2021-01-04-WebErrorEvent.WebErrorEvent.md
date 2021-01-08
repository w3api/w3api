---
title: WebErrorEvent.WebErrorEvent()
permalink: Java/WebErrorEvent/WebErrorEvent
date: 2021-01-04
key: JavaJava.W.WebErrorEvent
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
* **EventType&lt;WebErrorEvent&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="EventType<WebErrorEvent> type" %}
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Throwable exception**,  {% include w3api/param_description.html metodo=_data parametro="Throwable exception" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Clase Padre
[WebErrorEvent](/Java/WebErrorEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebErrorEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
