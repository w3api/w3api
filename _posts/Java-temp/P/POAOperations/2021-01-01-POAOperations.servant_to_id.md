---
title: POAOperations.servant_to_id()
permalink: /Java/POAOperations/servant_to_id/
date: 2021-01-11
key: Java.P.POAOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAOperations.metodos valor="servant_to_id" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
byte[] servant_to_id(Servant p_servant) throws ServantNotActive, WrongPolicy
~~~

## Parámetros
* **Servant p_servant**,  {% include w3api/param_description.html metodo=_dato parametro="Servant p_servant" %}

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
