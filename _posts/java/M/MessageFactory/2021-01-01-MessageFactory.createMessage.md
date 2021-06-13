---
title: MessageFactory.createMessage()
permalink: /Java/MessageFactory/createMessage/
date: 2021-01-11
key: Java.M.MessageFactory
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageFactory.metodos valor="createMessage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SOAPMessage createMessage() throws SOAPException
public abstract SOAPMessage createMessage(MimeHeaders headers, InputStream in) throws IOException, SOAPException
~~~

## Parámetros
* **MimeHeaders headers**,  {% include w3api/param_description.html metodo=_dato parametro="MimeHeaders headers" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [SOAPException](/Java/SOAPException/)

## Clase Padre
[MessageFactory](/Java/MessageFactory/)

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
