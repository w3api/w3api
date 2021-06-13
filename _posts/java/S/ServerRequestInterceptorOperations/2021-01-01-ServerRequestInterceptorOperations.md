---
title: ServerRequestInterceptorOperations
permalink: /Java/ServerRequestInterceptorOperations/
date: 2021-01-11
key: Java.S.ServerRequestInterceptorOperations
category: Java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ServerRequestInterceptorOperations.description }}

## Sintaxis
~~~java
public interface ServerRequestInterceptorOperations extends InterceptorOperations
~~~

## Métodos
* [receive_request()](/Java/ServerRequestInterceptorOperations/receive_request)
* [receive_request_service_contexts()](/Java/ServerRequestInterceptorOperations/receive_request_service_contexts)
* [send_exception()](/Java/ServerRequestInterceptorOperations/send_exception)
* [send_other()](/Java/ServerRequestInterceptorOperations/send_other)
* [send_reply()](/Java/ServerRequestInterceptorOperations/send_reply)

## Ejemplo
~~~java
{{ site.data.Java.S.ServerRequestInterceptorOperations.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServerRequestInterceptorOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
