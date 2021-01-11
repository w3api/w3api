---
title: POAOperations.activate_object_with_id()
permalink: Java/POAOperations/activate_object_with_id
date: 2021-01-11
key: JavaJava.P.POAOperations
category: java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAOperations.metodos valor="activate_object_with_id" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void activate_object_with_id(byte[] id, Servant p_servant) throws ServantAlreadyActive, ObjectAlreadyActive, WrongPolicy
~~~

## Parámetros
* **byte[] id**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] id" %}
* **Servant p_servant**,  {% include w3api/param_description.html metodo=_dato parametro="Servant p_servant" %}

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
