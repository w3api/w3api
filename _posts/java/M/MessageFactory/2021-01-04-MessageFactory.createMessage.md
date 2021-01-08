---
title: MessageFactory.createMessage()
permalink: Java/MessageFactory/createMessage
date: 2021-01-04
key: JavaJava.M.MessageFactory
category: java
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
* **MimeHeaders headers**,  {% include w3api/param_description.html metodo=_data parametro="MimeHeaders headers" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}

## Excepciones
[SOAPException](/Java/SOAPException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[MessageFactory](/Java/MessageFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MessageFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
