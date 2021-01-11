---
title: SOAPMessageContext.setMessage()
permalink: Java/SOAPMessageContext/setMessage
date: 2021-01-11
key: JavaJava.S.SOAPMessageContext
category: java
tags: ['java se', 'javax.xml.ws.handler.soap', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPMessageContext.metodos valor="setMessage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setMessage(SOAPMessage message)
~~~

## Parámetros
* **SOAPMessage message**,  {% include w3api/param_description.html metodo=_dato parametro="SOAPMessage message" %}

## Excepciones
[WebServiceException](/Java/WebServiceException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[SOAPMessageContext](/Java/SOAPMessageContext/)

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
