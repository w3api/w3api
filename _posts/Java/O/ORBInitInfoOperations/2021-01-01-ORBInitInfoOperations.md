---
title: ORBInitInfoOperations
permalink: /Java/ORBInitInfoOperations/
date: 2021-01-11
key: Java.O.ORBInitInfoOperations
category: Java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ORBInitInfoOperations.description }}

## Sintaxis
~~~java
public interface ORBInitInfoOperations
~~~

## Métodos
* [add_client_request_interceptor()](/Java/ORBInitInfoOperations/add_client_request_interceptor)
* [add_ior_interceptor()](/Java/ORBInitInfoOperations/add_ior_interceptor)
* [add_server_request_interceptor()](/Java/ORBInitInfoOperations/add_server_request_interceptor)
* [allocate_slot_id()](/Java/ORBInitInfoOperations/allocate_slot_id)
* [arguments()](/Java/ORBInitInfoOperations/arguments)
* [codec_factory()](/Java/ORBInitInfoOperations/codec_factory)
* [orb_id()](/Java/ORBInitInfoOperations/orb_id)
* [register_initial_reference()](/Java/ORBInitInfoOperations/register_initial_reference)
* [register_policy_factory()](/Java/ORBInitInfoOperations/register_policy_factory)
* [resolve_initial_references()](/Java/ORBInitInfoOperations/resolve_initial_references)

## Ejemplo
~~~java
{{ site.data.Java.O.ORBInitInfoOperations.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ORBInitInfoOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
