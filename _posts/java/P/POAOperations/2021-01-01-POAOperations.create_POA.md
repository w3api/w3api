---
title: POAOperations.create_POA()
permalink: /Java/POAOperations/create_POA/
date: 2021-01-11
key: Java.P.POAOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAOperations.metodos valor="create_POA" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
POA create_POA(String adapter_name, POAManager a_POAManager, Policy[] policies) throws AdapterAlreadyExists, InvalidPolicy
~~~

## Parámetros
* **POAManager a_POAManager**,  {% include w3api/param_description.html metodo=_dato parametro="POAManager a_POAManager" %}
* **Policy[] policies**,  {% include w3api/param_description.html metodo=_dato parametro="Policy[] policies" %}
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
