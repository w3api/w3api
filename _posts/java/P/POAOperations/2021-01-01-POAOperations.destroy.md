---
title: POAOperations.destroy()
permalink: /Java/POAOperations/destroy/
date: 2021-01-11
key: Java.P.POAOperations
category: java
tags: ['java se', 'org.omg.PortableServer', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.POAOperations.metodos valor="destroy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void destroy(boolean etherealize_objects, boolean wait_for_completion)
~~~

## Parámetros
* **boolean wait_for_completion**,  {% include w3api/param_description.html metodo=_dato parametro="boolean wait_for_completion" %}
* **boolean etherealize_objects**,  {% include w3api/param_description.html metodo=_dato parametro="boolean etherealize_objects" %}

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
