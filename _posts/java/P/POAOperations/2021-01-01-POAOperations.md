---
title: POAOperations
permalink: /Java/POAOperations/
date: 2021-01-11
key: Java.P.POAOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.POAOperations.description }}

## Sintaxis
~~~java
public interface POAOperations
~~~

## Métodos
* [activate_object()](/Java/POAOperations/activate_object)
* [activate_object_with_id()](/Java/POAOperations/activate_object_with_id)
* [create_id_assignment_policy()](/Java/POAOperations/create_id_assignment_policy)
* [create_id_uniqueness_policy()](/Java/POAOperations/create_id_uniqueness_policy)
* [create_implicit_activation_policy()](/Java/POAOperations/create_implicit_activation_policy)
* [create_lifespan_policy()](/Java/POAOperations/create_lifespan_policy)
* [create_POA()](/Java/POAOperations/create_POA)
* [create_reference()](/Java/POAOperations/create_reference)
* [create_reference_with_id()](/Java/POAOperations/create_reference_with_id)
* [create_request_processing_policy()](/Java/POAOperations/create_request_processing_policy)
* [create_servant_retention_policy()](/Java/POAOperations/create_servant_retention_policy)
* [create_thread_policy()](/Java/POAOperations/create_thread_policy)
* [deactivate_object()](/Java/POAOperations/deactivate_object)
* [destroy()](/Java/POAOperations/destroy)
* [find_POA()](/Java/POAOperations/find_POA)
* [get_servant()](/Java/POAOperations/get_servant)
* [get_servant_manager()](/Java/POAOperations/get_servant_manager)
* [id()](/Java/POAOperations/id)
* [id_to_reference()](/Java/POAOperations/id_to_reference)
* [id_to_servant()](/Java/POAOperations/id_to_servant)
* [reference_to_id()](/Java/POAOperations/reference_to_id)
* [reference_to_servant()](/Java/POAOperations/reference_to_servant)
* [servant_to_id()](/Java/POAOperations/servant_to_id)
* [servant_to_reference()](/Java/POAOperations/servant_to_reference)
* [set_servant()](/Java/POAOperations/set_servant)
* [set_servant_manager()](/Java/POAOperations/set_servant_manager)
* [the_activator()](/Java/POAOperations/the_activator)
* [the_children()](/Java/POAOperations/the_children)
* [the_name()](/Java/POAOperations/the_name)
* [the_parent()](/Java/POAOperations/the_parent)
* [the_POAManager()](/Java/POAOperations/the_POAManager)

## Ejemplo
~~~java
{{ site.data.Java.P.POAOperations.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.POAOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
