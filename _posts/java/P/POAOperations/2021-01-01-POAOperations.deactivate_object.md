---
title: POAOperations.deactivate_object()
permalink: /Java/POAOperations/deactivate_object/
date: 2021-01-11
key: Java.P.POAOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAOperations.metodos valor="deactivate_object" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void deactivate_object(byte[] oid) throws ObjectNotActive, WrongPolicy
~~~

## Parámetros
* **byte[] oid**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] oid" %}

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
