---
title: ORBInitInfoOperations.add_server_request_interceptor()
permalink: /Java/ORBInitInfoOperations/add_server_request_interceptor/
date: 2021-01-11
key: Java.O.ORBInitInfoOperations
category: Java
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
* **ServerRequestInterceptor interceptor**,  {% include w3api/param_description.html metodo=_dato parametro="ServerRequestInterceptor interceptor" %}

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
