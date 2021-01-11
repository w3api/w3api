---
title: ORBInitInfoOperations.add_client_request_interceptor()
permalink: Java/ORBInitInfoOperations/add_client_request_interceptor
date: 2021-01-11
key: JavaJava.O.ORBInitInfoOperations
category: java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ORBInitInfoOperations.metodos valor="add_client_request_interceptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void add_client_request_interceptor(ClientRequestInterceptor interceptor) throws DuplicateName
~~~

## Parámetros
* **ClientRequestInterceptor interceptor**,  {% include w3api/param_description.html metodo=_dato parametro="ClientRequestInterceptor interceptor" %}

## Clase Padre
[ORBInitInfoOperations](/Java/ORBInitInfoOperations/)

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
