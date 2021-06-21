---
title: ClientRequestInterceptorOperations.send_request()
permalink: /Java/ClientRequestInterceptorOperations/send_request/
date: 2021-01-11
key: Java.C.ClientRequestInterceptorOperations
category: Java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClientRequestInterceptorOperations.metodos valor="send_request" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void send_request(ClientRequestInfo ri) throws ForwardRequest
~~~

## Parámetros
* **ClientRequestInfo ri**,  {% include w3api/param_description.html metodo=_dato parametro="ClientRequestInfo ri" %}

## Clase Padre
[ClientRequestInterceptorOperations](/Java/ClientRequestInterceptorOperations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
