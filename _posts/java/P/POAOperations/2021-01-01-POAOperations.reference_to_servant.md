---
title: POAOperations.reference_to_servant()
permalink: /Java/POAOperations/reference_to_servant/
date: 2021-01-11
key: Java.P.POAOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAOperations.metodos valor="reference_to_servant" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Servant reference_to_servant(Object reference) throws ObjectNotActive, WrongPolicy, WrongAdapter
~~~

## Parámetros
* **Object reference**,  {% include w3api/param_description.html metodo=_dato parametro="Object reference" %}

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
