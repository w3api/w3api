---
title: SOAPHandler
permalink: /Java/SOAPHandler/
date: 2021-01-11
key: Java.S.SOAPHandler
category: Java
tags: ['java se', 'javax.xml.ws.handler.soap', 'java.xml.ws', 'interface java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SOAPHandler.description }}

## Sintaxis
~~~java
public interface SOAPHandler<T extends SOAPMessageContext> extends Handler<T>
~~~

## Métodos
* [getHeaders()](/Java/SOAPHandler/getHeaders)

## Ejemplo
~~~java
{{ site.data.Java.S.SOAPHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SOAPHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
