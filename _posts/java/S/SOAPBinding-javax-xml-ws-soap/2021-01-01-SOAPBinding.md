---
title: SOAPBinding
permalink: Java/SOAPBinding-javax-xml-ws-soap
date: 2021-01-11
key: JavaJava.S.SOAPBinding-javax-xml-ws-soap
category: java
tags: ['java se', 'javax.xml.ws.soap', 'java.xml.ws', 'interface java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SOAPBinding-javax-xml-ws-soap.description }}

## Sintaxis
~~~java
public interface SOAPBinding extends Binding
~~~

## Campos
* [SOAP11HTTP_BINDING](/Java/SOAPBinding-javax-xml-ws-soap/SOAP11HTTP_BINDING)
* [SOAP11HTTP_MTOM_BINDING](/Java/SOAPBinding-javax-xml-ws-soap/SOAP11HTTP_MTOM_BINDING)
* [SOAP12HTTP_BINDING](/Java/SOAPBinding-javax-xml-ws-soap/SOAP12HTTP_BINDING)
* [SOAP12HTTP_MTOM_BINDING](/Java/SOAPBinding-javax-xml-ws-soap/SOAP12HTTP_MTOM_BINDING)

## Métodos
* [getMessageFactory()](/Java/SOAPBinding-javax-xml-ws-soap/getMessageFactory)
* [getRoles()](/Java/SOAPBinding-javax-xml-ws-soap/getRoles)
* [getSOAPFactory()](/Java/SOAPBinding-javax-xml-ws-soap/getSOAPFactory)
* [isMTOMEnabled()](/Java/SOAPBinding-javax-xml-ws-soap/isMTOMEnabled)
* [setMTOMEnabled()](/Java/SOAPBinding-javax-xml-ws-soap/setMTOMEnabled)
* [setRoles()](/Java/SOAPBinding-javax-xml-ws-soap/setRoles)

## Ejemplo
~~~java
{{ site.data.Java.S.SOAPBinding-javax-xml-ws-soap.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SOAPBinding-javax-xml-ws-soap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
