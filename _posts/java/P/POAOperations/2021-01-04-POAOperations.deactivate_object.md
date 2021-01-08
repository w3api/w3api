---
title: POAOperations.deactivate_object()
permalink: Java/POAOperations/deactivate_object
date: 2021-01-04
key: JavaJava.P.POAOperations
category: java
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
* **byte[] oid**,  {% include w3api/param_description.html metodo=_data parametro="byte[] oid" %}

## Clase Padre
[POAOperations](/Java/POAOperations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.POAOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
