---
title: POAOperations.find_POA()
permalink: /Java/POAOperations/find_POA/
date: 2021-01-11
key: Java.P.POAOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAOperations.metodos valor="find_POA" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
POA find_POA(String adapter_name, boolean activate_it) throws AdapterNonExistent
~~~

## Parámetros
* **boolean activate_it**,  {% include w3api/param_description.html metodo=_dato parametro="boolean activate_it" %}
* **String adapter_name**,  {% include w3api/param_description.html metodo=_dato parametro="String adapter_name" %}

## Clase Padre
[POAOperations](/Java/POAOperations/)

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
