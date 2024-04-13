---
title: Environment.exception()
permalink: /Java/Environment/exception/
date: 2021-01-11
key: Java.E.Environment
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Environment.metodos valor="exception" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Exception exception()
public abstract void exception(Exception except)
~~~

## Parámetros
* **Exception except**,  {% include w3api/param_description.html metodo=_dato parametro="Exception except" %}

## Clase Padre
[Environment](/Java/Environment/)

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
