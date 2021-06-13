---
title: ServantActivatorOperations.incarnate()
permalink: /Java/ServantActivatorOperations/incarnate/
date: 2021-01-11
key: Java.S.ServantActivatorOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServantActivatorOperations.metodos valor="incarnate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Servant incarnate(byte[] oid, POA adapter) throws ForwardRequest
~~~

## Parámetros
* **byte[] oid**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] oid" %}
* **POA adapter**,  {% include w3api/param_description.html metodo=_dato parametro="POA adapter" %}

## Clase Padre
[ServantActivatorOperations](/Java/ServantActivatorOperations/)

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
