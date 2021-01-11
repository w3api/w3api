---
title: HandshakeCompletedEvent.HandshakeCompletedEvent()
permalink: Java/HandshakeCompletedEvent/HandshakeCompletedEvent
date: 2021-01-11
key: JavaJava.H.HandshakeCompletedEvent
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HandshakeCompletedEvent.constructores valor="HandshakeCompletedEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HandshakeCompletedEvent(SSLSocket sock, SSLSession s)
~~~

## Parámetros
* **SSLSession s**,  {% include w3api/param_description.html metodo=_dato parametro="SSLSession s" %}
* **SSLSocket sock**,  {% include w3api/param_description.html metodo=_dato parametro="SSLSocket sock" %}

## Clase Padre
[HandshakeCompletedEvent](/Java/HandshakeCompletedEvent/)

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
