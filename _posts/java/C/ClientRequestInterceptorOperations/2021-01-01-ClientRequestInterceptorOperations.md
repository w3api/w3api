---
title: ClientRequestInterceptorOperations
permalink: Java/ClientRequestInterceptorOperations
date: 2021-01-11
key: JavaJava.C.ClientRequestInterceptorOperations
category: java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClientRequestInterceptorOperations.description }}

## Sintaxis
~~~java
public interface ClientRequestInterceptorOperations extends InterceptorOperations
~~~

## Métodos
* [receive_exception()](/Java/ClientRequestInterceptorOperations/receive_exception)
* [receive_other()](/Java/ClientRequestInterceptorOperations/receive_other)
* [receive_reply()](/Java/ClientRequestInterceptorOperations/receive_reply)
* [send_poll()](/Java/ClientRequestInterceptorOperations/send_poll)
* [send_request()](/Java/ClientRequestInterceptorOperations/send_request)

## Ejemplo
~~~java
{{ site.data.Java.C.ClientRequestInterceptorOperations.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClientRequestInterceptorOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
