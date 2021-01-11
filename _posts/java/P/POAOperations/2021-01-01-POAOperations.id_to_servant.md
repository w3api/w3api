---
title: POAOperations.id_to_servant()
permalink: Java/POAOperations/id_to_servant
date: 2021-01-11
key: JavaJava.P.POAOperations
category: java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAOperations.metodos valor="id_to_servant" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Servant id_to_servant(byte[] oid) throws ObjectNotActive, WrongPolicy
~~~

## Parámetros
* **byte[] oid**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] oid" %}

## Clase Padre
[POAOperations](/Java/POAOperations/)

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
