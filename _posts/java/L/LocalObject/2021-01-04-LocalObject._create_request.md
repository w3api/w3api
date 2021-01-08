---
title: LocalObject._create_request()
permalink: Java/LocalObject/_create_request
date: 2021-01-04
key: JavaJava.L.LocalObject
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalObject.metodos valor="_create_request" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Request _create_request(Context ctx, String operation, NVList arg_list, NamedValue result)
public Request _create_request(Context ctx, String operation, NVList arg_list, NamedValue result, ExceptionList exceptions, ContextList contexts)
~~~

## Parámetros
* **String operation**,  {% include w3api/param_description.html metodo=_data parametro="String operation" %}
* **NamedValue result**,  {% include w3api/param_description.html metodo=_data parametro="NamedValue result" %}
* **Context ctx**,  {% include w3api/param_description.html metodo=_data parametro="Context ctx" %}
* **ExceptionList exceptions**,  {% include w3api/param_description.html metodo=_data parametro="ExceptionList exceptions" %}
* **ContextList contexts**,  {% include w3api/param_description.html metodo=_data parametro="ContextList contexts" %}
* **NVList arg_list**,  {% include w3api/param_description.html metodo=_data parametro="NVList arg_list" %}

## Clase Padre
[LocalObject](/Java/LocalObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
