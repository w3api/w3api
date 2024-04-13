---
title: POAManagerOperations.deactivate()
permalink: /Java/POAManagerOperations/deactivate/
date: 2021-01-11
key: Java.P.POAManagerOperations
category: Java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAManagerOperations.metodos valor="deactivate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void deactivate(boolean etherealize_objects, boolean wait_for_completion) throws AdapterInactive
~~~

## Parámetros
* **boolean wait_for_completion**,  {% include w3api/param_description.html metodo=_dato parametro="boolean wait_for_completion" %}
* **boolean etherealize_objects**,  {% include w3api/param_description.html metodo=_dato parametro="boolean etherealize_objects" %}

## Clase Padre
[POAManagerOperations](/Java/POAManagerOperations/)

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
