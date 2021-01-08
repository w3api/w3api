---
title: ORBInitInfoOperations.add_server_request_interceptor()
permalink: Java/ORBInitInfoOperations/add_server_request_interceptor
date: 2021-01-04
key: JavaJava.O.ORBInitInfoOperations
category: java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ORBInitInfoOperations.metodos valor="add_server_request_interceptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void add_server_request_interceptor(ServerRequestInterceptor interceptor) throws DuplicateName
~~~

## Parámetros
* **ServerRequestInterceptor interceptor**,  {% include w3api/param_description.html metodo=_data parametro="ServerRequestInterceptor interceptor" %}

## Clase Padre
[ORBInitInfoOperations](/Java/ORBInitInfoOperations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ORBInitInfoOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
