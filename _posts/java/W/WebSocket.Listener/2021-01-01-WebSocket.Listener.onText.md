---
title: WebSocket.Listener.onText()
permalink: Java/WebSocket/Listener/onText
date: 2021-01-11
key: JavaJava.W.WebSocket.Listener
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.Listener.metodos valor="onText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default CompletionStage<?> onText(WebSocket webSocket, CharSequence message, WebSocket.MessagePart part)
~~~

## Parámetros
* **CharSequence message**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence message" %}
* **WebSocket webSocket**,  {% include w3api/param_description.html metodo=_dato parametro="WebSocket webSocket" %}
* **WebSocket.MessagePart part**,  {% include w3api/param_description.html metodo=_dato parametro="WebSocket.MessagePart part" %}

## Clase Padre
[WebSocket.Listener](/Java/WebSocket/Listener/)

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
