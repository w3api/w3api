---
title: MessageContext
permalink: /Java/MessageContext/
date: 2021-01-11
key: Java.M.MessageContext
category: Java
tags: ['java se', 'javax.xml.ws.handler', 'java.xml.ws', 'interface java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MessageContext.description }}

## Sintaxis
~~~java
public interface MessageContext extends Map<String,Object>
~~~

## Campos
* [HTTP_REQUEST_HEADERS](/Java/MessageContext/HTTP_REQUEST_HEADERS)
* [HTTP_REQUEST_METHOD](/Java/MessageContext/HTTP_REQUEST_METHOD)
* [HTTP_RESPONSE_CODE](/Java/MessageContext/HTTP_RESPONSE_CODE)
* [HTTP_RESPONSE_HEADERS](/Java/MessageContext/HTTP_RESPONSE_HEADERS)
* [INBOUND_MESSAGE_ATTACHMENTS](/Java/MessageContext/INBOUND_MESSAGE_ATTACHMENTS)
* [MESSAGE_OUTBOUND_PROPERTY](/Java/MessageContext/MESSAGE_OUTBOUND_PROPERTY)
* [OUTBOUND_MESSAGE_ATTACHMENTS](/Java/MessageContext/OUTBOUND_MESSAGE_ATTACHMENTS)
* [PATH_INFO](/Java/MessageContext/PATH_INFO)
* [QUERY_STRING](/Java/MessageContext/QUERY_STRING)
* [REFERENCE_PARAMETERS](/Java/MessageContext/REFERENCE_PARAMETERS)
* [SERVLET_CONTEXT](/Java/MessageContext/SERVLET_CONTEXT)
* [SERVLET_REQUEST](/Java/MessageContext/SERVLET_REQUEST)
* [SERVLET_RESPONSE](/Java/MessageContext/SERVLET_RESPONSE)
* [WSDL_DESCRIPTION](/Java/MessageContext/WSDL_DESCRIPTION)
* [WSDL_INTERFACE](/Java/MessageContext/WSDL_INTERFACE)
* [WSDL_OPERATION](/Java/MessageContext/WSDL_OPERATION)
* [WSDL_PORT](/Java/MessageContext/WSDL_PORT)
* [WSDL_SERVICE](/Java/MessageContext/WSDL_SERVICE)

## Métodos
* [getScope()](/Java/MessageContext/getScope)
* [setScope()](/Java/MessageContext/setScope)

## Ejemplo
~~~java
{{ site.data.Java.M.MessageContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MessageContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
